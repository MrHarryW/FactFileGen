import matplotlib.pyplot as plt

print("Let's create a fact file on you! - This information may not be 100% accurate due to estimates.")

firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
age = int(input("Please enter your current age: "))


days = age * 365
weeks = age * 52
months = age * 12
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
milliseconds = seconds * 1000
microseconds = milliseconds * 1000
nanoseconds = microseconds * 1000
decades = age // 10
centuries = age // 100


print("\n\n" + lastname.capitalize() + ",", firstname.capitalize())
print("This is a fact file on", lastname.capitalize() + ",", firstname.capitalize() + "\n")
print("NAME:")
print("First Name:", firstname.capitalize())
print("Last Name:", lastname.capitalize(), "\n")
print("AGE:")
print("Centuries Old:", centuries)
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


time_labels = ["Centuries","Decades", "Years", "Months", "Weeks", "Days", "Hours", "Minutes", "Seconds", "Milliseconds", "Microseconds", "Nanoseconds"]
time_values = [centuries, decades, age, months, weeks, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds]

plt.figure(figsize=(10, 5))
plt.barh(time_labels, time_values, color=['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta', 'pink', 'yellow', 'grey', 'black', 'turquoise'])
plt.xlabel("Time Units")
plt.ylabel("Amount")
plt.title(f"Age of {firstname.capitalize()} {lastname.capitalize()} in Different Units")
plt.gca().invert_yaxis() 
plt.show()
