class Zvire:
    def __init__(self, jmeno: str, strava: list, output, death_reward):
        self.jmeno = jmeno
        self.strava = strava
        self.output = output
        self.death_reward = death_reward
        
        self.is_alive = True

class Krava(Zvire):
    def __init__(self, jmeno: str):
        super().__init__(jmeno, ["tráva"], [["mléko", 5]], [["kůže", 20], ["maso", 20]])