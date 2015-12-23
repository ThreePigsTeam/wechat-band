# -*- coding: utf-8 -*-

from .. import db
from . import *
from User import *
import random


petstage_nature = db.Table('petstage_nature',
                              db.Column('pet_stage_id',
                                        db.Integer,
                                        db.ForeignKey('pet_stages.id')),
                              db.Column('nature_id',
                                        db.Integer,
                                        db.ForeignKey('natures.id')))


# 用户宠物表
class Pet(db.Model):
    __tablename__ = 'pets'
    id      = db.Column(db.Integer, primary_key = True)
    name    = db.Column(db.String(200), default = 'cute', nullable = False)
    exp     = db.Column(db.Integer, default = 0)
    level   = db.Column(db.Integer, default = 0)
    basic_cost = db.Column(db.Integer, default = 2000)
    age     = db.Column(db.Integer, default = 0, nullable = False)
    sex     = db.Column(db.String(10), default = 'male', nullable = False)
    hunger  = db.Column(db.Integer, default = 0, nullable = False)
    health  = db.Column(db.Integer, default = 100, nullable = False)
    status  = db.Column(db.String(20), default = 'fit', nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pet_id  = db.Column(db.Integer, db.ForeignKey('original_pets.id'))
    stage   = db.Column(db.Integer, default = 0)


# 宠物原型表
class OriginalPet(db.Model):
    __tablename__ = 'original_pets'
    id         = db.Column(db.Integer, primary_key = True)
    name       = db.Column(db.String(50), nullable = False)
    pets       = db.relationship('Pet', backref='original_pet', lazy='dynamic')
    price      = db.Column(db.Integer, default = 100000)
    amount     = db.Column(db.Integer, default = 100)
    picture    = db.Column(db.String(100))
    basic_cost = db.Column(db.Integer, default = 2000)
    pet_stages = db.relationship('PetStage', backref='original_pet', lazy='dynamic')
    #natures    = db.relationship('Nature', secondary = originalpet_nature, backref = 'original_pets', lazy = 'dynamic')


# 宠物属性表
class Nature(db.Model):
    __tablename__ = 'natures'
    id            = db.Column(db.Integer, primary_key = True)
    name          = db.Column(db.String(30), nullable = False)
    pet_stages    = db.relationship('PetStage', secondary = petstage_nature, backref = 'natures', lazy = 'dynamic')


# 进化阶段
class PetStage(db.Model):
    __tablename__ = 'pet_stages'
    id              = db.Column(db.Integer, primary_key = True)
    name            = db.Column(db.String(30))
    original_pet_id = db.Column(db.Integer, db.ForeignKey('original_pets.id'))
    level_require   = db.Column(db.Integer, default = 1)
    picture         = db.Column(db.String(100))


# 等级经验对照表
class Level(db.Model):
    __tablename__ = 'levels'
    id      = db.Column(db.Integer, primary_key = True)
    exp     = db.Column(db.Integer)






# Pet

def add_pet(openid, original_pet_id = 1, name = 'cute', age = 0, sex = 'male', hunger = 0, health = 100, status = 'fit'):
    original_pet = OriginalPet.query.filter_by(id = original_pet_id).first()
    if original_pet == None:
        return 1

    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return 2

    if user.pets.filter_by(original_pet = original_pet).first() != None:
        return 3

    pet = Pet(user = user, original_pet = original_pet, name = name, age = age, sex = sex, hunger = hunger, health = health, status = status)
    db.session.add(pet)
    db.session.commit()
    return 0


def add_original_pet(name, price = 100000, amount = 100, basic_cost = 2000, picture = ''):
    original_pet = OriginalPet.query.filter_by(name = name).first()
    if original_pet == None:
        original_pet = OriginalPet(name = name, price = price, amount = amount, basic_cost = basic_cost, picture = picture)
    else:
        original_pet.price = price
        original_pet.amount = amount
        original_pet.basic_cost = basic_cost
        original_pet.picture = picture

    db.session.add(original_pet)
    db.session.commit()


def add_pet_stage(name, original_pet, level_require = 10, picture = '', natures = []):
    pet_stage = PetStage.query.filter_by(name = name).first()
    if pet_stage == None:
        pet_stage = PetStage(name = name, original_pet = original_pet, level_require = level_require, picture = picture)
    else:
        pet_stage.original_pet = original_pet
        pet_stage.level_require = level_require
        pet_stage.picture = picture
    db.session.add(pet_stage)

    for nature_name in natures:
        nature = Nature.query.filter_by(name = nature_name).first()
        if nature == None:
            add_nature(name = nature_name)
            nature = Nature.query.filter_by(name = nature_name).first()
        nature.pet_stages.append(pet_stage)

    db.session.commit()


def add_nature(name):
    nature = Nature.query.filter_by(name = name).first()
    if nature == None:
        nature = Nature(name = name)
        db.session.add(nature)
        db.session.commit()


def get_original_pets():
    original_pets = OriginalPet.query.all()
    return original_pets


def get_natures():
    natures = Nature.query.all()
    return [nature.name for nature in natures]


def get_original_pets_by_nature(nature = None):
    if nature == None:
        return []

    nature_name = nature
    nature = Nature.query.filter_by(name = nature_name).first()
    if nature == None:
        return []

    return nature.original_pets.all()


def get_pets_by_openid(openid):
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return []
    pets = user.pets.all()
    return [{'id' : pet.id,
             'picture' : pet.original_pet.pet_stages.all()[pet.stage].picture,
             'name': pet.original_pet.pet_stages.all()[pet.stage].name,
             'level': pet.level}
              for pet in pets]


def get_pet_by_openid_and_petid(openid, petid):
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return None
    return user.pets.filter_by(id = petid).first()


def get_exp_by_lv(lv):
    level = Level.query.filter_by(id = lv).first()
    if level == None:
        return None
    return level.exp


def try_get_pet(openid):
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return -1, -1
    user.free_flag = False
    db.session.add(user)

    while True:
        original_pet = random.choice(OriginalPet.query.all())
        if original_pet.amount > 0:
            break

    if user.pets.filter_by(original_pet = original_pet).first() != None:
        return original_pet.id, -1

    original_pet.amount = original_pet.amount - 1
    db.session.add(original_pet)
    db.session.commit()
    add_pet(openid = openid, original_pet_id = original_pet.id, name = original_pet.name)
    return original_pet.id, user.pets.all()[-1].id
