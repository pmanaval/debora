import time
import board
import adafruit_icm20x
from csv import writer

i2c = board.I2C()  # uses board.SCL and board.SDA
icm = adafruit_icm20x.ICM20948(i2c)
g = 1

end = time.time() + 60 * 5

while time.time() < end:
    print(g)
    print("")
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (icm.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rads/s" % (icm.gyro))
    print("Magnetometer X:%.2f, Y: %.2f, Z: %.2f uT" % (icm.magnetic))
    print("")
    accel_data = [icm.acceleration,icm.magnetic]
    
    def append_list_as_row(acceldata, list_of_elem):
    
        #open file in append mode
        
        with open(acceldata, 'a+', newline='') as write_obj:
            
            #Create a writer object from a csv module
            
            csv_writer = writer(write_obj)
            
            # Add contents of list as last row in the csv file
            
            csv_writer.writerow(list_of_elem)
            
    append_list_as_row('acceldata.csv',accel_data)
    

        
    g = g+1
    time.sleep(1.0)
