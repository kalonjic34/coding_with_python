print("fast" in "breakfast")
print("fast" in "dinner")
print()

meals = ["breakfest", "lunch", "dinner"]

print("lunch" in meals)
print("dinner" in meals)
print("snack" in meals)
print("Breakfest" in meals)

print()

test_scores = [99.0, 35.0, 23.5]
print(99.0 in test_scores)
print(99 in test_scores)
print(28 in test_scores)
print()

print("lunch" not in meals)
print("Breakfest" not in meals)
print(1000 not in test_scores)

if 1000 not in test_scores:
    print("That value is not in there!!")
