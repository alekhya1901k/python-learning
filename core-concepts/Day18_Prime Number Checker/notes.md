# Prime Number Checker

## 1. Quick Short Notes (10 Summary Points)

1. A prime number has exactly **two factors**: 1 and itself.
2. Numbers less than or equal to **1 are not prime**.
3. **2 is the only even prime number**.
4. Any even number greater than 2 is **not prime**.
5. A prime number cannot be divided evenly by any number other than 1 and itself.
6. To check primality, test divisibility from **2 up to √n**.
7. If a divisor is found, the number is **not prime**.
8. If no divisor exists, the number is **prime**.
9. Using √n improves efficiency compared to checking all numbers up to n.
10. Prime numbers are widely used in **cryptography, security, and mathematics**.

---

## 2. Examples

### Example 1: Prime Number

Input:

```python
73
```

Checks:

* Not divisible by 2
* Not divisible by 3
* Not divisible by 4
* Not divisible by 5
* Not divisible by 6
* Not divisible by 7
* √73 ≈ 8.54

No divisor found.

Output:

```python
True
```

---

### Example 2: Not a Prime Number

Input:

```python
75
```

Checks:

* 75 ÷ 3 = 25

Divisor found.

Output:

```python
False
```

---

## 3. Logic / Algorithm

### Step-by-Step

1. Accept a number.
2. If number ≤ 1, return False.
3. Loop from 2 to √number.
4. Check if number is divisible by current value.
5. If divisible, return False.
6. If loop completes, return True.

---

## 4. Flow of Execution


Start
  │
Input Number
  │
Is Number <= 1?
 ├─ Yes → False
 │
 └─ No
      │
Check divisibility from 2 to √n
      │
Divisor Found?
 ├─ Yes → False
 │
 └─ No → True
      │
     End

---

