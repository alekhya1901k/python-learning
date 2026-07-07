```markdown id="d5m8qw"
# Hirst Painting Project Part 2 – Drawing the Dots

## Quick Short Notes

1. The project creates a **10 × 10 grid** containing 100 colored dots.
2. The color palette extracted using Colorgram is reused for painting.
3. Each dot is assigned a random color from the color palette.
4. The `dot()` method quickly draws filled circular dots.
5. `penup()` prevents lines from appearing while the Turtle moves between dots.
6. `hideturtle()` hides the Turtle cursor, giving the artwork a cleaner appearance.
7. Loops automate drawing rows and columns of dots.
8. The modulo (`%`) operator detects when a row is complete and starts a new one.
9. Setting the Turtle speed to `"fastest"` significantly reduces drawing time.
10. This project combines loops, functions, randomness, Turtle Graphics, RGB colors, tuples, and documentation into one complete application.

## Example

tim.dot(20, random.choice(color_list))

## Quick Summary

1. Draw a total of **100 dots**.
2. Assign random colors from the extracted palette.
3. Use `penup()` to avoid drawing connecting lines.
4. Hide the Turtle using `hideturtle()`.
5. Set the speed to `"fastest"` for quicker drawing.
6. Choose an appropriate dot size (e.g., 20).
7. Arrange dots in a 10 × 10 grid.
8. Use loops to automate drawing.
9. Use modulo (`%`) to detect the end of each row.
10. This is the final Turtle Graphics project combining all previous concepts.

