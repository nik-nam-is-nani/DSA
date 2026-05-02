

---

# 🧠 1. What is a String (DSA mindset)

```python
s = "hello"
```

👉 A string is a **sequence of characters**

Think of it like an array:

```
h   e   l   l   o
0   1   2   3   4
```

---

## 🔬 Memory Thinking

* Stored as a **sequence**
* Each character has an **index**
* Internally optimized, but conceptually like an array

---

# 📍 2. Indexing (VERY IMPORTANT)

```python
s = "hello"

print(s[0])   # h
print(s[1])   # e
print(s[-1])  # o (last element)
```

---

## 🧠 DSA Insight

👉 Index = control
👉 Most string problems = **index manipulation**

---

## 🔁 Traversal

```python
for i in range(len(s)):
    print(s[i])
```

or

```python
for ch in s:
    print(ch)
```

---

# 🔥 3. Immutability (CRITICAL CONCEPT)

```python
s = "hello"
s[0] = 'H'   # ❌ ERROR
```

👉 Strings **cannot be changed in-place**

---

## 🧠 Why this matters in DSA

Instead of modifying:

```python
# WRONG
s[i] = 'x'
```

👉 You must create a new string:

```python
s = s[:i] + 'x' + s[i+1:]
```

---

## 💡 DSA Optimization Trick

👉 Convert string → list

```python
s = "hello"
lst = list(s)

lst[0] = 'H'

s = "".join(lst)
print(s)
```

---

# ✂️ 4. Slicing (POWER TOOL)

```python
s = "hello"

print(s[1:4])   # "ell"
print(s[:3])    # "hel"
print(s[::-1])  # reverse
```

---

## 🧠 DSA Usage

* Reverse string
* Substrings
* Sliding window

---

# 🔁 5. String Operations

---

## ➕ Concatenation

```python
s = "hello" + " world"
```

👉 Used in building results

---

## 🔍 Membership

```python
if "he" in s:
    print("Found")
```

---

## 📏 Length

```python
len(s)
```

---

# 🔥 6. Core DSA Problems Using Strings

---

# 🔁 1. Palindrome

👉 Same forward & backward

```python
s = "madam"

if s == s[::-1]:
    print("Palindrome")
```

---

## 🧠 DSA Thinking

* Compare with reverse
* Or use two pointers

```python
i, j = 0, len(s)-1

while i < j:
    if s[i] != s[j]:
        print("Not palindrome")
        break
    i += 1
    j -= 1
```

---

# 🔤 2. Anagram

👉 Same characters, different order

```python
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
```

---

## 🧠 Better Approach (Frequency)

```python
from collections import Counter

if Counter(s1) == Counter(s2):
    print("Anagram")
```

---

# 🔢 3. Character Frequency

```python
s = "banana"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
```

---

# 🧠 Used in:

* Anagrams
* Hashing
* Pattern matching

---

# 🔥 4. Sliding Window (ADVANCED)

```python
s = "abcabcbb"

seen = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    
    seen.add(s[right])
    max_len = max(max_len, right - left + 1)

print(max_len)
```

👉 Longest substring without repeating characters

---

# ⚠️ 7. Performance Insight

❌ Bad:

```python
res = ""
for ch in s:
    res += ch   # slow (creates new string every time)
```

✅ Better:

```python
res = []
for ch in s:
    res.append(ch)

res = "".join(res)
```

---

# 🧠 8. Build Your DSA Approach

When you see string problem, ask:

---

### 🧩 Step 1: Is it about order?

👉 Use indices / two pointers

---

### 🧩 Step 2: Is it about frequency?

👉 Use dictionary / Counter

---

### 🧩 Step 3: Is it substring?

👉 Use sliding window

---

### 🧩 Step 4: Need modification?

👉 Convert to list

---

# 🚀 Final Mindset

Don’t think:

> “String = text”

Think:

> “String = sequence I can control using indices”

---

## 🔥 Cheat Code

* String = array of characters
* Index = power
* Slice = shortcut
* Dict = frequency
* Set = uniqueness

---

