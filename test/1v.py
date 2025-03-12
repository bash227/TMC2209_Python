from TMC2209_PY import *


#BOARD mode pins
EN_pin = 33
MS1_pin = 35
MS2_pin = 32       

uart1 = UART("/dev/ttyTHS1",11520)
tmc2209 = TMC2209Configure(uart1,EN=EN_pin,MS1=MS1_pin,MS2=MS2_pin,node_address=0)   
print(tmc2209)

tmc2209.initialize()
tmc2209.set_SENDDELAY(7)
tmc2209.set_MRES(2)
tmc2209.set_direction(0)
tmc2209.set_velocity(-0)  #256

tmc2209.enable()

while True:

    print(tmc2209.read_MSCNT())
    if tmc2209.read_MSCNT() == 256:
        print("0.1mm is moved")



