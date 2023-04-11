import csv
import os
import numpy as np
from matplotlib import pyplot as plt

rawdata_path = "C:\\Users\\1priy\Desktop\\March 27 FOV Testing\\TOMFOOLERY2ElectricBoogaloo\\TOMFOOLERY\\counts vs angles\\rawdata"
histo_array = np.zeros((7,2)) #initializes the array that will be plotted
histo_array[:, 1] = [0, 12.81, 24.87, 37.04, 49.17, 61.37, 73.74] #Change angles here as necessary 
i = 0 #indexing for the histogram array


for foldername in os.listdir(rawdata_path):

    folder_path = "C:\\Users\\1priy\Desktop\\March 27 FOV Testing\\TOMFOOLERY2ElectricBoogaloo\\TOMFOOLERY\\counts vs angles\\rawdata\\{}".format(foldername)

    #Get the name of the set of measurements
    allfilenames = os.listdir(folder_path)
    filename = allfilenames[0]
    filename = filename.split("_000")
    filename = filename[0]
    plotname = filename


    # Create a new CSV file
    csvfilename = filename
    csv_file_path = f"{csvfilename}.csv" 

    # writed the data to a csv file
    with open(csv_file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for filename in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename)):
                with open(os.path.join(folder_path, filename), "r") as text_file:
                    if "." not in filename or filename.rsplit(".", 1)[1].lower() == "txt":
                        for line in text_file:
                            values = line.strip().split()
                            for value in values:
                                value = float(value)
                                if value != 0:
                                    writer.writerow([value])

    total_readings = 0

    #Gets the total measurements in each reading
    with open(f'{csvfilename}.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_readings += len(row)
        print('Total readings in this measurement:', total_readings)
        histo_array[i,0] = total_readings
        
    i = i + 1
print(histo_array) 



#Creates the count vs angle histogram
#plt.subplot(1, 2, 1)
fig, axis  = plt.subplots()
x1 = histo_array[:,1]
y1 = histo_array[:,0]
error1 = np.sqrt(y1)
print(error1)
plt.bar(x1,y1,
        yerr = error1,
        width = 3.0, 
        align = 'center',
        capsize=4)
plt.title("Counts vs Angle")
plt.ylabel("Count")
plt.xlabel('Angle (degrees)')
plt.savefig('{}_Histo.png'.format(plotname))



#Creates the count vs angle plot
#plt.subplot(1, 2, 2)
fig, axis  = plt.subplots()
x2 = histo_array[:,1]
y2 = histo_array[:,0]
error2 = np.sqrt(y2)
print(error2)
plt.scatter(x2,y2)
plt.errorbar(x2,y2, yerr = error2, fmt = "o")
plt.title("Counts vs Angle")
plt.ylabel("Count")
plt.xlabel('Angle (degrees)')
plt.savefig('{}_plot.png'.format(plotname))

plt.show()

 