# 1 tuple
my_tuple = (11, 22, 33, 44, 55, 66)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Length of tuple:", len(my_tuple))
print("Elements from index 1 to 3:", my_tuple[1:4])

# 2  tuple
fruits = ("apple", "banana", "mango", "orange", "grape")
print("Second fruit:", fruits[1])
print("Last two fruits:", fruits[-2:])
print("Total number of fruits:", len(fruits))

# 3  set
numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
print("Complete set:", numbers)
print("Length of set:", len(numbers))
print("Is 30 present?", 30 in numbers)

# 4 two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

#  5   dictionary
student = {
    "name": "Balkishan Sharma",
    "age": 20,
    "course": "Python"
}
print("Complete dictionary:", student)
print("Student name:", student["name"])
print("Student age:", student["age"])
print("Student course:", student["course"])


numbers = [12, 45, 7, 23, 56, 89, 34, 78, 90, 11]
largest = max(numbers)
smallest = min(numbers)
numbers.sort()
second_largest = numbers[-2]
print("Largest element:", largest)
print("Second largest element:", second_largest)
print("Smallest element:", smallest)


#  6   reverse() method. 
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def reverse_list(lst):
    return lst[::-1]
print("Original List:", arr)
print("Reversed List:", reverse_list(arr))


# 7   tuple
data = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
count = 0
for num in data:
    if num % 5 == 0:
        count += 1
total = sum(data)
average = total / len(data)
print("Count divisible by 5:", count)
print("Sum:", total)
print("Average:", average)


#    8    dictionary: 
students = {
    "Aman": 78,
    "Riya": 92,
    "Ankita": 88,
    "Balkishan": 95
}
highest = max(students, key=students.get)
lowest = min(students, key=students.get)
print("Highest Marks:", highest, "-", students[highest])
print("Lowest Marks:", lowest, "-", students[lowest])
print("\nStudents scoring more than 85 marks:")
for name, marks in students.items():
    if marks > 85:
        print(name, ":", marks)
        
        
#   9   count_frequency(arr) 
def count_frequency(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        if value == 1:
            print(f"{key} -> {value} time")
        else:
            print(f"{key} -> {value} times")
arr = [1, 2, 2, 3, 1, 4, 2]
count_frequency(arr)     

  
        
# 10  find_duplicates(arr) 
def find_duplicates(arr):
    duplicates = set()
    seen = set()

    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    print("Duplicate elements are:")
    for item in duplicates:
        print(item)


arr = [10, 20, 30, 20, 40, 10, 50, 30]
find_duplicates(arr)