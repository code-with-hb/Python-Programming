#ORGANIZING A LIST
#1. Soriting a list permanently with sort method
#python sort method makes it relatively easy to sort a list.
#it helps to orgainize a list in alphabetical oreder.
cars = ['bmw','audi','tata','mahindra']
cars.sort()
print(cars)

#we can sort a list in reverse alphabetical order by passing the argument reverse=True to the sort() method.
cars = ['bmw','audi','tata','mahindra']
cars.sort(reverse=True)     
print(cars)

#2. Sorting a list temporarily with sorted() functions
#the sorted() display our list in particular order doesn't affect the actual order of the list.
cars = ['bmw', 'audi', 'toyota', 'mahindra']
print("This is the original cars list:")
print(cars)
print("This is the sorted list:")
print(sorted(cars))
print("This is the original cars list again:")
print(cars)
#The sorted function can also accept a reverse = True argument if we want to sort a list in reverse alphabetical order
print("This is the reverse car list")
print(sorted(cars, reverse= True))