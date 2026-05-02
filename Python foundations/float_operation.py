# ============================================
# PYTHON FLOAT - COMPLETE DSA PLAYGROUND 🚀
# ============================================

# -------------------------------
# 1. BASIC FLOAT & TYPE
# -------------------------------

print("=== BASIC FLOAT ===")

x = 3.14
y = 1e-9   # scientific notation

print("x:", x)
print("y (1e-9):", y)
print("Type of x:", type(x))


# -------------------------------
# 2. FLOAT PRECISION ISSUE
# -------------------------------

print("\n=== PRECISION ISSUE ===")

a = 0.1
b = 0.2

c = a + b

print("0.1 + 0.2 =", c)  # not exactly 0.3
print("Is equal to 0.3?", c == 0.3)  # False


# -------------------------------
# 3. SAFE FLOAT COMPARISON (EPS)
# -------------------------------

print("\n=== SAFE COMPARISON ===")

EPS = 1e-9

if abs(c - 0.3) < EPS:
    print("c is approximately equal to 0.3")
else:
    print("c is NOT equal to 0.3")

# DSA Insight:
# Always use tolerance for float comparison


# -------------------------------
# 4. FLOAT OPERATIONS
# -------------------------------

print("\n=== FLOAT OPERATIONS ===")

x = 5.5
y = 2.2

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Power:", x ** 2)


# -------------------------------
# 5. AVERAGE (COMMON DSA USE)
# -------------------------------

print("\n=== AVERAGE ===")

arr = [1, 2, 3, 4, 5]

avg = sum(arr) / len(arr)

print("Average:", avg)


# -------------------------------
# 6. GEOMETRY (DISTANCE)
# -------------------------------

print("\n=== DISTANCE ===")

import math

x1, y1 = 0, 0
x2, y2 = 3, 4

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance:", distance)


# -------------------------------
# 7. BINARY SEARCH ON FLOAT
# -------------------------------

print("\n=== FLOAT BINARY SEARCH (SQRT) ===")

# Find sqrt of 2 using binary search
low = 0.0
high = 2.0

for _ in range(100):   # iterations for precision
    mid = (low + high) / 2
    
    if mid * mid < 2:
        low = mid
    else:
        high = mid

print("Approx sqrt(2):", mid)


# -------------------------------
# 8. LOOP TERMINATION USING FLOAT
# -------------------------------

print("\n=== LOOP WITH EPS ===")

low = 0.0
high = 1.0

while high - low > EPS:
    mid = (low + high) / 2
    if mid < 0.5:
        low = mid
    else:
        high = mid

print("Final mid:", mid)


# -------------------------------
# 9. PROBABILITY EXAMPLE
# -------------------------------

print("\n=== PROBABILITY ===")

favorable = 3
total = 10

probability = favorable / total

print("Probability:", probability)


# -------------------------------
# 10. FLOAT FORMATTING
# -------------------------------

print("\n=== FLOAT FORMATTING ===")

num = 1e-9

print("Default:", num)
print("Formatted:", f"{num:.10f}")


# -------------------------------
# 11. COMBINED MINI DSA PROBLEM
# -------------------------------

print("\n=== MINI DSA PROBLEM ===")

# Find average distance from origin

points = [(1, 2), (3, 4), (5, 6)]

total_dist = 0.0

for x, y in points:
    dist = math.sqrt(x*x + y*y)
    total_dist += dist

avg_dist = total_dist / len(points)

print("Average distance:", avg_dist)


# ============================================
# FINAL DSA THINKING SUMMARY
# ============================================

# float is used for:
# ✔ Averages → sum / n
# ✔ Geometry → distance
# ✔ Binary search (continuous values)
# ✔ Probabilities → ratios
# ✔ Approximation problems

# Avoid float when:
# ❌ exact comparison needed
# ❌ counting / indexing
# ❌ money calculations

print("\n=== END OF FLOAT PLAYGROUND 🚀 ===")