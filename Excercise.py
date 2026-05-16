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
            