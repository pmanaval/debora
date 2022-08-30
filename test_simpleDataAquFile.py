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



#this should load the file into the camera. 
#If the value of rc is 0, then it means the configuration is loaded.
rc=dev0.loadFactoryConfig()
print("loadFactoryConfig:", rc)



#testing Functions to see if the configuration file is loading properly
print(str(dev0.hasDefaultConfig())+str(dev0.isConfigInDeviceSupported())+str(dev0.hasConfigInDevice()))
#returns 100, telling me it has the default config  but it's not supported for some reason and it's not in the device
#device temp pg 35
print("dev0.doAdvancedAcquisition (100 frames @ 0.1 sec) - start")
rc = dev0.doAdvancedAcquisition(10, 0.1,pixet.PX_ACQTYPE_FRAMES, pixet.PX_ACQMODE_NORMAL, pixet.PX_FTYPE_ASCII_FRAME,0, "short")
print("dev0.doAdvancedAcquisition - end:", rc, "(0 is OK)")
pixet.exitPixet()
