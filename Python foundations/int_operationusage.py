# ============================================
# PYTHON INT - COMPLETE DSA PLAYGROUND 🚀
# ============================================

# -------------------------------
# 1. BASIC INTEGER & MEMORY IDEA
# -------------------------------

print("=== MEMORY DEMO ===")

a = 10
b = a   # both point to same integer initially

print("a:", a, "b:", b)

b = b + 5  # NEW integer object created

print("After modifying b:")
print("a:", a, "b:", b)

# DSA Insight:
# Integers are immutable → operations create new values


# -------------------------------
# 2. ARITHMETIC OPERATIONS
# -------------------------------

print("\n=== ARITHMETIC OPERATIONS ===")

x = 10
y = 3

print("Addition (+):", x + y)        # 13 → used in sums
print("Subtraction (-):", x - y)     # 7 → used in differences
print("Multiplication (*):", x * y)  # 30 → used in products
print("Division (/):", x / y)        # float → avoid in DSA when not needed
print("Floor Division (//):", x // y) # 3 → VERY IMPORTANT (binary search)
print("Modulus (%):", x % y)         # 1 → cycles, even/odd
print("Exponent (**):", x ** y)      # 1000 → powers


# -------------------------------
# 3. COUNTERS (CORE DSA USE)
# -------------------------------

print("\n=== COUNTER PATTERN ===")

arr = [1, 2, 3, 4, 5, 6]

count = 0

for num in arr:
    count += 1   # increment counter

print("Total elements:", count)


# -------------------------------
# 4. EVEN / ODD USING MODULUS
# -------------------------------

print("\n=== EVEN COUNT ===")

even_count = 0

for num in arr:
    if num % 2 == 0:   # modulus used for condition
        even_count += 1

print("Even numbers:", even_count)


# -------------------------------
# 5. INDICES (POSITION CONTROL)
# -------------------------------

print("\n=== INDEX USAGE ===")

for i in range(len(arr)):
    print("Index:", i, "Value:", arr[i])

# DSA Insight:
# Index = control of traversal


# -------------------------------
# 6. PREFIX SUM (VERY IMPORTANT)
# -------------------------------

print("\n=== PREFIX SUM ===")

arr = [1, 2, 3, 4]

prefix = [0] * len(arr)
prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

print("Prefix array:", prefix)

# DSA Use:
# Fast range sum queries


# -------------------------------
# 7. DIFFERENCE / TWO POINTER IDEA
# -------------------------------

print("\n=== DIFFERENCE ===")

i = 0
j = len(arr) - 1

diff = arr[j] - arr[i]

print("Difference between last and first:", diff)


# -------------------------------
# 8. BINARY SEARCH MID (IMPORTANT)
# -------------------------------

print("\n=== BINARY SEARCH MID ===")

low = 0
high = 10

mid = (low + high) // 2  # floor division

print("Mid index:", mid)


# -------------------------------
# 9. PRODUCT PATTERN
# -------------------------------

print("\n=== PRODUCT ===")

product = 1

for num in arr:
    product *= num

print("Product of array:", product)


# -------------------------------
# 10. LOOP CONTROL (WHILE)
# -------------------------------

print("\n=== WHILE LOOP ===")

i = 0
n = 5

while i < n:
    print("i:", i)
    i += 1   # integer controls loop


# -------------------------------
# 11. DECISION MAKING
# -------------------------------

print("\n=== DECISION MAKING ===")

x = 10
y = 20

if x > y:
    print("x is greater")
else:
    print("y is greater")


# -------------------------------
# 12. EXPONENT USE
# -------------------------------

print("\n=== POWER ===")

n = 5
print("2^n:", 2 ** n)


# -------------------------------
# 13. MINI DSA PROBLEM COMBINED
# -------------------------------

print("\n=== MINI DSA PROBLEM ===")

# Count:
# 1. Even numbers
# 2. Sum of array
# 3. Max element

arr = [3, 8, 1, 6, 2, 9]

even_count = 0
total_sum = 0
max_val = arr[0]

for num in arr:
    total_sum += num

    if num % 2 == 0:
        even_count += 1

    if num > max_val:
        max_val = num

print("Sum:", total_sum)
print("Even count:", even_count)
print("Max value:", max_val)


# ============================================
# FINAL DSA THINKING SUMMARY
# ============================================

# int is used for:
# ✔ Counting → count += 1
# ✔ Indexing → i, j
# ✔ Conditions → %, >, <
# ✔ Math → +, -, *, //
# ✔ Optimization → prefix sums, binary search

print("\n=== END OF PLAYGROUND 🚀 ===")