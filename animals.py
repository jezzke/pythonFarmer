class Zvire:

    instance = []
    count = 0

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
        self.max = 20
        
        self.is_alive = True

        Zvire.zvirata.append(self)
        Zvire.count += 1

        self.id = Zvire.count

        Zvire.info(self, "Objekt typu", "byl úspěšně vytvořen:")


    def info(self, text, text2):
        print(f"""\
{text} {self.__class__.__name__} {text2}:
    jméno: {self.jmeno}
    strava: {" ,".join(self.strava)}
    id: {self.id}""")


class Krava(Zvire):
    def __init__(self, jmeno: str):
        super().__init__(
        jmeno, 
        ["tráva"], 
        [["mléko", 5]], 
        [["kůže", 20], ["maso", 20]])




Krava("bob")
