import pypixet
import pypxproc
pypixet.start()
pixet = pypixet.pixet
devices = pixet.devices()

if devices[0].fullName()=="FileDevice 0":
    print("No devices connected")
    pixet.exitPixet()
    exit()
dev0 = devices[0]
#device temp pg 35
print("dev0.doSimpleAcquisition (3 frames @ 1 sec) - start")
rc = dev0.doSimpleAcquisition(3, 1, pixet.PX_FTYPE_AUTODETECT, "example.png")
print("dev0.doSimpleAcquisition - end:", rc, "(0 is OK)")
pixet.exitPixet()