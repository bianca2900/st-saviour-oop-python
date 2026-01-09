from horror import Movie

class Comedy(Movie): 
    def __init__(self, title: str, duration: float, jokes: int):
        super().__init__(title, duration)
        self.jokes = jokes

    def play_scene(self) -> str:
        jokes -= 1
        if jokes > 0:
            if jokes >= 10 and jokes < 20:
                return 'The movie ' + self.title + ' is really funny'
            if jokes >= 20 and jokes < 30:
                return 'The movie ' + self.title +  ' is high-key making me laugh.'
            if jokes > 30:
                return 'The movie'+ self.title + 'just made my day!' 