from hero import Hero

class Mage(Hero):
    def __init__(self, name, hp):
        # super() = mengekses parent class (Hero)
       super().__init__(name, hp, job="Mage")

    def skill1(self, enemy):
        dmg = 80
        print(f"⚔️ {self.name} menggunakan Skill 1: Fire Arrow!")
        print(f"dengan damage {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)

    def skill2(self, enemy):
        dmg = 85
        print(f"⚔️ {self.name} menggunakan Skill 2: Meteor Shower!")
        print(f"dengan damage {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)

    # method baru khusus mage aja
    def ultimate(self, enemy):
        dmg = 50
        print(f"⚔️ {self.name} menggunakan Ultimate: Bats Feast {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)