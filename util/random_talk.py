import random


class RandomTalk:
    def __init__(self):
        self.nums = '0123456789'
        self.chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def randomName(self, length):
        random_name = []
        for i in range(length):
            random_name.append(random.choice(self.chars))
        return "".join(random_name)

    def randomAge(self, length):
        random_age = []
        for i in range(length):
            random_age.append(random.choice(self.nums))
        return int("".join(random_age))

    def randomWords(self, length):
        random_age = []
        for i in range(length):
            random_age.append(random.choice(self.nums + self.chars))
        return "".join(random_age)

    def randomCode(self, length):
        random_code = []
        for i in range(length):
            random_code.append(random.choice(self.nums))
        return "".join(random_code)

    def randomHash(self, length):
        random_hash = []
        for i in range(length):
            random_hash.append(random.choice(self.nums + self.chars))
        return "".join(random_hash)
