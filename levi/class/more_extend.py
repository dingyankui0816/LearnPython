class AnimalA(object):
    @property
    def run(self):
        print('Animal A running...')

class AnimalB(object):
    @property
    def run(self):
        print('Animal B running...')

class AB(AnimalA,AnimalB):
    @property
    def run(self):
        print('Animal AB running...')
    pass

ab = AB()
ab.run