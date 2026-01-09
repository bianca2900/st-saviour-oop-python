from comedy import Comedy

class RomanticComedy(Comedy):
    def __init__(self, title: str, duration: float, laughs: str):
        super().__init__(title, duration, laughs)
        self.laughs = laughs

    def laugh(self) -> str:
        self.laughs -= 1
        if self.laughs > 0:
            if self.laughs >= 10 and self.laughs < 20:
                return 'The movie ' + self.title + ' is making me lonely'
            if self.laughs >= 20 and self.laughs < 30:
                return 'The movie ' + self.title +  ' is calling me lonely in every way possible'
            if self.laughs > 30:
                return  self.title + ' is so cringy' 
                
    def __str__(self) -> str:
        return f'title: {self.title}, duration: {self.duration}, laughs: {self.laughs}'