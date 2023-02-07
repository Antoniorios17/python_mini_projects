calculation_of_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_of_units} {name_of_unit}"
    elif num_of_days == 0:
        return "0 is not a valid number\nPlease enter a valid positive number"
    else:
        return "You enter a negative value\nNo conversion for you"


user_input=input("Hello \n\nEnter a number of days\nI wil convert it to hours\n--> ")

calculated_value = days_to_units(int(user_input))
print(calculated_value)
