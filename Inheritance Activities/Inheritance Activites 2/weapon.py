class Weapon:
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")

class Sword(Weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage)
        self.damage_category = damage_category

    def get_stats(self):
        super().get_stats()
        print(f"Damage Type: {self.damage_category}")
        print(f"Crit Damage: {self.damage * 3}")

class Bow(Weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage)
        self.damage_category = damage_category

    def get_stats(self):
        super().get_stats()
        print(f"Damage Type: {self.damage_category}")
        print(f"Crit Damage: {self.damage * 2}")

class Longbow(Bow):
    def __init__(self, name, category, damage, damage_category, bow_range):
        super().__init__(name, category, damage, damage_category)
        self.bow_range = bow_range

    def get_stats(self):
        super().get_stats()
        print(f"Range: {self.bow_range} ft")

class Shortbow(Bow):
    def __init__(self, name, category, damage, damage_category, bow_range):
        super().__init__(name, category, damage, damage_category)
        self.bow_range = bow_range

    def get_stats(self):
        super().get_stats()
        print(f"Range: {self.bow_range} ft")

sword = Sword("Steel Sword", "Sword", 15, "Slashing")
print("Sword Stats:")
sword.get_stats()

print("\n----------------\n")


bow = Bow("Hunting Bow", "Bow", 10, "Piercing")
print("Bow Stats:")
bow.get_stats()

print("\n----------------\n")


longbow = Longbow("Eagle Longbow", "Bow", 12, "Piercing", 150)
print("Longbow Stats:")
longbow.get_stats()

print("\n----------------\n")


shortbow = Shortbow("Quick Shortbow", "Bow", 8, "Piercing", 80)
print("Shortbow Stats:")
shortbow.get_stats()
