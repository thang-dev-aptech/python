def normalize_name(name):
    name = name.strip().title().split()
    return " ".join(name)

name = normalize_name("   nGuYEn   van   a  ")
print(name)

print(normalize_name("       Thang       nguyen  Doan"))


