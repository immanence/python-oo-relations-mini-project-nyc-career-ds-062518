class Invite:

    _all = []

    def __init__(self, dinner_party, guest):
        self._guest = guest
        self._dinner_party = dinner_party
        Invite._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def dinner_party(self):
        return self._dinner_party

    @dinner_party.setter
    def dinner_party(self, dinner_party):
        self._dinner_party = dinner_party

    def accepted(self):
        return self.accepted

    def guest(self):
        return self._guest

    # def dinner_party(self):
    #     return self._dinner_party
