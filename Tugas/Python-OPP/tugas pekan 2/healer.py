from hero import Hero

class Healer(Hero):
    def __init__(self, name, hp):
        # super() = mengekses parent class (Hero)
       super().__init__(name, hp, job="Healer")

    def skill1(self, enemy):
        heal_amount = 75
        print(f"💚 {self.name} menggunakan Skill 1: Holy Healing!")
        print(f"dengan heal {heal_amount}")
        # monster terkena damage
        self.heal()

    def skill2(self, enemy):
        heal_amount = 50
        print(f"💚 {self.name} menggunakan Skill 2: Love Waves!")
        print(f"dengan heal {heal_amount}")
        # monster terkena damage
        self.heal()

    # method baru khusus healer aja
    def ultimate(self, enemy):
        heal_amount = 85
        print(f"💚 {self.name} menggunakan Ultimate: Blessing of Moon Goddess {heal_amount}")
        # monster terkena damage
        self.heal()
        self.heal()
        self.heal()