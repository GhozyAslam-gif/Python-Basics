from hero import Hero

class Warrior(Hero):
    def __init__(self, name, hp):
        # super() = mengekses parent class (Hero)
       super().__init__(name, hp, job="Warrior")

    def ultimate(self, enemy):
        dmg = 100
        print(f"⚔️ {self.name} menggunakan Skill 1: Gigantic Slash!")
        print(f"dengan damage {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)