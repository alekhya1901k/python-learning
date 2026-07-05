# 3. Constructing Objects and Accessing Attributes and Methods

## Quick Summary Notes

- Objects are created using classes.
- Parentheses construct an object.
- Attributes store object data.
- Methods perform object actions.
- Dot notation accesses attributes.
- Dot notation calls methods.
- Attributes behave like variables.
- Methods behave like functions.
- Objects exist in memory.
- Documentation helps discover available attributes and methods.

---

## Object Construction

```
from turtle import Turtle

timmy = Turtle()
```

### Explanation

| Term | Meaning |
|--------|---------|
| `Turtle` | Class |
| `timmy` | Object (instance of `Turtle`) |

---

## Accessing Attributes

```
print(my_screen.canvheight)
```

### Syntax

```
object.attribute
```

### Explanation

- Attributes are pieces of data stored inside an object.
- They can be accessed using **dot notation (`.`)**.
- Attributes do not use parentheses.

---

## Calling Methods

```
timmy.forward(100)
timmy.color("coral")
timmy.shape("turtle")
```

### Syntax

```
object.method()
```

### Explanation

- Methods are functions that belong to an object.
- Methods are called using **dot notation** followed by parentheses.
- Parentheses may contain arguments depending on the method.

---

## Complete Example

```
from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

screen = Screen()
screen.exitonclick()
```

### What Happens?

1. A `Turtle` object named `timmy` is created.
2. The turtle's shape is changed to `"turtle"`.
3. The turtle's color is changed to `"coral"`.
4. The turtle moves forward by `100` units.
5. A `Screen` object is created.
6. The window remains open until it is clicked.

---

## Dot Notation

Dot notation (`.`) is used to interact with objects.

### Access an Attribute

```
object.attribute
```

Example:

```
print(my_screen.canvheight)
```

### Call a Method

```
object.method()
```

Example:

```
timmy.forward(100)
```


## Key Takeaways

- Classes are blueprints for creating objects.
- Objects are created using `ClassName()`.
- Attributes store information about an object.
- Methods define actions an object can perform.
- Dot notation (`.`) is used to access both attributes and methods.
- Documentation is useful for discovering available attributes and methods.