# ==============================
# PYTHON VARIABLES & DATA TYPES
# (DSA FOUNDATION MASTER FILE)
# ==============================

print("🔹 VARIABLES & MEMORY DEMO\n")

# Variable assignment
x = 10
y = 10

print("x =", x)
print("y =", y)

# Memory check
print("Memory ID of x:", id(x))
print("Memory ID of y:", id(y))  # Often same (optimization)

# Changing value
x = 20
print("\nAfter changing x:")
print("x =", x)
print("New Memory ID of x:", id(x))


# ==============================
# DATA TYPES
# ==============================

print("\n🔹 DATA TYPES DEMO\n")

# Integer
a = 100
print("a =", a, "| Type:", type(a))

# Float
b = 3.14
print("b =", b, "| Type:", type(b))

# String
c = "nikshith"
print("c =", c, "| Type:", type(c))

# Boolean
d = True
print("d =", d, "| Type:", type(d))


# ==============================
# TYPE CASTING
# ==============================

print("\n🔹 TYPE CASTING DEMO\n")

# float → int
f = 3.9
print("Original float:", f)
print("After int():", int(f))

# int → float
i = 5
print("Original int:", i)
print("After float():", float(i))

# int → string
num = 100
print("Original int:", num)
print("After str():", str(num), "| Type:", type(str(num)))

# string → int
s = "50"
print("String:", s)
print("After int():", int(s))

# bool conversions
print("\nBoolean conversions:")
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(''):", bool(""))
print("bool('hello'):", bool("hello"))


# ==============================
# IMMUTABILITY DEMO
# ==============================

print("\n🔹 IMMUTABILITY DEMO\n")

p = 10
q = p

print("p =", p, "| ID:", id(p))
print("q =", q, "| ID:", id(q))

p = 50  # new object created

print("\nAfter changing p:")
print("p =", p, "| ID:", id(p))
print("q =", q, "| ID:", id(q))  # remains unchanged


# ==============================
# DSA STYLE EXAMPLES
# ==============================

print("\n🔹 DSA EXAMPLES\n")

# Example 1: Counting
count = 0
for i in range(5):
    count += 1
print("Count result:", count)


# Example 2: String traversal
s = "nikshith"
print("\nCharacters in string:")
for ch in s:
    print(ch)


# Example 3: Boolean flag (search)
arr = [1, 2, 3, 4]
found = False

for x in arr:
    if x == 3:
        found = True

print("\nIs 3 found?", found)


# Example 4: Input handling (uncomment to test)
# n = int(input("\nEnter a number: "))
# print("You entered:", n, "| Type:", type(n))


# ==============================
# FINAL SUMMARY PRINT
# ==============================

print("\n🔹 SUMMARY")
print("Variables → references to memory")
print("int → whole numbers")
print("float → decimals")
print("str → text")
print("bool → True/False")
print("type() → check type")
print("Casting → convert types")
print("Immutable → new object created on change")