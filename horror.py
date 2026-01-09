from movie import Movie

class Horror(Movie): 
    def __init__(self, title: str, duration: float):
        super().__init__(title, duration)
        self.suspense = 0

    def create_suspense(self) -> str:
        self.suspense += 10
        if self.suspense >= 10 and self.suspense < 20:
            return 'The movie ' + self.title + ' is starting to get spooky ...'
        if self.suspense >= 20 and self.suspense < 30:
            return 'The movie ' + self.title +  ' is high-key scary ...'
        if self.suspense > 30:
            return 'You got jumpscared watching ' + self.title + ' ... boo!' 
    
    

