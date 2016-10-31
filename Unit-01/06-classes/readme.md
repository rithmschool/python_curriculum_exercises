# Classes

### Part 1

Answer the following questions

- What is a class?
- What is an instance?
- What is inheritance?
- What is multiple inheritance?
- What is polymorphism?
- What is `method resolution order` or `MRO`?

### Part 2

Each cuisine instance should have a `name`, `taste_level`, `spicy_level`, `most_common_dish`

Each cuisine instance should have a method called `describe`, which should be implemented by it's subclasses using polymorphsim. Also note that each restaurant can inherit from multiple cuisines.

Each restaurant instance should have a `name`, `location`, `rating` (which should be a number from 1 to 5).

Each restaurant instance should have a method called `display_base_class` which lists the classes that it inherited from. You can read more about how to figure this out [here](http://stackoverflow.com/questions/1401661/python-list-all-base-classes-in-a-hierarchy-of-given-class)

### Bonus

Refactor your file-io example into a class called `FileManipulator`. This class should implement a method called `addLine` and `printLines`, which should be implemented in the two classes that inherit from it using Polymorphism. These classes should be called `CSVManipulator` and `TextManipulator` and both should be able to add and read to files.