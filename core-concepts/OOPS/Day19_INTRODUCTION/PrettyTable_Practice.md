# 5. Practice Modifying Object Attributes and Calling Methods

## Quick Summary Notes

- PrettyTable is an external package.
- PrettyTable helps create ASCII tables.
- Objects can have methods.
- Objects can have attributes.
- Methods perform actions.
- Attributes store settings or data.
- `add_column()` is a method.
- `align` is an attribute.
- Documentation shows available functionality.
- Objects become powerful through attributes and methods.

---

## Example

```
from prettytable import PrettyTable

table = PrettyTable()

table.add_column(
    "Pokemon Name",
    ["Pikachu", "Squirtle", "Charmander"]
)

table.add_column(
    "Type",
    ["Electric", "Water", "Fire"]
)

table.align = "l"

print(table)
```

---

## Output

```
+--------------+----------+
| Pokemon Name | Type     |
+--------------+----------+
| Pikachu      | Electric |
| Squirtle     | Water    |
| Charmander   | Fire     |
+--------------+----------+
```

---

## Understanding the Example

### Step 1: Import the Package

```
from prettytable import PrettyTable
```

- Imports the `PrettyTable` class from the package.
- Allows creation of table objects.

---

### Step 2: Create an Object

```
table = PrettyTable()
```

- `PrettyTable` is the class.
- `table` is the object.
- Parentheses create a new object.

---

### Step 3: Call the `add_column()` Method

```
table.add_column(
    "Pokemon Name",
    ["Pikachu", "Squirtle", "Charmander"]
)
```

- `add_column()` is a method.
- It adds a new column to the table.
- The first argument is the column heading.
- The second argument contains the column values.

---

### Step 4: Add Another Column

```
table.add_column(
    "Type",
    ["Electric", "Water", "Fire"]
)
```

- Adds a second column.
- Each item aligns with the corresponding Pokémon.

---

### Step 5: Modify an Attribute

```
table.align = "l"
```

- `align` is an attribute.
- `"l"` means left alignment.
- Changing the attribute changes the table's appearance.

---

### Step 6: Display the Table

```
print(table)
```

- Prints the formatted ASCII table.
- Shows all columns and rows.

---

## Methods vs Attributes

| Feature | Method | Attribute |
|----------|----------|----------|
| Purpose | Performs an action | Stores data or settings |
| Parentheses Required | Yes | No |
| Example | `add_column()` | `align` |
| Usage | `table.add_column(...)` | `table.align = "l"` |

---

## Object Interaction

Objects become useful because they combine:

### Attributes

Store information and settings.

Example:

```
table.align = "l"
```

### Methods

Perform actions and operations.

Example:

```
table.add_column(...)
```

Together, attributes and methods define how an object behaves.

---

## Why Documentation Matters

Documentation helps developers:

- Discover available methods
- Learn available attributes
- Understand usage patterns
- Find examples
- Customize object behavior

When using a new package, documentation is often the first place to look.

---


## Key Takeaways

- PrettyTable is an external Python package.
- Objects contain both attributes and methods.
- Methods perform actions.
- Attributes store settings and data.
- `add_column()` is a method.
- `align` is an attribute.
- Documentation helps developers discover and use object functionality.
- Modifying attributes allows customization without changing the underlying code.