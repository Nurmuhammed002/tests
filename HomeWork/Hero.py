class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def display_name(self):
        print(f"Hero's name: {self.name}")

    def multiply_health(self):
        self.health_points *= 2
        print(f"Health points after multiplication: {self.health_points}")

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health Points: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Clark Kent", "Superman", "Super Strength", 100, "Up, up and away!")
hero.display_name()
hero.multiply_health()
print(hero)
print(f"Length of catchphrase: {len(hero)}")

