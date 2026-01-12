class Movie: #creates the parent class
    def __init__(self, title: str, duration: float): #tells the other classes what to have 
        self.title = title #something all movies have
        self.duration = duration #something all movies have

    def play(self) -> str: #creates something that all movies can do
        return 'You play the movie ' + self.title + ' for ' + str(self.duration) + ' minutes!' #allows the function to run 
