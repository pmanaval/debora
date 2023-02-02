import time
import board
import adafruit_icm20x
from adafruit_bme280 import basic as adafruit_bme280
from csv import writer

i2c = board.I2C()  # uses board.SCL and board.SDA
icm = adafruit_icm20x.ICM20948(i2c)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

g = 1

end = time.time() + 60 * 5 #Change this to however long the code should run

header_names = ['Time', 'Acceleration: X: m/s^2','Acceleration: Y: m/s^2', 'Acceleration: Z: m/s^2', 
'Gyroscope: X: rads/s', 'Gyroscope: Y: rads/s', 'Gyroscope: Z: rads/s',
'Temperature (C)', 'Humidity(%)','Pressure (hPa)', 'Altitude (m)' ]

def append_list_as_row(sensordata, list_of_elem):#from https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/
    
        #open file in append mode
        
        with open(sensordata, 'a+', newline='') as write_obj:
            
            #Create a writer object from a csv module
            
            csv_writer = writer(write_obj)
            
            # Add contents of list as last row in the csv file
            
            csv_writer.writerow(list_of_elem)
            
append_list_as_row('sensordata.csv',header_names)

while time.time() < end:
    
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S",t) #gets current time
    
    print(g)
    print("")
    
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (icm.acceleration))
    x_accel, y_accel, z_accel = icm.acceleration
    
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rads/s" % (icm.gyro))
    x_gyro, y_gryo, z_gyro = icm.gyro
    
    print("Magnetometer X:%.2f, Y: %.2f, Z: %.2f uT" % (icm.magnetic))
    x_mag, y_mag, z_mag = icm.magnetic
    
    print("")
    
    print("\nTemperature: %0.1f C" % bme280.temperature)
    temp = bme280.temperature
    
    print("Humidity: %0.1f %%" % bme280.relative_humidity)
    humidity = bme280.relative_humidity
    
    print("Pressure: %0.1f hPa" % bme280.pressure)
    pressure = bme280.pressure
    
    print("Altitude = %0.2f meters" % bme280.altitude)
    altitude = bme280.altitude
    
    sensor_data = [current_time, x_accel, y_accel, z_accel, x_gyro, y_gryo, z_gyro, temp, humidity, pressure, altitude]
    
            
    append_list_as_row('sensordata.csv',sensor_data)
    

        
    g = g+1
    time.sleep(1.0)
