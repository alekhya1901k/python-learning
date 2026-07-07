```markdown id="g8v2kp"
# Hirst Painting Project Part 1 – RGB Extraction

## Quick Short Notes

1. The project uses the external **Colorgram** package to extract colors from images.
2. Colorgram identifies the dominant colors present in an image.
3. Extracted RGB values are stored as tuples for easy use.
4. The image file should be placed inside the project folder.
5. External packages must be installed before they can be imported.
6. The extracted colors form the color palette for the painting.
7. Background colors (such as white) are usually removed from the palette.
8. The remaining colors are stored in a Python list.
9. The extracted palette can be reused throughout the project.
10. Color extraction simplifies generating artwork with colors similar to the original image.

## Example

colors = colorgram.extract("image.jpg", 30)

## Quick Summary

1. Install the Colorgram package.
2. Import the package into the project.
3. Load the target image.
4. Extract the dominant colors.
5. Convert RGB values into tuples.
6. Store the tuples in a color palette list.
7. Remove white or background colors.
8. Reuse the palette throughout the project.
9. Color extraction is efficient and reusable.
10. The extracted palette is used in the final Hirst Painting project.

