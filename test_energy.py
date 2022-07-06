import pypixet
import pypxproc
import time
import numpy

pypixet.start()
#Starts PixetPro
pixet = pypixet.pixet
#initialize as a variable so its methods can be called
devices = pixet.devices()
#get a list of connected devices
if devices[0].fullName()=="FileDevice 0":
    print("No devices connected")
    pixet.exitPixet()
    exit()
dev0 = devices[0]
#pick the first device in the list (minipix)
si = pypxproc.SpectraImaging(dev0.asIDev())
#initialize spectral imaging environment
print("Load calibration...")
rc = si.loadCalibrationFromDevice()
#load the default calibration contained in the minipix
si.setMeasParams(0, 100, 0.5, True, False)
#measure energy range from 0-100 keV, with 0.5 keV bands
print("Start measurement...")
print("measuring...")
print("Get frames for energy range: 0 - 100 keV")
iteration = 0
frameCount = 0
#THIS WILL KEEP RUNNING UNTIL YOU QUIT THE TERMINAL!!!
while True:
    #if not a dead frame, save frame energy as txt
    if iteration%2==0:
        rc = si.startMeasurement(1, 1, "", False)
        while si.isRunning(): #DO NOT REMOVE, THIS ENSURES THAT THERE IS A DEAD TIME BETWEEN FRAMES
            time.sleep(0.1)
        rc1, fb = si.getFrameForEnergyRange(0, 199, True)
        filename = 'short' + str(frameCount) + '.txt'
        numpy.savetxt(filename, numpy.array(fb), fmt='%1.3f')
        frameCount += 1
    #take the dead frame measurement and throw it away
    else:
        rc = si.startMeasurement(1, 1, "", False)
        while si.isRunning(): #DO NOT REMOVE, THIS ENSURES THAT THERE IS A DEAD TIME BETWEEN FRAMES
            time.sleep(0.1)
        rc1, fb = si.getFrameForEnergyRange(0, 199, True)
    iteration += 1