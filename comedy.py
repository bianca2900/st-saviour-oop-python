from horror import Movie #imports content from the movie class

class Comedy(Movie): #imports content from the movie class
    def __init__(self, title: str, duration: float, jokes: int): #defines what is in the classes
        super().__init__(title, duration) #helps call things from the parent function 
        self.jokes = jokes

    def play_scene(self) -> str: #self helps access specific things 
        jokes -= 1
        if jokes > 0: #there will be more than zero jokes
            if jokes >= 10 and jokes < 20:
                return 'The movie ' + self.title + ' is really funny' #if it meets the above requirement then return this
            if jokes >= 20 and jokes < 30:
                return 'The movie ' + self.title +  ' is high-key making me laugh.' #if it meets the above requirement then return this
            if jokes > 30:
                return 'The movie'+ self.title + 'just made my day!' #if it meets the above requirement then return this