from  TMC2209_PY.registers import * 
from .uart import UART
import time


class TMC2209Configure:
    """
    Represents the TMC2209 configuration, including registers, microsteps,
    current, and voltage. Excludes GPIO pins and UART handler for simplicity.
    """

    def __init__(self ,uart: UART ,MS1,MS2,EN, node_address):

        self.uart = uart
        self.ms1 = MS1
        self.ms2= MS2
        self.en= EN
        
        
        self.node_address = node_address  # Node address for the TMC2209
        
        # Registers
        self.gconf = GCONF()
        self.gstat = GSTAT()
        self.ifcnt = IFCNT()
        self.nodeconf = NODECONF()
        self.otp_prog = OTP_PROG()
        self.otp_read = OTP_READ()
        self.ioin = IOIN()
        self.factory_conf = FACTORY_CONF()
        self.ihold_irun = IHOLD_IRUN()
        self.tpowerdown = TPOWERDOWN()
        self.tstep = TSTEP()
        self.tpwmthrs = TPWMTHRS()
        self.vactual = VACTUAL()
        self.tcoolthrs = TCOOLTHRS()
        self.sgthrs = SGTHRS()
        self.sg_result = SG_RESULT()
        self.coolconf = COOLCONF()
        self.mscnt = MSCNT()
        self.mscuract = MSCURACT()
        self.chopconf = CHOPCONF()
        self.drv_status = DRV_STATUS()
        self.pwmconf = PWMCONF()
        self.pwm_scale = PWM_SCALE()
        self.pwm_auto = PWM_AUTO()
        
        
       

    @staticmethod
    def _calculate_crc(data: list) -> int:
        
        crc = 0
        for byte in data:
            current_byte = byte
            for _ in range(8):
                if ((crc >> 7) ^ (current_byte & 0x01)):
                    crc = (crc << 1) ^ 0x07
                else:
                    crc = (crc << 1)
                crc &= 0xFF
                current_byte >>= 1
        return crc


    def send_register(self, data: int, address: int):
        
        # Construct the packet
        packet = [
            0x5,  # Sync byte
            self.node_address,  # Node address
            (1 << 7) | address,  # Register address
            (data >> 24) & 0xFF,  # Data byte 1
            (data >> 16) & 0xFF,  # Data byte 2
            (data >> 8) & 0xFF,   # Data byte 3
            data & 0xFF           # Data byte 4
        ]

        # Compute CRC and append it to the packet
        crc = self._calculate_crc(packet[:7])
        packet.append(crc)

        # Send the packet over UART
        self.uart.send_message(bytes(packet))
        

    def send_read_request(self, address: int):
        

        # Construct the datagram for a read request
        packet = [
            0x05,  # Sync byte (bits 0-7)
            self.node_address,  # 8-bit node address (bits 16-23)
            (0 << 7) | address  # RW (MSB = 0) + 7-bit register address (bits 24-31)
        ]

        # Compute CRC for the first 3 bytes and append it
        crc = self._calculate_crc(packet)
        packet.append(crc)

        # Transmit the datagram over UART
        self.uart.send_message(bytes(packet))
    
    def read_register(self, address: int) -> int:
        
       # Send the read request using the existing send_read_request function
        self.send_read_request(address)
        while True:
            response = self.uart.read_message(8)
            
            if response and len(response) == 8:
                if self._calculate_crc(response[:-1]) == response[-1]:  # Verify CRC
                    # Extract the 32-bit data from the response (bytes 4-7)
                    data = (
                        (response[3] << 24) |
                        (response[4] << 16) |
                        (response[5] << 8)  |
                        (response[6]) 
                    )
                    break  # Exit loop when valid data is received
                else:
                    print("CRC mismatch! Retrying...")  # Debugging message
            else:
                print("Invalid response size! Retrying...")  # Debugging message
                break
                

        return data

    def write_GCONF(self):
        self.send_register(self.gconf.reg, GCONF_adr)

    def write_GSTAT(self):
        self.send_register(self.gstat.reg, GSTAT_adr)

    def write_NODECONF(self):
        self.send_register(self.nodeconf.reg, NODECONF_adr)

    def write_OTP_PROG(self):
        self.send_register(self.otp_prog.reg, OTP_PROG_adr)

    def write_FACTORY_CONF(self):
        self.send_register(self.factory_conf.reg, FACTORY_CONF_adr)

    def write_IHOLD_IRUN(self):
        self.send_register(self.ihold_irun.reg, IHOLD_IRUN_adr)

    def write_TPOWERDOWN(self):
        self.send_register(self.tpowerdown.reg, TPOWER_DOWN_adr)

    def write_TPWMTHRS(self):
        self.send_register(self.tpwmthrs.reg, TPWMTHRS_adr)

    def write_VACTUAL(self):
        self.send_register(self.vactual.reg, VACTUAL_adr)

    def write_TCOOLTHRS(self):
        self.send_register(self.tcoolthrs.reg, TCOOLTHRS_adr)

    def write_SGTHRS(self):
        self.send_register(self.sgthrs.reg, SGTHRS_adr)

    def write_COOLCONF(self):
        self.send_register(self.coolconf.reg, COOLCONF_adr)

    def write_CHOPCONF(self):
        self.send_register(self.chopconf.reg, CHOPCONF_adr)

    def write_PWMCONF(self):
        self.send_register(self.pwmconf.reg, PWMCONF_adr)

    def read_GSTAT(self):
        self.gstat.reg = self.read_register(GSTAT_adr)
        return self.gstat.reg

    def read_IFCNT(self):
        self.ifcnt.reg = self.read_register(IFCNT_adr)
        return self.ifcnt.reg

    def read_OTP_READ(self):
        self.otp_read.reg = self.read_register(OTP_READ_adr)
        return self.otp_read.reg

    def read_IOIN(self):
        self.ioin.reg = self.read_register(IOIN_adr)
        return self.ioin.reg

    def read_FACTORY_CONF(self):
        self.factory_conf.reg = self.read_register(FACTORY_CONF_adr)
        return self.factory_conf.reg

    def read_TSTEP(self):
        self.tstep.reg = self.read_register(TSTEP_adr)
        return self.tstep.reg

    def read_SG_RESULT(self):
        self.sg_result.reg = self.read_register(SG_RESULT_adr)
        return self.sg_result.reg

    def read_MSCNT(self):
        self.mscnt.reg = self.read_register(MSCNT_adr)
        return self.mscnt.reg

    def read_MSCURACT(self):
        self.mscuract.reg = self.read_register(MSCURACT_adr)
        return self.mscuract.reg

    def read_CHOPCONF(self):
        self.chopconf.reg = self.read_register(CHOPCONF_adr)
        return self.chopconf.reg

    def read_DRV_STATUS(self):
        self.drv_status.reg = self.read_register(DRV_STATUS_adr)
        return self.drv_status.reg

    def read_PWMCONF(self):
        self.pwmconf.reg = self.read_register(PWMCONF_adr)
        return self.pwmconf.reg

    def read_PWM_SCALE(self):
        self.pwm_scale.reg = self.read_register(PWM_SCALE_adr)
        return self.pwm_scale.reg

    def read_PWM_AUTO(self):
        self.pwm_auto.reg = self.read_register(PWM_AUTO_adr)
        return self.pwm_auto.reg

    def initialize(self):
        self.chopconf.toff = 5
        self.chopconf.hstrt = 5
        self.chopconf.vsense = 1
        self.chopconf.intpol = 1
        self.chopconf.mres = 4
        self.write_CHOPCONF()

        self.ihold_irun.IHOLD = 0
        self.ihold_irun.IRUN = 15
        self.ihold_irun.IHOLDDELAY = 1
        self.write_IHOLD_IRUN()

        self.gconf.I_scale_analog = 1
        self.gconf.mstep_reg_select = 1
        self.gconf.multistep_filt = 1
        self.gconf.pdn_disable = 1
        self.gconf.shaft = 0
        self.write_GCONF()

        self.nodeconf.SENDDELAY = 7
        self.write_NODECONF()

        self.pwmconf.PWM_OFS = 36
        self.pwmconf.PWM_FREQ = 1
        self.pwmconf.PWM_autoscale = 1
        self.pwmconf.PWM_autograd = 1
        self.pwmconf.PWM_REG = 1
        self.pwmconf.PWM_LIM = 12
        self.write_PWMCONF()
                
    	
    def __repr__(self):
        """
        String representation of the TMC2209 configuration.
        """
        return (
            f"TMC2209Configure(node_address={self.node_address}, "
            f", MS1={self.ms1}, MS2={self.ms2})"
        )
        
        

    

