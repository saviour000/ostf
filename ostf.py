"""
Python Practical Lab Manual with Solutions
"""

# =========================
# ✅ List Operations
# =========================

# Program 1: Create and Display Elements of a List
print("\n--- Program 1: Create and Display Elements of a List ---")
my_list = [10, 20, 30, 40, 50]
print("The list is:", my_list)

# Program 2: Add, Update, and Remove Elements from a List
print("\n--- Program 2: Add, Update, and Remove Elements from a List ---")
my_list = [1, 2, 3]
my_list.append(4)  # Add
my_list[1] = 20    # Update index 1
my_list.remove(3)  # Remove element 3
print("Updated list:", my_list)

# Program 3: Sort a List in Ascending and Descending Order
print("\n--- Program 3: Sort a List in Ascending and Descending Order ---")
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)

# Program 4: Find the Maximum and Minimum Element in a List
print("\n--- Program 4: Find the Maximum and Minimum Element in a List ---")
numbers = [10, 25, 5, 75, 30]
print("Max:", max(numbers))
print("Min:", min(numbers))

# Program 5: Count Frequency of Each Element in a List
print("\n--- Program 5: Count Frequency of Each Element in a List ---")
items = [1, 2, 2, 3, 3, 3, 4]
frequency = {}
for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print("Frequency of elements:", frequency)

# Program 6: Remove Duplicates from a List
print("\n--- Program 6: Remove Duplicates from a List ---")
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print("List without duplicates:", unique_list)

# Program 7: Find the Sum and Average of List Elements
print("\n--- Program 7: Find the Sum and Average of List Elements ---")
numbers = [10, 20, 30, 40]
total = sum(numbers)
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)

# Program 8: Merge Two Lists into One
print("\n--- Program 8: Merge Two Lists into One ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print("Merged list:", merged)

# Program 9: Search an Element in a List
print("\n--- Program 9: Search an Element in a List ---")
my_list = [10, 20, 30, 40, 50]
element = 30
if element in my_list:
    print(f"{element} found at index {my_list.index(element)}")
else:
    print(f"{element} not found")


# =========================
# ✅ Tuple Operations
# =========================

# Program 10: Create and Display a Tuple
print("\n--- Program 10: Create and Display a Tuple ---")
my_tuple = (10, 20, 30)
print("Tuple elements:", my_tuple)

# Program 11: Access Elements Using Indexing
print("\n--- Program 11: Access Elements Using Indexing ---")
my_tuple = (5, 10, 15, 20)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Program 12: Slice a Tuple
print("\n--- Program 12: Slice a Tuple ---")
my_tuple = (1, 2, 3, 4, 5)
print("Sliced Tuple (index 1 to 3):", my_tuple[1:4])

# Program 13: Find the Length, Max, and Min in a Tuple
print("\n--- Program 13: Find the Length, Max, and Min in a Tuple ---")
my_tuple = (8, 2, 10, 4)
print("Length:", len(my_tuple))
print("Max:", max(my_tuple))
print("Min:", min(my_tuple))

# Program 14: Convert List to Tuple and Vice Versa
print("\n--- Program 14: Convert List to Tuple and Vice Versa ---")
list1 = [1, 2, 3]
tuple1 = tuple(list1)
print("Tuple:", tuple1)
new_list = list(tuple1)
print("List again:", new_list)


# =========================
# ✅ Dictionary Operations
# =========================

# Program 15: Create and Display a Dictionary
print("\n--- Program 15: Create and Display a Dictionary ---")
student = {"name": "Alice", "age": 20, "grade": "A"}
print("Student Dictionary:", student)

# Program 16: Add, Update, and Delete Dictionary Elements
print("\n--- Program 16: Add, Update, and Delete Dictionary Elements ---")
student = {"name": "Bob"}
student["age"] = 21  # Add
student["name"] = "Robert"  # Update
del student["age"]  # Delete
print("Updated dictionary:", student)

# Program 17: Access Dictionary Values Using Keys
print("\n--- Program 17: Access Dictionary Values Using Keys ---")
person = {"name": "John", "city": "New York"}
print("Name:", person.get("name"))
print("City:", person["city"])

# Program 18: Iterate Through a Dictionary
print("\n--- Program 18: Iterate Through a Dictionary ---")
fruits = {"apple": 2, "banana": 3, "cherry": 5}
for key, value in fruits.items():
    print(key, ":", value)

# Program 19: Merge Two Dictionaries
print("\n--- Program 19: Merge Two Dictionaries ---")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print("Merged Dictionary:", merged)


# =========================
# ✅ Basic Logic and Number Programs
# =========================

# Program 20: Check if a Number is Palindrome
print("\n--- Program 20: Check if a Number is Palindrome ---")
num = 121
if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Program 21: Reverse a Number
print("\n--- Program 21: Reverse a Number ---")
num = 1234
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed Number:", rev)

# Program 22: Check Prime Number
print("\n--- Program 22: Check Prime Number ---")
num = 7
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# Program 23: Generate Fibonacci Series
print("\n--- Program 23: Generate Fibonacci Series ---")
n = 10
a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# Program 24: Factorial Using Loop
print("\n--- Program 24: Factorial Using Loop ---")
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)

# Program 25: Check Armstrong Number
print("\n--- Program 25: Check Armstrong Number ---")
num = 153
_sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    _sum += digit ** 3
    temp //= 10
if num == _sum:
    print("Armstrong Number")
else:
    print("Not Armstrong")

# Program 26: Count Vowels in a String
print("\n--- Program 26: Count Vowels in a String ---")
string = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for ch in string if ch in vowels)
print("Vowel Count:", count)

# Program 27: Find the Largest Element in a List Without max()
print("\n--- Program 27: Find the Largest Element in a List Without max() ---")
numbers = [10, 25, 5, 75, 30]
largest = numbers[0]
for num in numbers[1:]:
    if num > largest:
        largest = num
print("Largest element:", largest)

# Program 28: Find Common Elements Between Two Lists
print("\n--- Program 28: Find Common Elements Between Two Lists ---")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print("Common Elements:", common)

# Program 29: Find Even and Odd Numbers in a List
print("\n--- Program 29: Find Even and Odd Numbers in a List ---")
numbers = [1, 2, 3, 4, 5, 6]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]
print("Even:", even)
print("Odd:", odd)

# Program 30: Count Positive, Negative, and Zero in a List
print("\n--- Program 30: Count Positive, Negative, and Zero in a List ---")
nums = [0, -1, 2, -3, 4, 0]
pos = neg = zero = 0
for num in nums:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)
