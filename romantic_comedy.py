from comedy import Comedy #imports things from the Comedy class

class RomanticComedy(Comedy): #calls things from the comedy class
    def __init__(self, title: str, duration: float, laughs: str): #defines whats in the classes
        super().__init__(title, duration, laughs) #helps call things from the parent function
        self.laughs = laughs

    def laugh(self) -> str: #calls things from this class
        self.laughs -= 1
        if self.laughs > 0: #there will more than zero laughs
            if self.laughs >= 10 and self.laughs < 20:
                return 'The movie ' + self.title + ' is making me lonely' #if it meets the above requirement then return this
            if self.laughs >= 20 and self.laughs < 30:
                return 'The movie ' + self.title +  ' is calling me lonely in every way possible' #if it meets the above requirement then return this
            if self.laughs > 30:
                return  self.title + ' is so cringy'  #if it meets the above requirement then return this
    #helps define the movies components      
    def __str__(self) -> str:
        return f'title: {self.title}, duration: {self.duration}, laughs: {self.laughs}'