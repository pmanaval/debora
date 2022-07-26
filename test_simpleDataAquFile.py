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
#device temp pg 35
print("dev0.doAdvancedAcquisition (100 frames @ 0.1 sec) - start")
rc = dev0.doAdvancedAcquisition(1000, 0.1,pixet.PX_ACQTYPE_FRAMES, pixet.PX_ACQMODE_NORMAL, pixet.PX_FTYPE_ASCII_FRAME,0, r"RunData\short")
print("dev0.doAdvancedAcquisition - end:", rc, "(0 is OK)")
pixet.exitPixet()