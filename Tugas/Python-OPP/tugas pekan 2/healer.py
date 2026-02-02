from hero import Hero

class Healer(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, job="Healer")

    def skill1(self, ally):
        heal_amount = 75
        # Menambahkan info target heal di print agar lebih jelas
        print(f"💚 {self.name} menggunakan Skill 1: Holy Healing ke {ally.name}!")
        
        # PERBAIKAN DI SINI: ganti self menjadi ally
        ally.healer(heal_amount)

    def skill2(self, ally):
        heal_amount = 80
        print(f"💚 {self.name} menggunakan Skill 2: Love Waves ke {ally.name}!")
        
        # PERBAIKAN DI SINI
        ally.healer(heal_amount)

    def ultimate(self, ally):
        heal_amount = 55
        print(f"💚 {self.name} menggunakan Ultimate: Blessing of Moon Goddess ke {ally.name}!")
        
        # PERBAIKAN DI SINI (3x heal ke ally)
        ally.healer(heal_amount)
        ally.healer(heal_amount)