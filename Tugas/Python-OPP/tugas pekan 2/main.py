from monster import Monster
from warrior import Warrior
from mage import Mage
from healer import Healer

print("== SUMMON SEMUA HERO ==")
alucard = Warrior("Alucard", 150)
eudora = Mage("Eudora", 100)
angela = Healer("Angela", 100)

print("\n== SUMMON BOSS ==")
dragon = Monster("Dragon King", 1000)
goblin = Monster("Goblin", 95)

print("\n== RAID DIMULAI! ==")
alucard.ultimate(dragon)
eudora.skill1(dragon)
dragon.take_damage(100)
angela.skill1(alucard)


eudora.ultimate(dragon)
dragon.attack(alucard, 50)
dragon.ultimate(angela)

print("\n== CEK STATUS ==")
print(alucard)
print(eudora)
print(angela)

