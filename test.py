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
import pickle
from Army import Army
from IF_ItemsEquipment import Sword
x = json.load(open('Weapons.json','r'))
Chrom.inventory.put(Sword(*x["Bronze Sword"]))
save = Army([Chrom], 'Natsume', Inventory(-1))
pickle.dump(save, open('first_army.pckl','w'))
