#Using variable in a string
first_name = "Hemanta"
last_name = "Boro"
full_name = f"{first_name} {last_name}" #to insert a variable's value into a string, we place letter f immediately before the opening quotation mark.
#put braces around any variable to use inside a string.
print(full_name)
#we can use f-strings to compose complete message also using the information associated with variable.
print(f"Hello My name is, {full_name.upper()}")