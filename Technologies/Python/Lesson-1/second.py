calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days):
    return (f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}")    

user_input = input("Hey user! \nEnter a number of days: ")
user_input_number = int(user_input)
calculated_values = days_to_units(user_input_number)

print(calculated_values)
