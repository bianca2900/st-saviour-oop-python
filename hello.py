#imports information from all classes
from movie import Movie
from zombie_horror import ZombieHorror
from romantic_comedy import RomanticComedy

if __name__ == '__main__':  #if true the code will run

    twenty_eight_days_later = ZombieHorror('28 Days Later', 2.5, 28) #tells the code the conditions of this specific movie
    print(twenty_eight_days_later.create_suspense()) #this will print the suspensful part of the movie

    assert isinstance(twenty_eight_days_later, Movie) #checks to see if the condition is true

    print(str(twenty_eight_days_later)) #if it is true print the title
    
    how_to_lose_a_guy_in_ten_days= RomanticComedy('How To Lose A Guy in 10 Days', 2.5, 28) #tells the code the conditions of this specific movie
    
    print(how_to_lose_a_guy_in_ten_days.laugh()) #this will print the parts of the movie that have laughs

    assert isinstance(how_to_lose_a_guy_in_ten_days, Movie) #checks to see if the condition is true

    print(str(how_to_lose_a_guy_in_ten_days)) #if it is true print the title
