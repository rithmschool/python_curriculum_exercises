class Cuisine(object):

    def __init__(self, name, taste_level, spicy_level):
        self.name = name
        self.taste_level = taste_level
        self.spicy_level = spicy_level

    def describe(self):
        raise NotImplementedError("Subclass must implement this method")


class FrenchCuisine(Cuisine):
    def __init__(self,name, taste_level, spicy_level):
        super().__init__(name, taste_level, spicy_level)

    def describe(self):
        return "The finest of cuisine in the world"

