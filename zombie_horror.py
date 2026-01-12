from horror import Horror #imports content from the horror class

class ZombieHorror(Horror): #imports content from the horror class 
    def __init__(self, title: str, duration: float, scares: str): #defines what is in the classes
        super().__init__(title, duration) #helps call things from the parent function
        self.scares = scares 

    def to_scare(self) -> str: #calls things from the this class
        scares -= 1
        if scares > 0: #there will be more than zero scares
            if scares >= 10 and scares < 20:
                return 'The movie ' + self.title + ' giving me nightmares' #if it meets the above requirement then return this
            if scares >= 20 and scares < 30:
                return 'The movie ' + self.title +  'is making me not sleep' #if it meets the above requirement then return this
            if scares > 30:
                return  self.title + 'is making me hide behind my blanket' #if it meets the above requirement then return this
    #helps define the movies components 
    def __str__(self) -> str: 
        return f'title: {self.title}, duration: {self.duration}, scares: {self.scares}'