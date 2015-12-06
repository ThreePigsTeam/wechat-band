import urllib

for i in range(100, 721):
    urllib.urlretrieve("http://assets22.pokemon.com/assets/cms2/img/pokedex/full/%.3d.png" % i, "%.3d.png" % i)