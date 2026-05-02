

---

# 🧠 What is Type Casting?

👉 **Type casting = converting one data type into another**

```python
int()    # → integer
float()  # → decimal
str()    # → string
bool()   # → True / False
```

---

# 🔢 1. `int()` — Convert to Integer

## ✅ Examples

```python
x = int("10")      # 10
y = int(3.7)       # 3 (cuts decimal)
```

## 🚨 Important in DSA

```python
n = int(input())   # ALWAYS needed
```

👉 Input is **string by default**, so:

```python
n = input()   # ❌ string
n = int(input())  # ✅ integer
```

---

# 🔢 2. `float()` — Convert to Decimal

```python
x = float("3.14")  # 3.14
y = float(5)       # 5.0
```

## 🧠 Use in DSA

* Average
* Precision problems
* Geometry problems

---

# 🔤 3. `str()` — Convert to String

```python
x = str(123)   # "123"
```

## 🔥 Useful in DSA

### Reverse number trick

```python
n = 1234
rev = str(n)[::-1]  # "4321"
```

### Digit iteration

```python
for digit in str(n):
    print(int(digit))
```

---

# 🔘 4. `bool()` — Convert to Boolean

```python
bool(0)        # False
bool(1)        # True
bool("")       # False
bool("abc")    # True
```

## ⚡ Truthy vs Falsy (VERY IMPORTANT)

| Value           | Boolean |
| --------------- | ------- |
| 0, 0.0          | False   |
| "", None        | False   |
| Empty list/dict | False   |
| Everything else | True    |

---

# 🧠 Where casting is used in DSA

## 1. Input handling 🧾

```python
arr = list(map(int, input().split()))
```

👉 Converts:

```
"1 2 3" → [1, 2, 3]
```

---

## 2. Character → Integer

```python
ch = '5'
num = int(ch)  # 5
```

---

## 3. Integer → Digits

```python
n = 123
digits = list(map(int, str(n)))  # [1,2,3]
```

---

## 4. Boolean conditions

```python
if bool(n):
    print("Non-zero")
```

---

# 🚨 Common Errors (VERY IMPORTANT)

## ❌ 1. Invalid string → int

```python
int("abc")  # ❌ ValueError
```

---

## ❌ 2. Float string → int directly

```python
int("3.14")  # ❌
```

✅ Fix:

```python
int(float("3.14"))
```

---

## ❌ 3. Forgetting input casting

```python
n = input()
print(n + 1)  # ❌ error
```

---

## ❌ 4. Mixing types

```python
"5" + 2   # ❌
```

---

## ❌ 5. bool confusion

```python
if "0":   # TRUE 😳
```

👉 Because non-empty string = True

---

# 💡 Pro Tips (DSA Gold 🏆)

## ⭐ Fast input conversion

```python
arr = list(map(int, input().split()))
```

---

## ⭐ Convert list of digits to number

```python
digits = [1,2,3]
num = int("".join(map(str, digits)))  # 123
```

---

## ⭐ Check digit

```python
ch.isdigit()
```

---

# 🔥 Mini Practice (Do This)

Try solving 👇

### 1.

```python
s = "12345"
# Convert to list of integers → [1,2,3,4,5]
```

---

### 2.

```python
n = 9876
# Reverse using type casting
```

---

### 3.

```python
s = "10 20 30"
# Convert into list of ints
```

---

### 4.

```python
x = "0"
# What is bool(x)?
```

---

# 🧩 Final Pattern to Remember

> 🔹 Input → always string
> 🔹 Convert early → avoid bugs
> 🔹 Use `str()` for digit tricks
> 🔹 Use `map()` for fast conversion

---


