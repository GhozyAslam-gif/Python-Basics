class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print(f"✨ Monster {self.name} telah di summon!")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"💥 {self.name} terkena {damage} damage\n")
        print(f"❤️ Sisa HP: {self.hp}")
        if self.hp == 0:
            print(f"💀 {self.name} tereliminasi dari arena!")

    def heal(self):
        print(f"🧪 {self.name} meminum potion...")
        heal_amount = 20
        self.hp += heal_amount
        print(f"💚 HP {self.name} bertambah +{heal_amount}")

    def take_damage(self, damage):
        # self.hp = self.hp - damage (aslinya)
        self.hp -= damage
        print(f"💥 {self.name} terkena {damage} damage\n")
        print(f"❤️ Sisa HP: {self.hp}")
        if self.hp <= 0:
            print(f"💀 {self.name} tereliminasi dari arena!")

    def attack(self, enemy, damage):
        print(f"⚔️ {self.name} menyerang {enemy.name}!")
        # panggil method lain dari dalam
        enemy.take_damage(damage)

    # fungsi cek status terkini
    def __str__(self):
        status = "💚 Hidup"
        if self.hp == 0:
            status = "💀 Mati"
        return f"Monster {self.name} | HP: {self.hp} | {status}"


    # skill ultimate (dasar)
    def ultimate(self, enemy):
        print(f"🔥 {self.name} bengong!")