fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
print(fruits)
#2
print(fruits.count('tangerine'))

#0
fruits.index('banana')
#3
fruits.index('banana', 4)  # Find next banana starting at position 4
#6
fruits.reverse()
#fruits
#['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
#fruits
#['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
#fruits
#['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
print(fruits.pop())
#'pear'