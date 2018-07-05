from review import Review

class Recipe:

    _all = []

    def __init__(self, name):
        self._name = name
        Recipe._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def recipe_reviews(cls):
        dict = {recipe: [review._rating for review in recipe.reviews()] for recipe in cls._all}
        for recipe in list(dict.keys()):
            if dict[recipe] == []:
                del dict[recipe]
        tuples = sorted(dict.items(), key = lambda item: sum(item[1])/len(item[1]))
        return [recipe[0] for recipe in tuples]

    @classmethod
    def top_three(cls):
        return cls.recipe_reviews()[-1:-4:-1]

    @classmethod
    def bottom_three(cls):
        return cls.recipe_reviews()[:3]

    def reviews(self):
        return [review for review in Review._all if review._recipe == self]

    def top_five_reviews(self):
        return sorted(self.reviews(), key = lambda review: review._rating, reverse = True)[:5]
