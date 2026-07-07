```markdown
# Day 22 - Interview FAQs

## 1. What is Turtle Graphics?

Turtle Graphics is a Python graphics library used to draw shapes, patterns, and animations by moving a virtual turtle around the screen.

---

## 2. Why do we create a `Screen` object?

The `Screen` object creates and controls the graphics window where the Turtle performs its drawing.

---

## 3. What does `exitonclick()` do?

It keeps the Turtle graphics window open until the user clicks inside the window.

---

## 4. Why is official documentation important?

Official documentation explains available classes, methods, parameters, return values, and examples, making it the primary reference for learning a library.

---

## 5. What is dot notation?

Dot notation is used to access an object's attributes and methods.

**Example:**

`tim.forward(100)`

---

## 6. What is the difference between a module and a package?

- **Module:** A single Python file containing code.
- **Package:** A collection of related Python modules organized into directories.

---

## 7. What is the difference between `import module` and `from module import item`?

- `import module` imports the entire module.
- `from module import item` imports only the required class, function, or variable.

---

## 8. Why should `from module import *` be avoided?

It pollutes the namespace, reduces code readability, and may cause naming conflicts between different modules.

---

## 9. Why are aliases used in Python imports?

Aliases shorten long module names, making code easier to read.

**Example:**

`import turtle as t`

---

## 10. What is a virtual environment?

A virtual environment is an isolated Python workspace that stores project-specific packages and dependencies separately from other projects.

---

## 11. Why should packages be installed per project?

Installing packages per project prevents dependency conflicts and allows different projects to use different library versions.

---

## 12. Why do we use loops when drawing shapes?

Loops eliminate repetitive code by repeating the same set of instructions multiple times, making programs shorter and easier to maintain.

---

## 13. Why does the Turtle turn 90° when drawing a square?

A square has four right angles (90° each), so the Turtle must turn 90° after drawing each side.

---

## 14. What happens if the turning angle changes?

Changing the angle changes the final shape because the geometry depends on the turning angle.

---

## 15. Why do we use `range(4)` when drawing a square?

A square has four sides, so the loop must execute exactly four times.

---

## 16. How does the Turtle know where to move?

The Turtle moves in the direction of its current heading. Commands like `left()`, `right()`, and `setheading()` change this direction.

---

## 17. What is the difference between `penup()` and `pendown()`?

- `penup()` lifts the pen so the Turtle moves without drawing.
- `pendown()` lowers the pen so movement draws lines.

---

## 18. Does the Turtle move while the pen is up?

Yes. The Turtle continues moving, but it leaves no visible line.

---

## 19. Why use `penup()` in the Hirst Painting project?

It prevents unwanted connecting lines while the Turtle moves between dots.

---

## 20. Can the dash length and gap size be customized?

Yes. Simply change the distance passed to `forward()` for both the drawn segments and the gaps.

---

## 21. What is Tkinter?

Tkinter is Python's built-in GUI (Graphical User Interface) library. Turtle Graphics is built on top of Tkinter.

---

## 22. What is the difference between a CLI and a GUI?

- **CLI (Command-Line Interface):** Users interact by typing commands.
- **GUI (Graphical User Interface):** Users interact using windows, buttons, graphics, and a mouse.

---

## 23. Why are colors used in Turtle Graphics?

Colors improve the appearance of drawings and make different shapes easier to distinguish.

---

## 24. What does `forward()` do?

`forward()` moves the Turtle forward by a specified distance in its current direction.

---

## 25. What does `right()` do?

`right()` rotates the Turtle clockwise by the specified number of degrees.

---

## 26. What is a Random Walk?

A Random Walk is a sequence of movements where each step is taken in a randomly selected direction. It is commonly used in mathematics and simulations.

---

## 27. Why do we use `setheading()`?

`setheading()` directly sets the Turtle's direction to a specified angle, making movement simpler and more predictable.

---

## 28. Why is `setheading()` preferred over multiple `left()` and `right()` calls?

It directly sets the exact direction instead of calculating multiple turns, making the code cleaner and easier to understand.

---

## 29. Why is `random.choice()` used?

`random.choice()` randomly selects one item from a sequence, making it ideal for choosing random directions or colors.

---

## 30. What controls the Turtle's drawing speed?

The `speed()` method controls the animation speed. `"fastest"` is commonly used for complex drawings.

---

## 31. Why increase the pen size?

Increasing the pen size makes drawing lines thicker and easier to see.

---

## 32. What is a tuple?

A tuple is an ordered, immutable collection of values enclosed in parentheses.

---

## 33. What is the difference between a tuple and a list?

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Can be modified | Cannot be modified |

---

## 34. Why do we use RGB colors?

RGB combines Red, Green, and Blue values to create millions of different colors.

---

## 35. Why do we call `turtle.colormode(255)`?

It changes Turtle's RGB range from **0–1** to **0–255**, making standard RGB values usable.

---

## 36. Can tuple values be changed?

No. Tuples are immutable, so their values cannot be modified after creation.

---

## 37. What creates a spirograph?

A spirograph is created by repeatedly drawing circles while rotating the Turtle by a fixed angle after each circle.

---

## 38. Why do we change the Turtle's heading while drawing a spirograph?

Changing the heading rotates each new circle slightly, creating the overlapping geometric design.

---

## 39. Why do we convert values to `int()` before using `range()`?

`range()` only accepts integer values. Division usually returns a float, so conversion is required.

---

## 40. Why do we use loops in a spirograph?

Loops repeatedly draw circles and rotate the Turtle automatically without duplicating code.

---

## 41. What controls the size of each circle?

The radius passed to the `circle()` method determines the size of the circle.

---

## 42. What is Colorgram?

Colorgram is a Python package that extracts the most common colors from an image.

---

## 43. Why do we need to install Colorgram?

Colorgram is an external package and is not included in Python's Standard Library.

---

## 44. Why are RGB values stored as tuples?

RGB colors are fixed values, making tuples an ideal immutable data structure for storing them.

---

## 45. Why do we remove white or background colors?

Background colors usually do not contribute to the artwork and are removed to create a cleaner color palette.

---

## 46. Where should the image be stored?

The image should be stored inside the project folder (or referenced using the correct file path) so Colorgram can access it.

---

## 47. Why do we use `dot()` instead of `circle()`?

`dot()` quickly draws a filled circle of a specified size and color without requiring extra drawing logic.

---

## 48. Why do we hide the Turtle?

`hideturtle()` removes the Turtle cursor, making the final artwork cleaner and slightly improving drawing performance.

---

## 49. Why do we use the modulo (`%`) operator?

The modulo operator detects when a row is complete so the Turtle can automatically move to the next row.

---

## 50. Why do we use `speed("fastest")`?

It minimizes animation delays and significantly speeds up drawing large graphics.

---

## 51. What concepts are combined in the Hirst Painting project?

The Hirst Painting project combines:

- Turtle Graphics
- Loops
- Functions
- RGB Colors
- Tuples
- Randomness
- External Packages (Colorgram)
- Documentation Usage
- Coordinate-Based Drawing
- Grid-Based Pattern Generation
```
