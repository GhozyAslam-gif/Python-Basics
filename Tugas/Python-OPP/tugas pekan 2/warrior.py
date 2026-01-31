from hero import Hero

class Warrior(Hero):
    def __init__(self, name, hp):
        # super() = mengekses parent class (Hero)
       super().__init__(name, hp, job="Warrior")

    def skill1(self, enemy):
        dmg = 100
        print(f"⚔️ {self.name} menggunakan Skill 1: Gigantic Slash!")
        print(f"dengan damage {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)

    def skill2(self, enemy):
        dmg = 85
        print(f"⚔️ {self.name} menggunakan Skill 2: ")
        print(f"dengan damage {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)

    # method baru khusus mage aja
    def ultimate(self, enemy):
        dmg = 20
        print(f"⚔️ {self.name} menggunakan Ultimate: WATER CANON x3 {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)