# Interview FAQs

### 1. What is a prime number?

A prime number is a number greater than 1 that has exactly two factors: 1 and itself.

---

### 2. Why is 1 not considered a prime number?

Because a prime number must have exactly two distinct factors, while 1 has only one factor (1).

---

### 3. Why is 2 a prime number?

Because it is divisible only by 1 and 2. It is also the only even prime number.

---

### 4. Why do we check divisibility only up to √n?

If a number has a factor larger than √n, it must also have a corresponding factor smaller than √n. Therefore checking beyond √n is unnecessary.

---

### 5. What is the time complexity of the optimized prime checker?

The time complexity is:

```text
O(√n)
```

because we only check factors up to the square root of the number.

---

### 6. Is 0 a prime number?

No. Prime numbers must be greater than 1.

---

### 7. Is every odd number a prime number?

No.

Example:

```python
9 = 3 × 3
15 = 3 × 5
21 = 3 × 7
```

These are odd but not prime.

---

### 8. What is the difference between prime and composite numbers?

| Prime Number         | Composite Number     |
| -------------------- | -------------------- |
| Exactly 2 factors    | More than 2 factors  |
| Examples: 2, 3, 5, 7 | Examples: 4, 6, 8, 9 |

---

### 9. Which Python operator is used to check divisibility?

The modulus operator `%`.

Example:

```python
10 % 2 == 0
```

Output:

```python
True
```

---

### 10. What are some applications of prime numbers?

* Cryptography (RSA Encryption)
* Cybersecurity
* Computer Algorithms
* Hash Functions
* Number Theory
* Digital Signatures

---

## Sample Test Cases

| Input | Output |
| ----- | ------ |
| 2     | True   |
| 3     | True   |
| 4     | False  |
| 5     | True   |
| 10    | False  |
| 17    | True   |
| 73    | True   |
| 75    | False  |
| 97    | True   |
| 100   | False  |

---

### Key Interview Takeaway

> A number is prime if it is greater than 1 and has no divisors other than 1 and itself. The most efficient beginner-friendly approach is to check divisibility only up to the square root of the number, giving a time complexity of **O(√n)**.
