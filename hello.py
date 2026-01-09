from movie import Movie
from zombie_horror import ZombieHorror
from romantic_comedy import RomanticComedy

if __name__ == '__main__':
    # print('new dawn, new day')
    twenty_eight_days_later = ZombieHorror('28 Days Later', 2.5, 28)
    print(twenty_eight_days_later.create_suspense())

    assert isinstance(twenty_eight_days_later, Movie)

    print(str(twenty_eight_days_later))

    how_to_lose_a_guy_in_ten_days= RomanticComedy('How To Lose A Guy in 10 Days', 2.5, 28)
    print(twenty_eight_days_later.create_suspense())

    assert isinstance(twenty_eight_days_later, Movie)

    print(str(twenty_eight_days_later))

    print(how_to_lose_a_guy_in_ten_days.laugh())