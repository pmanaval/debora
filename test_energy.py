import pypixet
import pypxproc
import time
import numpy
pypixet.start()
pixet = pypixet.pixet
devices = pixet.devices()

if devices[0].fullName()=="FileDevice 0":
    print("No devices connected")
    pixet.exitPixet()
    exit()
dev0 = devices[0]
si = pypxproc.SpectraImaging(dev0.asIDev())
print("Load calibration...")
rc = si.loadCalibrationFromDevice()
print("rc", rc , "0 is OK")
si.setMeasParams(0, 100, 0.5, True, False)
# The clusters will be sorted into 20 keV wide bands, first at 0, last at 5120,
# noisy pixels masked, subpixel correction ON
print("Start measurement...")
#si.startMeasurement(acqTime (ignore at data-driven devs), measTime, outFile, processData)
rc = si.startMeasurement(20, 10, "", True)
print("rc", rc, "(0 is OK)")
print("measuring...")
while si.isRunning():
    time.sleep(0.1)
print("Get frames for energy range: 0 - 15 keV")
# getFrameForEnergyRange(energyFromIndex, energyToIndex, normalize)
rc1, fb = si.getFrameForEnergyRange(0, 199, True)
#rc2, fg = si.getFrameForEnergyRange(5, 9, True)
#rc3, fr = si.getFrameForEnergyRange(10, 14, True)

print("success!")