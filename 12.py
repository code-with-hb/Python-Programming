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

#Inerting Elements into a list.
#______________________________________________________________
#we can add a new element at any postion in our list by using the insert() method.
#We do this by specifying the index of the new element and the value of the new item.
bike = ['hero', ' yamaha', 'Suzuki']
bike.insert(0, 'Ducati')
print(bike)

#Removing Elements from a list
#______________________________________________________________
#If we know the position of the item we want to remove from a list, we can use the del statement.
bike = ['hero', ' yamaha', 'Suzuki']
del bike[1]
print(bike)
#Removing items using the pop() Method
bike = ['hero', ' yamaha', 'Suzuki']
popped_bike = bike.pop()
print(bike)
print(popped_bike)