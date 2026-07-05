# 1. Object Oriented Programming (OOP) Introduction

## Quick Short Notes 

1. **OOP (Object Oriented Programming)** is a programming paradigm used to organize complex code into manageable pieces.
2. **Procedural Programming** uses functions and procedures that execute step-by-step from top to bottom.
3. As projects grow larger, procedural code can become difficult to manage and understand.
4. OOP helps reduce "spaghetti code" by grouping related data and behavior together.
5. OOP encourages **modularity**, where large systems are divided into smaller components.
6. Different teams can work on separate modules independently.
7. OOP promotes **code reusability**, allowing existing components to be reused in future projects.
8. Real-world systems such as self-driving cars can be divided into modules like navigation, camera, lane detection, and fuel management.
9. OOP allows developers to focus on **what an object does** rather than **how it does it internally**.
10. Large software systems become easier to maintain, extend, test, and debug using OOP principles.

---

# Procedural Programming

## What is Procedural Programming?

Procedural Programming organizes code as a sequence of instructions and functions.

### Characteristics

* Functions perform specific tasks.
* Execution generally flows top-to-bottom.
* Variables are often shared between functions.
* Easier for small projects.
* Becomes difficult to manage in large applications.

### Problems with Procedural Programming

* Too many interconnected functions.
* Difficult to track variable changes.
* High dependency between code sections.
* Harder to maintain large systems.
* Increased risk of bugs.

### Example

```python
def take_order():
    print("Order Taken")

def cook_food():
    print("Food Prepared")

def serve_food():
    print("Food Served")

take_order()
cook_food()
serve_food()
```

---

# Why OOP Was Introduced

As software became larger:

* More features were added.
* More developers worked together.
* More relationships existed between components.

OOP was introduced to:

* Reduce complexity.
* Improve maintainability.
* Increase reusability.
* Support teamwork.
* Build scalable applications.

---

# Self-Driving Car Analogy

A self-driving car can be divided into multiple modules:

| Module          | Responsibility      |
| --------------- | ------------------- |
| Camera System   | Detect road objects |
| Lane Detection  | Stay within lane    |
| Navigation      | Find routes         |
| Fuel Management | Monitor fuel levels |

### Benefits

* Teams can work independently.
* Modules can be reused later.
* Easier testing and maintenance.
* Faster development.

---

# Restaurant Analogy (Understanding OOP)

## One-Person Restaurant (Procedural Programming)

One person performs:

* Receptionist
* Waiter
* Chef
* Cleaner

### Problems

* Slow
* Difficult to scale
* Overloaded responsibilities

## Organized Restaurant (OOP)

Separate staff members handle:

* Waiter
* Chef
* Cleaner
* Receptionist

The manager only coordinates work.

### OOP Lesson

Each object has:

* A specific responsibility
* Its own behavior
* Minimal dependency on others

This makes systems cleaner and easier to manage.

---

# Key Benefits of OOP

## 1. Modularity

Large projects are broken into smaller pieces.

## 2. Reusability

Components can be reused in future applications.

## 3. Scalability

Applications can grow without becoming chaotic.

## 4. Maintainability

Fixes and updates are easier.

## 5. Team Collaboration

Different teams can work on different modules simultaneously.

---

# Example of Reusability

## Project 1: Self-Driving Car

Uses:

* Camera Module
* Navigation Module
* Fuel Management Module

## Project 2: Delivery Drone

Can reuse:

* Camera Module
* Navigation Module
* Fuel Management Module

No need to rewrite everything.

---

**Procedural Programming = Organize code around functions.**

**Object Oriented Programming (OOP) = Organize code around objects that contain both data and behavior, making large applications easier to build, maintain, and reuse.**
