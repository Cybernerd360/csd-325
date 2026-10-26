# import files from computer to python
import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt
# Define the file path to find the data file
filename = r'C:\Users\Aubre\Downloads\sitka_weather\sitka_weather_2018_simple.csv'
with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
# define the lists to store the data
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            highs.append(int(row[5]))
            lows.append(int(row[6]))
# Ask customer for input
while True:
    menu = input('Enter your choice (highs, lows, exit): ').strip().lower()
# highs temperatures
    if menu == 'highs':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
   # lows temperatures     
    elif menu == 'lows':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
   # exit code     
    elif menu == 'exit':
        print("exit selected")
        sys.exit()
   # invalid input
    else:
        print("Invalid choice")
