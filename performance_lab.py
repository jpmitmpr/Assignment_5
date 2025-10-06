# 1️ Find Most Frequent Element
# The time complexity for this function is O(n) in all cases since it has to go through every element in the list. The space complexity is also O(n) because it stores each unique element and its count. I used the Counter class since it’s simple, fast, and easy to understand. You could make it a bit more efficient by using a regular dictionary, but that would make the code less clean and harder to read.
from collections import Counter

def find_most_frequent(lst):
    if not lst:
        return None
    counts = Counter(lst)
    return max(counts, key=counts.get)

# Test Cases
test1 = [1, 2, 2, 3, 3, 3]
test2 = []
test3 = [7]
test4 = [1, 1, 2]

assert find_most_frequent(test1) == 3
assert find_most_frequent(test2) is None
assert find_most_frequent(test3) == 7
assert find_most_frequent(test4) in [1, 2]

print("Most Frequent Element Tests:")
print(find_most_frequent(test1))  # 3
print(find_most_frequent(test2))  # None
print(find_most_frequent(test3))  # 7
print(find_most_frequent(test4))  # 1 o 2
print("--------------------------------------")

# 2️ Remove Duplicates While Preserving Order
# The time complexity of this function is O(n) since it loops through the list once, and checking items in a set is really fast. The space complexity is also O(n) because it keeps track of the seen elements and the final list without duplicates. I used this approach because it’s simple and keeps the original order of the list. You could use other methods like an OrderedDict, but this one is cleaner and works just as well.
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

test5 = [1, 2, 2, 3, 1]
test6 = []
test7 = [5, 5, 5]
test8 = ["a", "b", "a"]

assert remove_duplicates(test5) == [1, 2, 3]
assert remove_duplicates(test6) == []
assert remove_duplicates(test7) == [5]
assert remove_duplicates(test8) == ["a", "b"]

print("Remove Duplicates Tests:")
print(remove_duplicates(test5))  # [1, 2, 3]
print(remove_duplicates(test6))  # []
print(remove_duplicates(test7))  # [5]
print(remove_duplicates(test8))  # ["a", "b"]
print("--------------------------------------")

# 3️ Return All Pairs That Sum to Target
# The time complexity of this function is O(n) because it only loops through the list once, and checking values in a set is really fast. The space complexity is also O(n) since it keeps track of the numbers we’ve seen and the pairs we find. I used this approach because it’s quick, simple, and avoids duplicate pairs. You could sort the list and use two pointers instead, but that would take more time and make the code less straightforward.
def find_pairs(lst, target):
    seen = set()
    pairs = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)

test9 = [1, 2, 3, 4, 5]
target1 = 5
test10 = []
target2 = 10
test11 = [2, 2, 3, 3]
target3 = 5
test12 = [1, 1, 1, 1]
target4 = 2

assert sorted(find_pairs(test9, target1)) == [(1, 4), (2, 3)]
assert find_pairs(test10, target2) == []
assert sorted(find_pairs(test11, target3)) == [(2, 3)]
assert find_pairs(test12, target4) == [(1, 1)]

print("Find Pairs Tests:")
print(find_pairs(test9, target1))  # [(1, 4), (2, 3)]
print(find_pairs(test10, target2))  # []
print(find_pairs(test11, target3))  # [(2, 3)]
print(find_pairs(test12, target4))  # [(1, 1)]
print("--------------------------------------")

# 4️ Simulate List Resizing
# The average time complexity of this function is O(1) because most inserts are fast, though resizing occasionally takes longer at O(n). The space complexity is O(1) since it only uses a few variables to track the list’s size and capacity. I used this approach because it mimics how real dynamic arrays grow in memory, doubling when needed. You could make it grow by smaller amounts, but that would mean more resizing and slower performance overall.
def simulate_list_resizing(operations):
    capacity = 1
    size = 0
    resizes = 0
    for _ in range(operations):
        if size == capacity:
            capacity *= 2
            resizes += 1
        size += 1
    return {"final_capacity": capacity, "resizes": resizes}

test13 = 10
test14 = 1
test15 = 16

assert simulate_list_resizing(test13)["final_capacity"] >= 10
assert simulate_list_resizing(test14)["resizes"] == 0
assert simulate_list_resizing(test15)["resizes"] == 4

print("Simulate List Resizing Tests:")
print(simulate_list_resizing(test13))  # {'final_capacity': >=10, 'resizes': ?}
print(simulate_list_resizing(test14))  # {'final_capacity': 1, 'resizes': 0}
print(simulate_list_resizing(test15))  # {'final_capacity': 16, 'resizes': 4}
print("--------------------------------------")

# 5️ Compute Running Totals
# The time complexity of this function is O(n) because it goes through the list once, adding each number to a running total. The space complexity is also O(n) since it creates a new list to store the cumulative sums. I used this approach because it’s simple and easy to understand while efficiently calculating totals in one pass. You could make it update the list in place to save memory, but that would overwrite the original data.
def running_totals(lst):
    total = 0
    result = []
    for num in lst:
        total += num
        result.append(total)
    return result

test16 = [1, 2, 3]
test17 = []
test18 = [5]
test19 = [1, -1, 1, -1]

assert running_totals(test16) == [1, 3, 6]
assert running_totals(test17) == []
assert running_totals(test18) == [5]
assert running_totals(test19) == [1, 0, 1, 0]

print("Running Totals Tests:")
print(running_totals(test16))  # [1, 3, 6]
print(running_totals(test17))  # []
print(running_totals(test18))  # [5]
print(running_totals(test19))  # [1, 0, 1, 0]
print("--------------------------------------")

# Optimize One (Refactoriza una de tus soluciones)

def find_most_frequent_optimized(lst):
    if not lst:
        return None
    freq = {}
    most = lst[0]
    max_count = 0
    for x in lst:
        freq[x] = freq.get(x, 0) + 1
        if freq[x] > max_count:
            max_count = freq[x]
            most = x
    return most

assert find_most_frequent_optimized(test1) == 3
assert find_most_frequent_optimized(test2) is None
assert find_most_frequent_optimized(test3) == 7

print("Optimized Most Frequent Tests:")
print(find_most_frequent_optimized(test1))  # 3
print(find_most_frequent_optimized(test2))  # None
print(find_most_frequent_optimized(test3))  # 7
print("--------------------------------------")
