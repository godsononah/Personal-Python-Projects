"""Frequency Distribution Table"""

def frequency_count(data_list, interval_start, interval_end):
    count = 0
    for data in data_list:
        if data in range(interval_start, (interval_end + 1)):
            count += 1
    return count

print('This program will accept a group of data and print a frequency distribution table with the class interval and frequency.\n')

title = input('Enter the title of the frequency distribution table: ') # Inputs the title/name of the frequency distribution table
frequency_name = input('Enter the frequency count name: ')

input_data = input("Enter the data (format => 'data1, data2, data3': ")
data_string_list = input_data.split(', ')
data_list = []
for data in data_string_list:
    data_list.append(int(data))

data_dict = {}
while True:
    interval = input("Enter the class interval or enter N or n if you don't have any more class interval to input: ")
    if interval.lower() == 'n':
        break
    else:
        interval_start = int(interval.split('-')[0])
        interval_end = int(interval.split('-')[-1])
        data_dict[interval] = frequency_count(data_list, interval_start, interval_end)

print('\n\n{:>4}'.format(title))
print('__________________________________________________________________\n')
print('        Class Interval    |    Number of Persons in Class')

for key in data_dict:
    print('{:>16}                     {:<}             '.format(key, data_dict[key]))


"""Data as an example:
Title = Raw Scores of Hypnotic Suceptibility
Frequency count name = Number of Persons in Class
data_list1 = [55, 86, 52, 17, 61, 57, 84, 51, 16, 64,
              22, 56, 25, 38, 35, 24, 54, 26, 37, 38,
              52, 42, 59, 26, 21, 55, 40, 59, 25, 57,
              91, 27, 38, 53, 19, 93, 25, 39, 52, 56,
              66, 14, 18, 63, 59, 68, 12, 19, 62, 45,
              47, 98, 88, 72, 50, 49, 96, 89, 71, 66,
              50, 44, 71, 57, 90, 53, 41, 72, 56, 93,
              57, 38, 55, 49, 87, 59, 36, 56, 48, 70,
              33, 69, 50, 50, 60, 35, 67, 51, 50, 52,
              11, 73, 46, 16, 67, 13, 71, 47, 25, 77]"""
data_list1 = [55, 86, 52, 17, 61, 57, 84, 51, 16, 64, 22, 56, 25, 38, 35, 24, 54, 26, 37, 38, 52, 42, 59, 26, 21, 55, 40, 59, 25, 57, 91, 27, 38, 53, 19, 93, 25, 39, 52, 56, 66, 14, 18, 63, 59, 68, 12, 19, 62, 45, 47, 98, 88, 72, 50, 49, 96, 89, 71, 66, 50, 44, 71, 57, 90, 53, 41, 72, 56, 93, 57, 38, 55, 49, 87, 59, 36, 56, 48, 70, 33, 69, 50, 50, 60, 35, 67, 51, 50, 52, 11, 73, 46, 16, 67, 13, 71, 47, 25, 77]
