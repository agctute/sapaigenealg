import sapai.player as pl
from sapai.shop import Shop
from sapai.teams import Team

testShop = Shop(pack="StandardPack", seed_state=None)
testTeam = Team(seed_state=None)
test = pl.Player(testShop, testTeam)

print(test)
