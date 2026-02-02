from hero import Hero

class Warrior(Hero):
    def __init__(self, name, hp):
        # super() = mengekses parent class (Hero)
       super().__init__(name, hp, job="Warrior")

    def skill1(self, enemy):
        dmg = 45
        print(f"⚔️ {self.name} menggunakan Skill 1: Gigantic Slash!")
        print(f"dengan damage {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)

    def skill2(self, enemy):
        dmg = 55
        print(f"⚔️ {self.name} menggunakan Skill 2: Whirling Smash!")
        print(f"dengan damage {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)

    # method baru khusus mage aja
    def ultimate(self, enemy):
        dmg = 75
        print(f"⚔️ {self.name} menggunakan Ultimate: Lethal Counter!")
        print(f"dengan damage {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)