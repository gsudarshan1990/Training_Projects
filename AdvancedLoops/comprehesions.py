"""
This is an example of the comprehension
"""

num = range(10)
print([x*x for x in num])

letters = [letter for letter in 'anxiety']
print(letters)

list_of_words  = ['this','is','a','list','of','words']
first_words = [word[0] for word in list_of_words]
print(first_words)

upper_fist_words  = [word[0].upper() for word in list_of_words]
upper_words = [word.upper() for word in list_of_words]
print(upper_fist_words)
print(upper_words)

odd_squares = [x*x for x in num if x%2 !=0]
print(odd_squares)
even_numbers = [x for x in range(20) if x%2 == 0]
print(even_numbers)

multiples_15 = [x for x in range(200) if x%15 == 0]
print(multiples_15)

vowel_from_word = [i for i in 'MATHEMATICS' if i in ['A','E','I','O','U']]
print(vowel_from_word)

string1 = 'Hello 12345 Hello'
numbers = [x for x in string1 if x.isdigit()]
print(numbers)

stationary =['Pen','Marker','Geometry box']
colors =['Red','blue','Pink']

combined = [(i,j) for i in stationary for j in colors]
print(combined)

number_divisible_2_5 = [i for i in range(50) if i%2 == 0 if i%5 ==0]
print(number_divisible_2_5)

odd_list =[]
even_list =[]
[odd_list.append(i) if i%2 !=0 else even_list.append(i) for i in range(20)]
print(odd_list)
print(even_list)

numbers3 = [22,30,45,50,18,69,43,44,12]
numbers4 = [x+1 if x > 45 else x+5 for x in numbers3 ]
print(numbers4)

number5 = ['small' if num < 20 else 'large' for num in numbers3 if num%2 == 0 if num%3 ==0]
print(number5)