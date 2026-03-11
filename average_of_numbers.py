# Collects numbers, makes list

def collect_numbers(total_numbers):
    print("Please enter", total_numbers, "numbers: ")
    for i in range(0, total_numbers):
        ele = float(input())
        my_list.append(ele)


# Calculates average

def calculate_average():
    total = 0
    for i in range(0, len(my_list)):
        total = total + my_list[i]
    return (total/total_numbers)

my_list = []

total_numbers = int(input("Average of how many numbers? "))
collect_numbers(total_numbers)  # Calling function to create the list

average = calculate_average()  # Calling function to calculate average

print("The average is : ", average)



