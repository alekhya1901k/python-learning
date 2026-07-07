```markdown
# Turtle Challenge 2 – Draw a Dashed Line

## Quick Short Notes

1. A dashed line is created by alternating between drawing and leaving gaps.
2. `penup()` lifts the pen so the Turtle moves without drawing.
3. `pendown()` places the pen back on the screen to resume drawing.
4. The Turtle continues moving even when the pen is lifted.
5. Loops automate the repeated drawing and skipping pattern.
6. The Turtle documentation explains how to control the pen.
7. Gaps make the line appear dashed instead of continuous.
8. Drawing and movement are independent actions.
9. The pen's state (up or down) determines whether movement leaves a trail.
10. Repeating patterns like dashed lines are ideal candidates for loops.

## Example

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

## Quick Summary

1. `penup()` lifts the pen.
2. `pendown()` resumes drawing.
3. The Turtle can move without drawing.
4. Loops simplify repetitive patterns.
5. Dashed lines alternate between drawing and gaps.
6. Documentation helps discover useful methods.
7. Pen state controls whether lines are drawn.
8. Movement continues regardless of pen state.
9. The same logic can be reused for other patterns.
10. Loops make dashed-line generation simple and efficient.

