from horror import Horror

class ZombieHorror(Horror):
    def __init__(self, title: str, duration: float, scares: str):
        super().__init__(title, duration)
        self.scares = scares

    def to_scare(self) -> str:
        scares -= 1
        if scares > 0:
            if scares >= 10 and scares < 20:
                return 'The movie ' + self.title + ' giving me nightmares'
            if scares >= 20 and scares < 30:
                return 'The movie ' + self.title +  'is making me not sleep'
            if scares > 30:
                return  self.title + 'is making me hide behind my blanket' 
            
    def __str__(self) -> str:
        return f'title: {self.title}, duration: {self.duration}, scares: {self.scares}'