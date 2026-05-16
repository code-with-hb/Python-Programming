#1. Make a list that includes at least three people you would like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
invitees = ['rabi', 'sagar', 'appa']
print(f"Dear {invitees[0].title()} you are invited to dinner.")
print(f"Dear {invitees[1].title()} you are invited to dinner.")
print(f"Dear {invitees[2].title()} you are invited to dinner.")                 

#2. You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting. Then print a second set of invitation messages, one for each person who is still in your list.
invitees = ['rabi', 'sagar', 'appa']        
print(f"Dear {invitees[0].title()} you are invited to dinner.")
print(f"Dear {invitees[1].title()} you are invited to dinner.")             
print(f"Dear {invitees[2].title()} you are invited to dinner.")
print(f"\nSorry to inform you that {invitees[0].title()} can't make it to the dinner.")
invitees[0] = 'suman'               
print(f"\nDear {invitees[0].title()} you are invited to dinner.")
print(f"Dear {invitees[1].title()} you are invited to dinner.")
print(f"Dear {invitees[2].title()} you are invited to dinner.")

#3. You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner. Add a print statement to the end of your program informing people that you found a bigger dinner table. Then use insert() to add one new guest to the beginning of your list, use insert() to add one new guest to the middle of your list, and use append() to add one new guest to the end of your list. Print a new set of invitation messages, one for each person in your list.
invitees = ['suman', 'sagar', 'appa']           
print(f"Dear {invitees[0].title()} you are invited to dinner.")
print(f"Dear {invitees[1].title()} you are invited to dinner.")
print(f"Dear {invitees[2].title()} you are invited to dinner.")
print("\nGood news! I found a bigger dinner table.")    
invitees.insert(0, 'rabi')
invitees.insert(2, 'sushil')    
invitees.append('sujan')
print(f"\nDear {invitees[0].title()} you are invited to dinner.")       
print(f"Dear {invitees[1].title()} you are invited to dinner.")
print(f"Dear {invitees[2].title()} you are invited to dinner.") 
print(f"Dear {invitees[3].title()} you are invited to dinner.")
print(f"Dear {invitees[4].title()} you are invited to dinner.")     
print(f"Dear {invitees[5].title()} you are invited to dinner.")
#4. You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests. Start with your program from Exercise 3. Add a new line that prints a message saying that you can invite only two people for dinner. Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner. Print a message to each of the two people still on your list, letting them know they're still invited. Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure it's empty.
invitees = ['rabi', 'suman', 'sushil', 'sagar', 'appa', 'sujan']
print(f"Sorry, i can invites two people for dinner.")
popped_guest = invitees.pop(0)
print(f"Sorry {popped_guest.title()}, you can't be invited to dinner.")
popped_guest = invitees.pop(1)
print(f"Sorry {popped_guest.title()}, you can't be invited to dinner.")
popped_guest = invitees.pop(2)
print(f"Sorry {popped_guest.title()}, you can't be invited to dinner.")
popped_guest = invitees.pop(2)
print(f"Sorry {popped_guest.title()}, you can't be invited to dinner.")
print(f"\nDear {invitees[0].title()} you are still invited to dinner     .")
print(f"Dear {invitees[1].title()} you are still invited to dinner.")
del invitees[0]
del invitees[0] 
print(invitees)
