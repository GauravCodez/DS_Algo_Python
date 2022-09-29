# Create a program to take the input from the user of the total number of days.
# Then provide the temperature for those particular days
# Find the average and display it
# Also state the number of days which had the temperature over the average temp

def average(lis):
    sum1 = 0
    for i in range(len(lis)):
        sum1 = sum1 + lis[i]
    avg = sum1 / len(lis)
    return avg


def input_temp(no_of_days):
    total = 0
    temp = []
    for i in range(no_of_days):
        g = int(input("Enter the temperature : "))
        temp.append(g)
        total = total + temp[i]
    # Calculating the average of the entered day's temp
    avg = total / no_of_days

    # Finding the days which are more than the average temperature
    count_above_avg = 0
    for i in temp:
        if i > avg:
            count_above_avg += 1

    out = [total, avg, count_above_avg]
    return out


no_of_days = int(input("Enter the number of days : "))
list_out = input_temp(no_of_days)
print("Total value : ", str(list_out[0]))
print("Average : ", str(list_out[1]))
print("Days with temperature above average : ", list_out[2])
