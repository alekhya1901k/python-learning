# Coffee Machine Project — Concise Notes

## Goal

Build a coffee machine program that lets the user buy **espresso, latte, or cappuccino** using coins.

## 10 Quick Points

1. `MENU` stores drink details: ingredients and cost.
2. `resources` stores available water, milk, and coffee.
3. `profit` stores total money earned.
4. User chooses a drink from input.
5. Typing `report` shows current resources and money.
6. Typing `off` stops the machine.
7. `is_resource_sufficient()` checks if ingredients are enough.
8. `process_coins()` calculates inserted money.
9. `is_transaction_successful()` checks payment and gives change.
10. `make_coffee()` deducts ingredients and serves coffee.

## Main Flow

```text
Start
↓
Ask user drink choice
↓
If off → stop
If report → show resources
Else → check resources
↓
Take coins
↓
Check payment
↓
Deduct ingredients
↓
Serve coffee
```

## Important Functions

### `is_resource_sufficient()`

Checks whether the machine has enough ingredients.

### `process_coins()`

Asks for quarters, dimes, nickels, and pennies, then calculates total money.

### `is_transaction_successful()`

Checks if user paid enough.
If yes, adds money to profit and returns change.

### `make_coffee()`

Reduces used ingredients from resources and prints coffee message.

## Example

User chooses:

```text
latte
```

Latte needs:

```text
Water: 200ml
Milk: 150ml
Coffee: 24g
Cost: $2.5
```

If resources and payment are enough:

```text
Here is your latte ☕️. Enjoy!
```

## Interview FAQs

### 1. Why is `MENU` a dictionary?

Because each drink has related data like ingredients and cost.

### 2. Why use functions?

Functions make code reusable, organized, and easier to debug.

### 3. Why is `global profit` used?

Because the function modifies the global `profit` variable.

### 4. What happens if resources are not enough?

The program prints which ingredient is missing and does not take money.

### 5. What happens if payment is insufficient?

Money is refunded and coffee is not made.

### 6. Why use a `while` loop?

Because the machine should keep running until the user types `off`.

### 7. What does `report` do?

It displays current water, milk, coffee, and money.

## Key Concepts Learned

Dictionaries, nested dictionaries, functions, loops, conditionals, user input, global variables, return values, and basic simulation logic.
