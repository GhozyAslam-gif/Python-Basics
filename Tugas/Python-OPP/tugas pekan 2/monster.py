class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.rage_mode = False
        print(f"💀 Monster [{self.name}] telah di summon!")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

        print(f"💥 {self.name} terkena {damage} damage")
        print(f"❤️ Sisa HP: {self.hp}")

        if self.hp <= self.max_hp / 2 and not self.rage_mode:
            self.rage_mode = True
            print(f"😈 {self.name} memasuki RAGE MODE!")
            print("⚡ Serangan menjadi lebih kuat (CRITICAL HIT)")

        if self.hp == 0:
            print(f"💀 {self.name} tereliminasi dari arena!")

    def heal(self):
        heal_amount = 20
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print(f"🧪 {self.name} meminum potion...")
        print(f"💚 HP bertambah +{heal_amount}")
        print(f"❤️ HP sekarang: {self.hp}")

    def attack(self, enemy, damage):
        print(f"⚔️ {self.name} menyerang {enemy.name}!")

        if self.rage_mode:
            damage *= 2
            print("💢 CRITICAL HIT!")

        enemy.take_damage(damage)

    def ultimate(self, enemy):
        dmg = 93
        print(f"🔥 {self.name} Ultimate : 'Cauterant Inferno'!")

        if self.rage_mode:
            dmg *= 2
            print("💥 RAGE ULTIMATE!")

        enemy.take_damage(dmg)

    def __str__(self):
        status = "💚 Hidup"
        if self.hp == 0:
            status = "💀 Mati"
        return f"Monster {self.name} | HP: {self.hp}/{self.max_hp} | {status}"
