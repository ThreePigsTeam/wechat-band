import unittest
from flask import current_app
from app import create_app, db
from app.models.User import *
from app.models.Pet import *
from app.models.Step import *
from app.models.Rate import *
from manage import insert_pet_info

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    def test_app_exists(self):
        self.assertFalse(current_app is None)
    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    def test_add_user(self):
        self.assertFalse(exist_user(openid = 'gxd'))
        add_user(openid = 'gxd')
        self.assertTrue(exist_user(openid = 'gxd'))
    def test_del_user(self):
        add_user(openid = 'gxd')
        del_user(openid = 'gxd')
        self.assertFalse(exist_user(openid = 'gxd'))
    def test_set_user(self):
        set_user(openid = 'gxd', goal = 1234)
        self.assertTrue(get_goal_by_openid(openid = 'gxd') == 1234)


class PetTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        insert_pet_info()
        add_user(openid = 'gxd')
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    def test_insert_pet_info(self):
        #insert_pet_info()
        #print Pet.query.all()
        self.assertTrue(OriginalPet.query.all() != [])
        self.assertTrue(PetStage.query.all() != [])
    def test_add_pet(self):
        self.assertTrue(get_pets_by_openid(openid = 'gxd') == [])
        add_pet(openid = 'gxd', original_pet_id = 1)
        self.assertTrue(get_pets_by_openid(openid = 'gxd') != [])


class StepTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        add_user(openid = 'gxd')
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    def test_step(self):
        self.assertTrue(get_steps_by_openid(openid = 'gxd') == [0, 0, 0, 0, 0, 0, 0])
        add_step(openid = 'gxd', data = 10)
        self.assertTrue(get_steps_by_openid(openid = 'gxd') == [0, 0, 0, 0, 0, 0, 10])


class RateTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        add_user(openid = 'gxd')
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    def test_rate(self):
        self.assertTrue(get_steps_by_openid(openid = 'gxd') == [0, 0, 0, 0, 0, 0, 0])
        add_step(openid = 'gxd', data = 10)
        self.assertTrue(get_steps_by_openid(openid = 'gxd') == [0, 0, 0, 0, 0, 0, 10])