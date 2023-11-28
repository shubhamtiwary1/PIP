greeting = "Good Morning. Have a Good Day!!"
print(greeting.count('Good'))#2
print(greeting.find('a'))
print(greeting.rfind('a')) #returns highest value of a value here = index.
print(greeting.capitalize())
print(greeting.lower())
print(greeting.upper())
print(greeting.swapcase())
print(greeting.istitle())
print(greeting.replace('Good', 'Sweet'))
print(greeting.strip())
print(greeting.split())
print(greeting.partition('.'))
print(greeting.startswith('good'))
print(greeting.endswith('!!'))
print()



# Example 1
str1 = "   Hello   "
result1 = str1.strip()
print("'" + result1 + "'")  # Output: 'Hello'

# Example 2
str2 = "\t\t\tPython\t\t\t"
result2 = str2.strip()
print("'" + result2 + "'")  # Output: 'Python'

# Example 3
str3 = "\n\n\nHello World\n\n\n"
result3 = str3.strip()
print("'" + result3 + "'")  # Output: 'Hello World'

# Example 4
str4 = "  Python Programming   "
result4 = str4.strip(' Pgrm')
print("'" + result4 + "'")  # Output: 'ython Pro'
