```markdown id="4tmc7k"
# Turtle Challenge 5 – Draw a Spirograph

## Quick Short Notes

1. A spirograph is created by repeatedly drawing circles while slightly changing the Turtle's direction.
2. The Turtle's heading changes after every circle to create the overlapping pattern.
3. Loops automate the repeated drawing process.
4. The radius of each circle remains constant throughout the drawing.
5. Using random colors makes the spirograph more attractive.
6. The `circle()` method draws a circle with a specified radius.
7. The `heading()` method returns the Turtle's current direction.
8. The `setheading()` method changes the Turtle's direction to a specified angle.
9. Increasing the Turtle's speed improves drawing performance.
10. Since `range()` only accepts integers, floating-point values must be converted using `int()`.

## Example

tim.circle(100)
tim.setheading(tim.heading() + 10)

## Quick Summary

1. Draw circles repeatedly.
2. Rotate the heading after each circle.
3. Use loops to automate repetition.
4. Apply random colors for better visuals.
5. Keep the circle radius constant.
6. Use `circle()` to draw circles.
7. Set Turtle speed to `"fastest"` for better performance.
8. Update the heading after every iteration.
9. Convert floating-point values to integers for `range()`.
10. Repeated circles create beautiful geometric patterns.

