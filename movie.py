class Movie: 
    def __init__(self, title: str, duration: float):
        self.title = title
        self.duration = duration

    def play(self) -> str:
        return 'You play the movie ' + self.title + ' for ' + str(self.duration) + ' minutes!'
