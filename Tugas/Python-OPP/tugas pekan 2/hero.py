class Hero:
    # pertama kali dipanggil (summon)
    # self = dirinya sendiri / internal
    def __init__(self, name, hp, job):
        self.name = name
        self.job = job
        self.hp = hp
        print(f"✨ [{self.job}] Hero {self.name} telah di summon!")

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
        return f"[{self.job}] {self.name} | HP: {self.hp} | {status}"

    # skill ultimate (dasar)
    def ultimate(self, enemy):
        dmg = 100
        print(f"🔥 {self.name} Ultimate : 'Abysm Strike' !")
        enemy.take_damage(dmg)