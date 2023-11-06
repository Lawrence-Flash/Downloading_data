import csv

from matplotlib import pyplot as plt
from datetime import datetime

def main():
    filename = 'sitka_weather_07-2014.csv'
    #header_positions(filename)
    Extract_Read_Data(filename)
    

def header_positions(file):
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        for index, column_header in enumerate(header_row):
            print(index, column_header)
    

def Extract_Read_Data(file):
    # Get dates and high temperature from file
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        dates, highs = [], []
        for row in reader:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            dates.append(current_date)
            
            high = int(row[1])
            highs.append(high)
        
        # call the function that plots the data in a line a graph plot
        plot_Data(highs,dates)
    
# this function is responsible for ploting the Data
def plot_Data(temprature, DATE):
    
    # Plot the data.
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(DATE, temprature, c='red')
    
    # Format plot
    plt.title("Daily high temperatures, july 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major',labelsize=16)

    plt.show()
    





main()