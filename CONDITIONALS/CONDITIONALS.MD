
---

# 🧠 1. What are Conditionals in Python?

Conditionals = **decision makers in code**

👉 They let your program choose *what to do next* based on a condition (True/False).

### Basic Structure:

```python
if condition:
    # runs if True
elif another_condition:
    # runs if first is False, second is True
else:
    # runs if all above are False
```

---

# ⚡ 2. Comparison Operators (VERY IMPORTANT for DSA)

These are what we use inside conditions 👇

| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | equal to         |
| `!=`     | not equal        |
| `>`      | greater than     |
| `<`      | less than        |
| `>=`     | greater or equal |
| `<=`     | less or equal    |

### Example:

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

---

# 🔗 3. Logical Operators (Combine Conditions)

| Operator | Meaning                      |
| -------- | ---------------------------- |
| `and`    | both conditions must be True |
| `or`     | at least one True            |
| `not`    | reverses condition           |

### Example:

```python
x = 10

if x > 5 and x < 20:
    print("x is between 5 and 20")
```

---

# 🧩 4. Nested Conditionals (Condition inside Condition)

👉 Used when decisions depend on multiple levels

```python
x = 10

if x > 5:
    if x % 2 == 0:
        print("Even and greater than 5")
    else:
        print("Odd and greater than 5")
```

---

# 🚀 5. Conditionals in DSA (THIS IS THE MAIN PART)

Now let’s connect to **real algorithms** 👇

---

## 🔍 A. Searching (Linear Search Example)

👉 We check each element using condition

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:   # CONDITION
            return i
    return -1
```

### 🧠 Thinking:

* “Is this element equal to target?”
* If YES → stop
* If NO → continue

---

## ⚡ B. Binary Search (VERY IMPORTANT)

👉 Decisions cut the array in half

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1   # go right
        else:
            right = mid - 1  # go left

    return -1
```

### 🧠 Thinking:

* Is middle = target?
* If smaller → go right
* If bigger → go left

👉 Entire algorithm = just conditionals 🔥

---

## 🔄 C. Sorting (Bubble Sort Example)

👉 Condition used to compare & swap

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:   # CONDITION
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
```

### 🧠 Thinking:

* “Is left element bigger than right?”
* If YES → swap
* If NO → leave it

---

# 🎯 6. Real DSA Patterns Using Conditionals

## ✅ Pattern 1: Checking Condition

```python
if arr[i] == target:
```

## ✅ Pattern 2: Updating Answer

```python
if arr[i] < min_val:
    min_val = arr[i]
```

## ✅ Pattern 3: Decision Making

```python
if mid < target:
    left = mid + 1
```

## ✅ Pattern 4: Filtering

```python
if num % 2 == 0:
    even_list.append(num)
```

---

# ⚠️ 7. Common Mistakes (VERY IMPORTANT)

❌ Using `=` instead of `==`

```python
if x = 5   # WRONG
```

✔️ Correct:

```python
if x == 5
```

---

❌ Wrong indentation

```python
if x > 5:
print(x)
```

✔️ Correct:

```python
if x > 5:
    print(x)
```

---

# 🧠 Final Understanding (SUPER IMPORTANT)

👉 In DSA:

* **Loops = repetition**
* **Conditionals = intelligence**

Without conditionals:
👉 Algorithms cannot decide anything.

---

# 🔥 Mini Challenge (Try this)

Write a function:

* Find **maximum element** in array using conditionals

```python
def find_max(arr):
    max_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num

    return max_val
```

---


