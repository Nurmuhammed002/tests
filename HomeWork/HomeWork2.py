class SuperHero:
    def __init__(self, name, health_points):
        self.name = name
        self.health_points = health_points

    def power_up(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_phrase(self):
        print(f"True in the {self.__class__.__name__}")

class AirHero(SuperHero):
    def __init__(self, name, health_points, damage):
        super().__init__(name, health_points)
        self.damage = damage
        self.fly = False

class EarthHero(SuperHero):
    def __init__(self, name, health_points, damage):
        super().__init__(name, health_points)
        self.damage = damage
        self.fly = False

class Villain(SuperHero):
    def __init__(self, name, health_points, damage):
        super().__init__(name, health_points)
        self.damage = damage
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self):
        return self.damage ** 2

if __name__ == "__main__":
    air_hero = AirHero("Air Man", 100, 20)
    earth_hero = EarthHero("Earth Woman", 150, 30)

    air_hero.power_up()
    earth_hero.power_up()

    air_hero.true_phrase()
    earth_hero.true_phrase()

    villain = Villain("Dark Lord", 200, 50)

    hero_damage = 25
    crit_damage = villain.crit(hero_damage)
    print(f"Crit damage dealt: {crit_damage}")
