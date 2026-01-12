from movie import Movie #imports from the movie class

class Horror(Movie): #import from the movie class
    def __init__(self, title: str, duration: float): #defines what is in the classes
        super().__init__(title, duration) #helps call things from the parent function 
        self.suspense = 0 #refrences the function called

    def create_suspense(self) -> str: # self helps access specific things
        self.suspense += 10 #starts the instructions to tell the function what to do.
        if self.suspense >= 10 and self.suspense < 20:
            return 'The movie ' + self.title + ' is starting to get spooky ...' #if it meets the above requirement then return this
        if self.suspense >= 20 and self.suspense < 30:
            return 'The movie ' + self.title +  ' is high-key scary ...' #if it meets the above requirement then return this
        if self.suspense > 30:
            return 'You got jumpscared watching ' + self.title + ' ... boo!' #if it meets the above requirement then return this
    
    

