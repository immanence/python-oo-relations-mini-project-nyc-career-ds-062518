from invite import Invite
from review import Review

class Guest:

    _all = []

    def __init__(self, name):
        self._name = name
        Guest._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def most_popular(cls):
        dict= {}
        dict = dict.fromkeys(Guest._all, 0)
        for invite in Invite._all:
            dict[invite._guest] += 1
        return max(dict.items(), key = lambda item: item[1])[0]

    @classmethod
    def toughest_critic(cls):
        dict = {}
        dict = dict.fromkeys(Guest._all, [])
        for review in Review._all:
            dict[review._guest].append(review._rating)
        return min(dict.items(), key = lambda item: sum(item[1])/len(item[1]))[0]

    @classmethod
    def most_active_critic(cls):
        dict = {}
        dict = dict.fromkeys(Guest._all, 0)
        for review in Review._all:
            dict[review._guest] += 1
        return max(dict.items(), key = lambda item: item[1])[0]

    def invites(self):
        return [invite for invite in Invite._all if invite._guest == self]

    def reviews(self):
        return [review for review in Review._all if review._guest == self]

    def number_of_invites(self):
        return len(self.invites())

    def rsvp(self, invite, rsvp_status):
        invite.accepted = rsvp_status
        return invite.accepted

    def review_recipe(self, recipe, rating, comment):
        Review(self, recipe, rating, comment)
        return [review for review in Review._all if review._recipe == recipe]

    def favorite_recipe(self):
        l = [review for review in Review._all if review._guest == self]
        return max(l, key = lambda review: review._rating)._recipe
