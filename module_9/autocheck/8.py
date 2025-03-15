from collections import UserDict


class LookUpKeyDict(UserDict):
    keys = []
    def lookup_key(self, value):
        keys = [key for key, val in self.data.items() if val == value]
        return keys
