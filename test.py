import json
jobs = json.load(open('Data/Jobs.json'))
chara = json.load(open('Data/Characters.json'))
from FeUnit.Fe_Class import Job
from FeUnit.Unit import Unit
from FeUnit.Personal import Personal
from Inventory import Inventory
x = Job(*jobs['Lord'])
y = Personal(*chara["Chrom"])
Chrom = Unit(y, x, [0,0,0,0,0,0,0,0], Inventory(5), 20, [])
x = Job(*jobs['Fighter'])
y = Personal(*chara["Vaike"])
Vaike = Unit(y, x, [0,0,0,0,0,0,0,0], Inventory(5), 20, [])
x = Job(*jobs['Cavalier'])
y = Personal(*chara["Stahl"])
Stahl = Unit(y, x, [0,0,0,0,0,0,0,0], Inventory(5), 20, [])
import pickle
from Army import Army
from IF_ItemsEquipment import *
x = json.load(open('Data/Weapons.json','r'))
Chrom.inventory.put(Sword(*x["Bronze Sword"]))
Chrom.equip(0)
Vaike.inventory.put(Axe(*x["Bronze Axe"]))
Vaike.equip(0)
Stahl.inventory.put(Lance(*x["Bronze Lance"]))
Stahl.equip(0)
Vaike.personal.movement = 5
save = Army([Chrom], 'Natsume', Inventory(-1))

#pickle.dump(save, open('first_army.pckl','w'))
#save = Army([Vaike, Stahl], 'Natsume', Inventory(-1))
#pickle.dump(save, open('second_army.pckl','w'))

pickle.dump(save, open('second_army.pckl','w'))
save = Army([Vaike, Stahl], 'Natsume', Inventory(-1))
pickle.dump(save, open('first_army.pckl','w'))
