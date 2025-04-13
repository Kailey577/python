
class Cat:
    def __init__(self):
        #state
        self._favoriteFood = None
    def setFavoriteFood(self, theFavorite):
        self._favoriteFood = theFavorite
    def getFavoriteFood(self):
        return self._favoriteFood


def main():
    tucker = Cat()
    tucker.setFavoriteFood("fish")
    tucker_alias = tucker #alias is not a copy
    tucker_alias.setFavoriteFood("apples")
    print(tucker.getFavoriteFood())

    phoeobe = Cat()

    s = "cat"
    s1 = s #s1 is a copy of s. it doesnt point to s.
    s1 = "dog"
    print(s)

main()