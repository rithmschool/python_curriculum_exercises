# Classes

### Part 1

Answer the following questions

- What is a class?
- What is an instance?
- What is inheritance?
- What is multiple inheritance?
- What is polymorphism?

### Part 2

- Inheritance (Multiple)
- Class methods
- Instance methods

**Cuisine**
**Restaurant**
**FoodTruck**

Each cuisine should have a `name`, `taste_level`, `spicy_level`, `most_common_dish`

Each cusine instance should have a method called `describe`, which should be implemented by it's subclasses

Each restaurant can inherit from multiple cuisines.

### Bonus

Refactor your file-io example into a class called `FileManipulator`. This class should implement a method called `addLine` and `printLines`, which should be implemented in the two classes that inherit from it using Polymorphism. These classes should be called `CSVManipulator` and `TextManipulator` and both should be able to add and read to files.