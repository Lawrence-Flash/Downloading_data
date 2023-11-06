import csv
def main():
    filename = 'sitka_weather_07-2014.csv'
    #header_positions(filename)
    Extract_Read_Data(filename)

def header_positions(file):
    with open(file) as fil:
        reader = csv.reader(fil)
        header_row = next(reader)
        
        for index, column_header in enumerate(header_row):
            print(index, column_header)
    
def Extract_Read_Data(file):
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        highs = []
        for row in reader:
            highs.append(row[1])
        
        print(highs)
    





main()