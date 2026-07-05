# 6. Building the Coffee Machine in OOP

## Quick Summary Notes

- OOP separates responsibilities into classes.
- `CoffeeMaker` manages ingredients.
- `MoneyMachine` manages money.
- `Menu` stores drink options.
- `MenuItem` represents a drink.
- `report()` displays machine status.
- `get_items()` returns menu choices.
- `find_drink()` finds a selected drink.
- `is_resource_sufficient()` checks ingredients.
- `make_payment()` handles payments.

---

## Why Use OOP for the Coffee Machine?

Object-Oriented Programming (OOP) helps organize code by assigning specific responsibilities to different classes.

### Benefits

- Easier to maintain
- Easier to debug
- Reusable code
- Better organization
- Clear separation of responsibilities

Instead of placing all logic in one file, each class handles a specific task.

---

## Coffee Machine Class Responsibilities

### CoffeeMaker

Responsible for managing ingredients and making coffee.

#### Responsibilities

- Manage water
- Manage milk
- Manage coffee
- Make coffee
- Generate reports

#### Common Methods

```
report()
is_resource_sufficient()
make_coffee()
```

---

### MoneyMachine

Responsible for handling all money-related operations.

#### Responsibilities

- Accept coins
- Calculate money
- Return change
- Track profit

#### Common Methods

```
make_payment()
report()
```

---

### Menu

Responsible for storing and retrieving drink information.

#### Responsibilities

- Store available drinks
- Return menu options
- Find requested drink

#### Common Methods

```
get_items()
find_drink()
```

---

### MenuItem

Represents a single drink on the menu.

#### Responsibilities

- Store drink name
- Store ingredient requirements
- Store drink cost

#### Example Drinks

- Espresso
- Latte
- Cappuccino

---

## Key Methods

### `report()`

Displays the current machine status.

Example:

```
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $5.00
```

---

### `get_items()`

Returns available menu choices.

Example:

```
espresso/latte/cappuccino
```

---

### `find_drink()`

Finds and returns the selected drink.

Example:

```
menu.find_drink("latte")
```

---

### `is_resource_sufficient()`

Checks whether enough ingredients exist.

Example:

```
coffee_maker.is_resource_sufficient(drink)
```

Possible result:

```
True
```

or

```
Sorry there is not enough water.
```

---

### `make_payment()`

Processes customer payment.

Example:

```
money_machine.make_payment(drink.cost)
```

Responsibilities:

- Accept coins
- Calculate total
- Verify payment
- Return change if necessary

---

## Coffee Machine Flow

```text
Start
   ↓
Display Menu
   ↓
Get User Choice
   ↓
Check Resources
   ↓
Process Payment
   ↓
Make Coffee
   ↓
Update Resources
   ↓
Display Drink
   ↓
Repeat
```

---

## Typical Program Workflow

### Step 1: Display Menu

```
espresso/latte/cappuccino
```

---

### Step 2: User Selects a Drink

```
latte
```

---

### Step 3: Check Resources

```
is_resource_sufficient()
```

Verify enough:

- Water
- Milk
- Coffee

---

### Step 4: Process Payment

```
make_payment()
```

- Insert coins
- Calculate amount
- Return change if needed

---

### Step 5: Make Coffee

```
make_coffee()
```

Resources are deducted.

---

### Step 6: Serve Drink

```
Here is your latte ☕
```

---

### Step 7: Wait for Next Customer

Program continues running until stopped.

---

## OOP Design Overview

| Class | Responsibility |
|---------|---------------|
| `CoffeeMaker` | Ingredient management |
| `MoneyMachine` | Money handling |
| `Menu` | Menu management |
| `MenuItem` | Individual drink representation |

This design keeps each class focused on a single task.

---

## OOP Principle Demonstrated

### Separation of Responsibilities

Each class has one primary responsibility.

Examples:

- `CoffeeMaker` handles ingredients.
- `MoneyMachine` handles payments.
- `Menu` handles drink selection.

This makes the program easier to:

- Understand
- Modify
- Test
- Expand

---


## Key Takeaways

- OOP divides the coffee machine into specialized classes.
- `CoffeeMaker` manages ingredients.
- `MoneyMachine` manages money.
- `Menu` manages drink options.
- `MenuItem` represents a single drink.
- Classes communicate to complete the coffee-making process.
- Separation of responsibilities improves maintainability and scalability.
- The Coffee Machine project is a practical example of modular OOP design.