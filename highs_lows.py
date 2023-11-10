import csv

from matplotlib import pyplot as plt
from datetime import datetime

def main():
    filename = 'death_valley_2014.csv'
    #header_positions(filename)
    Extract_Read_Data(filename)
    

def header_positions(file):
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        for index, column_header in enumerate(header_row):
            print(index, column_header)
    

def Extract_Read_Data(file):
    # Get dates, high  and low temperature from file
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
        
        # call the function that plots the data in a line a graph plot
        plot_Data(lows,highs,dates)
    
# this function is responsible for ploting the Data
def plot_Data(low_temperature,high_temprature, DATE):
    
    # Plot the data.
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(DATE, high_temprature, c='red', alpha=0.5)
    plt.plot(DATE, low_temperature, c='blue', alpha=0.5)
    # Adding the shadding between the graphs to show the range between each day's high and low temperatures
    plt.fill_between(DATE, high_temprature, low_temperature, facecolor='blue', alpha=0.1)
    
    # Format plot
    plt.title("Daily high and low temperatures - 2023\nDeath Valley, SA", fontsize=20)
    plt.xlabel('', fontsize=16)
    # Draw the date labels diagonally to prevent them from overlapping
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major',labelsize=16)

    plt.show()
    





main()