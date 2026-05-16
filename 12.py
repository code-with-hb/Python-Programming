#Changing, Adding, and Removing Elemenyts
#Modifying element in a list
bike = ['Yamaha', 'Enfiled', 'Hero', 'Honda']
print(bike)
bike[0] = 'Ducati'
print(bike)
#Adding Element to a list
#appending elements to the end of a list
bike.append('Yamaha')
print(bike)
#Append method makes it easy to build list dynamically. For Example, we can start with an empty list and then add item to the list using the series of append() calls.
bike = []
bike.append('Hero')
bike.append('honda')
bike.append('Yamaha')
print(bike)