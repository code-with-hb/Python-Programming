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