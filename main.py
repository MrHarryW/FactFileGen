print("Let's create a fact file on you! - This information may not be 100% accurate due to estimates.")
firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
age = int(input("Please enter your current age: "))
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
weeks = age * 52
decades = age//10
centuries = age//100
months = age * 12
milliseconds = seconds * 1000
microseconds = milliseconds * 1000
nanoseconds = microseconds * 1000
​
print("\n\n"+lastname.capitalize()+",", firstname.capitalize())
print("This is a fact file on",lastname.capitalize()+",", firstname.capitalize()+"\n")
print("NAME:")
print("First Name:", firstname.capitalize())
print("Last Name:", lastname.capitalize()+"\n")
print("AGE:")
print("Centuries Old:", centuries
print("Decades Old:", decades)
print("Years Old:", age)
print("Months Old:", months)
print("Weeks Old:", weeks)
print("Days Old:", days)
print("Hours Old:", hours)
print("Minutes Old:", minutes)
print("Seconds Old:", seconds)
print("Milliseconds Old:", milliseconds)
print("Microseconds Old:", microseconds)
print("Nanoseconds Old:", nanoseconds)
