## Python program to calculate the Sum of even numbers from 1 to 100:

def sum_of_even_numbers(minimum, maximum):
    total = 0 
    for number in range(minimum, maximum + 1):
        if number % 2 == 0:
            total += number 

    print(f"The sum of even numbers from {minimum} to {maximum} is: {total}")


minimum = 1
maximum = 100

sum_of_even_numbers(minimum, maximum)


## Write python progrom to convert list of dictionaries

colour_name = ['Black', 'White', 'Red', 'Green', 'Blue']
color_code = ['#000000', '#FFFFFF', '#FF0000', '#008000', '#0000FF']

new = []
for i, j in zip(colour_name, color_code):
    d = {'color_name': i, 'color_code': j}
    new.append(d)

print(new)

    #solution 2: 

    # new = []

    # for index in range(len(colour_name)):
    #     color_dict = {
    #         'color_name': colour_name[index],
    #         'color_code': color_code[index]
    #     }
    #     new.append(color_dict)

    # print(new)


##group the list a = ['1', '2', '3', '4'] into pairs of consecutive elements

a = ['1', '2', '3', '4']
#o/p = ['12', '34']

b = list(zip(a[::2], a[1::2]))
print(b)

d = []
for i in b:
    c = ''.join(i)
    d.append(c)

print(d)

    # a = ['1', '2', '3', '4']
    # result = []

    # for i in range(0, len(a), 2):
    #     result.append(a[i] + a[i+1])

    # print(result)


# with open('INTERVIEW/Python/myinterview.py', 'w') as file:
#     data = file.readlines()
#     for line in data:
#         if 'a' in line:
#             print(line.strip())
#             matched_str = i 
#             print(f"Matched string: {matched_str}")



#o/p = ['hello care', 'hello sir', 'take care', 'take sir']
#create all combinations of elements from two lists a and b,
#where each element from a is combined with each element from b
a = ['hello', 'take']
b = ['care', 'sir']

result = []
for i in a:
    for j in b:
        result.append(i+' ' + j)
        #result = [i + ' ' + j for i in a for j in b]
print(result)


# Pair elements in the list as tuple
# then filter only the tuples where the sum of the two numbers in 10
#o/p = [(2,8), (9,1),(5,5)]
ls = [2,4,3,1,6,5,9,8,7,5]

result = []
for i in range(0, len(ls), 2):
    pair = (ls[i], ls[i+1])
    if pair[0] + pair[1] == 10:
        result.append(pair)

    # Step 1: Group into pairs
    #pairs = [(ls[i], ls[i+1]) for i in range(0, len(ls), 2)]
    # Step 2: Filter pairs where sum == 10
    #result = [pair for pair in pairs if sum(pair) == 10]

print(result)

# python proram to find all possible pairs with given sum 
# Input list and target sum
nums = [2, 4, 3, 1, 6, 5, 9, 8, 7, 5]
target_sum = 10

result = []

# Check all pairs (i, j) where i < j
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target_sum:
            result.append((nums[i], nums[j]))

print(f"Pairs with sum {target_sum}: {result}")

a = "python online compiler"
b = " "
#o/p = ['p', 'o', 'c']

words = a.split(b)
result = []
for word in words:
    result.append(word[0])
print(result)


#write a class name "Ayalyzer", that takes a list of strings as a 
#parameter in the constructor, in the class, define a method named "Analyze"

#that returns the following details as dictionary:
#1. The number of ites in the list 
#2. The number of palindromes (case insensitive) in the list 
#3. The palindromes (Original words) as list 

class Ayalyzer:
    def __init__(self, words):
        self.words = words

    def Analyze(self):
        total_items = len(self.words)
        palindromes = []

        for word in self.words:
            lower_word = word.lower()
            if lower_word == lower_word[::-1]:
                palindromes.append(word)  # Keep original word

        return {
            "total_items": total_items,
            "num_palindromes": len(palindromes),
            "palindromes": palindromes
        }

# Example usage
words = ["madam", "hello", "Racecar", "world", "noon"]
analyzer = Ayalyzer(words)
result = analyzer.Analyze()

print(result)

#find firt largest number in the list
#o/p = 90

a = [20,60,90,10]
b = 0 
for i in a:
    if i > b:
        b = i 

print(f"The largest number in the list is: {b}")

#find second largest number in the list
#o/p = 60
a = [20, 60, 90, 10]
b = 0
c = 0
for i in a:
    if i > b:
        c = b
        b = i
    elif i > c and i != b:
        c = i
print(f"The second largest number in the list is: {c}")