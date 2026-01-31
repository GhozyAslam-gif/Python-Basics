class Hero:
    # pertama kali dipanggil (summon)
    # self = dirinya sendiri / internal
    def __init__(self, name, job, hp):
        self.name = name
        self.job = job
        self.hp = hp
        print(f"✨ Hero {self.name} telah di summon!")

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

# buat objek / summon hero-hero ke lobby
zilong = Hero("Zilong", "Warrior", 100)
aurora = Hero("Aurora", "Mage", 100)
zilong.attack(aurora, 30)
print(aurora)
aurora.attack(zilong, 5)
print(zilong)
aurora.attack(zilong, 5)
print(zilong)
aurora.attack(zilong, 5)
print(zilong)
zilong.heal()
print('SKILL 1: CONGKEL BANG')
zilong.attack(aurora, 70)
aurora.heal()

# cek status terkini
print(aurora)
print(zilong)