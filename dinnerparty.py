from invite import Invite
from course import Course
from recipe import Recipe
from review import Review
from guest import Guest

class DinnerParty:

    _all = []

    def __init__(self, name):
        DinnerParty._all.append(self)
        self._name = name

    @classmethod
    def all(cls):
        return cls._all

    def invites(self):
        return [invite for invite in Invite._all if invite._dinner_party == self]

    def guests(self):
        return [invite._guest for invite in Invite._all if invite._dinner_party == self]

    def number_of_attendees(self):
        return len([invite for invite in Invite._all if invite._dinner_party == self and invite.accepted == True])

    def courses(self):
        return [course for course in Course._all if course._dinner_party == self]

    def recipes(self):
        return [course._recipe for course in self.courses()]

    def recipe_count(self):
         return len(self.recipes())

    def reviews(self):
        l = []
        for recipe in self.recipes():
            l += [review for review in Review._all if review._recipe == recipe]
        return l

    def highest_rated_recipe(self):
        avgs = {}
        for recipe in self.recipes():
            reciperatings = []
            for review in self.reviews():
                reciperatings.append(review._rating)
            avgs.update({recipe: sum(reciperatings)/len(reciperatings)})
        return max(avgs.items(), key = lambda item: item[1])[0]
