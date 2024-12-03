"""
In Lab 16, locate the attached csv data file called ‘OHRU.csv’. 
This file was downloaded from the FRED Economic Data site, https://fred.stlouisfed.org/. 
It records the national unemployment rate going back to 1976. 
Analyze the header information using the enumerate() function. 
Then plot the graph. Remember to label the axes appropriately. 
For the Date, use the datetime class to label the x-axis with appropriate information.
"""
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

#Path and read
path = Path(r'OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#Init lists
dates = []

unemployment_rate = []

#processing
for row in reader:
    try:
        date_lookup = datetime.strptime(row[0], '%Y-%m-%d')
        unemployed = float(row[1])
    except ValueError as e:
        print(date_lookup)
    dates.append(date_lookup)
    unemployment_rate.append(unemployed)

#graph and graph style
plt.style.use('dark_background')
figure, graph = plt.subplots()

graph.plot(dates, unemployment_rate, color='red')

graph.set_title('Unemployment rate by month: 1976 - 2022')
graph.set_ylabel('Unemployment rate')
graph.set_xlabel('Date')
figure.autofmt_xdate()

plt.show()



