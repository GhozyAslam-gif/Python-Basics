from hero import Hero

class Mage(Hero):
    def __init__(self, name, hp):
        # super() = mengekses parent class (Hero)
       super().__init__(name, hp, job="Mage")

    def ultimate(self, enemy):
        dmg = 85
        print(f"⚔️ {self.name} menggunakan Skill 1: Fire Arrow!")
        print(f"dengan damage {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)

    # method baru khusus mage aja
    def combo(self, enemy):
        dmg = 20
        print(f"⚔️ {self.name} menggunakan Skill combo: WATER CANON x3 {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)