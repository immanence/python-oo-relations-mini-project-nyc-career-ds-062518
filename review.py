class Review:

    _all = []

    def __init__(self, guest, recipe, rating, comment = None):
        self._guest = guest
        self._recipe = recipe
        self._rating = rating
        self._comment = comment
        Review._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    @property
    def recipe(self):
        return self._recipe

    @recipe.setter
    def recipe(self, recipe):
        self._recipe = recipe

    @property
    def reviewer(self):
        return self._guest

    @reviewer.setter
    def reviewer(self, guest):
        self._guest = guest

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, comment):
        self._comment = comment
