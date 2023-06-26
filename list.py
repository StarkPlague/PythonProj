badang = Hero("Jungler02", "Badang", 499, 32000, 0, "Physical", 5000)
badang.info_hero
badang_role = Role()
badang_role.add_hero("Badang", "Jungler01", "Jungler", "Physical")
Akun_Func = Akun()
Akun_Func.add_role("Jungler02", "Jungler")
Akun_Func.search_hero("Badang", "Jungler01", "Jungler", "Physical")
print(Role_Akun)


badang = Hero("Jungler02", "Badang", 499, 32000, 0, "Physical", 5000)
thamuz = Hero("Jungler02", "Thamuz", 499, 32000, 0, "Physical", 5000)
badang.info_hero
badang_role = Role()
badang_role.add_hero("Badang", "Jungler01", "Jungler", "Physical")
badang_role.list_hero()
badang_role.search_hero("Badang")
