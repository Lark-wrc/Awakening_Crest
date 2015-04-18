import json
jobs = json.load(open('Jobs.json'))
chara = json.load(open('Characters.json'))
from Job import Job
from Unit import Unit
from Personal import Personal
from Statlist import Statlist
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
x = json.load(open('Weapons.json','r'))
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
