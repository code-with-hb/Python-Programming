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
                                