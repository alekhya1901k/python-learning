# 4. How to Add Python Packages and Use PyPI

## Quick Summary Notes

- A module is usually a single Python file.
- A package contains multiple modules.
- PyPI stands for Python Package Index.
- PyPI contains thousands of Python packages.
- Packages are created by developers worldwide.
- Packages save development time.
- Some packages come pre-installed.
- Others require installation.
- Documentation explains package usage.
- Packages extend Python functionality.

---

## Installing a Package

```
pip install prettytable
```

### Explanation

- `pip` is Python's package installer.
- It downloads and installs packages from PyPI.
- After installation, the package can be imported into your Python programs.

---

## Why Use Packages?

Instead of building everything yourself, you can use existing packages to:

- Create tables
- Generate charts
- Work with APIs
- Handle data science tasks
- Build web applications

### Benefits

- Saves development time
- Reduces complexity
- Provides tested and reliable code
- Increases productivity

---

## Module vs Package

| Type | Description |
|--------|-------------|
| Module | A single Python file containing code |
| Package | A collection of related modules |

### Example

```
# Module
math.py

# Package
pandas
numpy
requests
```

---

## Popular Packages

| Package | Purpose |
|----------|---------|
| `prettytable` | Create ASCII tables |
| `requests` | API calls |
| `pandas` | Data analysis |
| `numpy` | Numerical computing |
| `turtle` | Graphics |

---

## Example: Using PrettyTable

```
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Name", ["Alice", "Bob", "Charlie"])
table.add_column("Age", [25, 30, 35])

print(table)
```

### Output

```
+---------+-----+
|   Name  | Age |
+---------+-----+
|  Alice  |  25 |
|   Bob   |  30 |
| Charlie |  35 |
+---------+-----+
```

---

## Understanding PyPI

### What is PyPI?

PyPI (Python Package Index) is the official repository for Python packages.

### Features

- Hosts thousands of Python packages
- Maintained by the Python community
- Allows developers to share code
- Makes package installation simple using `pip`

---

## Documentation

Documentation helps developers:

- Learn package features
- Understand available classes
- Discover attributes and methods
- Follow best practices
- Find usage examples

---


## Key Takeaways

- PyPI is the Python Package Index.
- Packages extend Python's functionality.
- `pip` is used to install packages.
- Modules are single files.
- Packages are collections of modules.
- Documentation is essential for learning how to use packages effectively.
- Using existing packages saves significant development time.