from monster import Monster
from warrior import Warrior
from mage import Mage
from healer import Healer

print("== SUMMON SEMUA HERO ==\n")
alucard = Warrior("Alucard", 150)
eudora = Mage("Eudora", 120)
angela = Healer("Angela", 100)

print("\n== SUMMON BOSS ==\n")
dragon = Monster("Dragon King", 1000)
goblin = Monster("Goblin", 95)

print("\n== RAID DIMULAI! ==\n")
alucard.attack(goblin, 10)
eudora.attack(goblin, 10)
angela.attack(goblin, 10)
goblin.attack(alucard, 10)
goblin.attack(alucard, 30)
goblin.ultimate(alucard)
alucard.skill1(goblin)
alucard.attack(goblin, 20)
angela.skill2(alucard)
dragon.attack(alucard, 50)
eudora.ultimate(dragon)
alucard.ultimate(dragon)
dragon.ultimate(eudora)
angela.skill1(eudora)
angela.skill2(alucard)
dragon.attack(angela, 50)
eudora.skill2(dragon)
alucard.skill1(dragon)
dragon.ultimate(alucard)
angela.skill1(alucard)
dragon.attack(alucard, 50)
eudora.attack(dragon, 50)
dragon.attack(alucard, 40)
alucard.ultimate(dragon)
angela.skill2(alucard)
dragon.ultimate(alucard)
dragon.attack(alucard, 6)
eudora.ultimate(dragon)
angela.heal(angela, 10)
angela.skill2(eudora)
eudora.skill2(dragon)
dragon.ultimate(eudora)
eudora.ultimate(dragon)
angela.ultimate(eudora)
angela.heal(angela, 10)
angela.attack(dragon, 50)
eudora.skill2(dragon)




print("\n== CEK STATUS ==")
print(alucard)
print(eudora)
print(angela)
print(dragon)
print(goblin)

