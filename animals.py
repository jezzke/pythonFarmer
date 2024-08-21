class Zvire:
    def __init__(
            self, 
            jmeno: str, 
            strava: list, 
            output: list, 
            death_reward: list):
        self.jmeno = jmeno
        self.strava = strava
        self.output = output
        self.death_reward = death_reward

        self.hunger = 0
        self.thirst = 0
        
        self.is_alive = True

class Krava(Zvire):
    def __init__(self, jmeno: str):
        super().__init__
        (jmeno, 
         ["tráva"], 
         [["mléko", 5]], 
         [["kůže", 20], ["maso", 20]])
