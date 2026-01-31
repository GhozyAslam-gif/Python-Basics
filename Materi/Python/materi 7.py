print("MATER 7C - PYTHON DATA STURUCTURE")
print("----------------------------------")
# Set -> { } -> tidak berurutan, berubah, tidak boleh duplikat
game_ridho = {"genshin", "mlbb", "delta force"}
game_imam = {"valorant", "point blank", "genshin"}
print("Game ridho =>", game_ridho)
print("Game imam =>", game_imam)
# .add
game_imam.add("valorant") # jika ada akan di skip
game_imam.add("mlbb")
# .remove() -> menghapus dari set
game_ridho.remove("mlbb")
# len() -> menghitung jumlah item
print("Ridho ada", len(game_ridho), " =>", game_ridho)
print("Imam ada", len(game_imam), " =>", game_imam)
# .union() menggabungkan 2 set berbeda
game_gabungan = game_imam.union(game_ridho)
total_game = len(game_gabungan)
print("Game Gabungan ", total_game , "=>", game_gabungan)
# .intersection() mencari item yg kembar dari 2 set berbeda
# .disfference() mencari item yg beda dari 2 set berbeda
game_kembar = game_ridho.intersection(game_imam)
game_beda = game_ridho.difference(game_imam)
print("Game Kembar:", game_kembar)
print("Game Berbeda:", game_beda)

# Dict (dictionary) -> {key:value} / {kunci:isinya}
# berurutan berdasarkan key, berubah, key tidak duplikat
print("--------------------DICT----------------------")
daftar_anime = {
    "jujutsu_kaisen": "gojo satoru",
    "one_punch_man": "saitama",
    "jigoku_raku": "sagiri",
    "naruto": "shikamaru",
    "waifu": {
        "demon_slayer": "mitsuri",
        "spy_x_family": "anya",
        "naruto": "tsunade,"
    }
}
print("Daftar anime:", daftar_anime)
print("MC ONE PUNCH MAN:", daftar_anime["one_punch_man"])
print("Waifu loli: ", daftar_anime["waifu"]["spy_x_family"])
# menambah atau mengubah item value berdasarkan key
daftar_anime["one_punch_man"] = "genos"
daftar_anime["waifu"]["demon_slayer"] = "nezuko"
print("MC ONE PUNCH MAN BARU:", daftar_anime["one_punch_man"])
print("Waifu loli tapi gede: ", daftar_anime["waifu"]["demon_slayer"])
# menambah item value berdasarkan key
daftar_anime["wind_breaker"] = "sakura"
print("MC wind breaker:", daftar_anime['wind_breaker'])