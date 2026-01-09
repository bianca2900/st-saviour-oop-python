from movie import Movie
from zombie_horror import ZombieHorror

if __name__ == '__main__':
    # print('new dawn, new day')
    twnety_eight_days_later = ZombieHorror('28 Days Later', 2.5, 28)
    print(twnety_eight_days_later.create_suspense())

    assert isinstance(twnety_eight_days_later, Movie)

    print(str(twnety_eight_days_later))