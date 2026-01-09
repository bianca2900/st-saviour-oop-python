from romantic_comedy import Comedy
def __init__(self, title: str, duration: float, laughs: str):
        super().__init__(title, duration, laughs)
        self.laughs = laughs

        def self_laugh(self) -> str
            laughs -= 1
            if laughs > 0:
                if laughs >= 10 and laughs < 20:
                    return 'The movie ' + self.title + ' is making me loneley'
                if laughs >= 20 and laughs < 30:
                    return 'The movie ' + self.title +  'is calling me loneley in every way possible'
                if laughs > 30:
                    return  self.title + 'is so cringy' 
                
            def __str__(self) -> str:
             return f'title: {self.title}, duration: {self.duration}, laughs: {self.laughs}'