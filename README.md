1. here i created a file called highs_lows.py that reads data from a csv file called sitka_weater_07-2014.csv the contains differents functions that manipulate the data contained in the file.....

2. the function header_positions(file) : reads the file's data using csv reader function and only displays the headers in the file in the enumerated format

3. the function Extract_Read_Data(file): reads the high temperature of the day so basically this function extracts data from the file that contains the high temperature of the day...

i created two empty list to store the dates and high temperatures from the file and then i converted the data containing the date information (row[0]) to a datetime object and append it to dates list.

this function also calls the plot_data() function which visaulizes the temperature data we have and plot a line graph of the Data extracted from the csv file creating a simple plot of the daily highs using the matplotlib.
the function also accepts two parameters which are dates and temperatures to used by the plot()

