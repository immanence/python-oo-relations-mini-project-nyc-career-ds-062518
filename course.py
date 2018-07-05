class Course:

    _all = []

    def __init__(self, dinner_party, recipe):
        self._dinner_party = dinner_party
        self._recipe = recipe
        Course._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def dinner_party(self):
        return self._dinner_party

    def recipe(self):
        return self._recipe
