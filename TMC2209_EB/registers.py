
# General Configuration
GCONF_adr = 0x00        # General Configuration register address
GSTAT_adr = 0x01        # General Status register address
IFCNT_adr = 0x02        # Interrupt Function Counter register address
NODECONF_adr = 0x03     # Node Configuration register address
OTP_PROG_adr = 0x04     # OTP Programming register address
OTP_READ_adr = 0x05     # OTP Read register address
IOIN_adr = 0x06         # IO Input Status register address
FACTORY_CONF_adr = 0x07 # Factory Configuration register address

# Velocity Dependent Control
IHOLD_IRUN_adr = 0x10   # Hold and Run Current Configuration register address
TPOWER_DOWN_adr = 0x11  # Power Down Time register address
TSTEP_adr = 0x12        # Step Time register address
TPWMTHRS_adr = 0x13     # PWM Threshold register address
VACTUAL_adr = 0x22      # Actual Velocity register address

# StallGuard Control
TCOOLTHRS_adr = 0x14    # Cool Threshold register address
SGTHRS_adr = 0x40       # StallGuard Threshold register address
SG_RESULT_adr = 0x41    # StallGuard Result register address
COOLCONF_adr = 0x42     # Cool Configuration register address

# Sequencer Registers
MSCNT_adr = 0x6A        # Motion Step Counter register address
MSCURACT_adr = 0x6B     # Motion Current Active Configuration register address

# Chopper Control Registers
CHOPCONF_adr = 0x6C     # Chopper Configuration register address
DRV_STATUS_adr = 0x6F   # Driver Status register address
PWMCONF_adr = 0x70      # PWM Configuration register address
PWM_SCALE_adr = 0x71    # PWM Scaling register address
PWM_AUTO_adr = 0x72     # PWM Automatic Configuration register address



class GCONF:
    """
    Represents the GCONF register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the GCONF register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def I_scale_analog(self):
        return (self.reg >> 0) & 0x1

    @I_scale_analog.setter
    def I_scale_analog(self, value):
        self.reg = (self.reg & ~(0x1 << 0)) | ((value & 0x1) << 0)

    @property
    def internal_Rsense(self):
        return (self.reg >> 1) & 0x1

    @internal_Rsense.setter
    def internal_Rsense(self, value):
        self.reg = (self.reg & ~(0x1 << 1)) | ((value & 0x1) << 1)

    @property
    def en_SpreadCycle(self):
        return (self.reg >> 2) & 0x1

    @en_SpreadCycle.setter
    def en_SpreadCycle(self, value):
        self.reg = (self.reg & ~(0x1 << 2)) | ((value & 0x1) << 2)

    @property
    def shaft(self):
        return (self.reg >> 3) & 0x1

    @shaft.setter
    def shaft(self, value):
        self.reg = (self.reg & ~(0x1 << 3)) | ((value & 0x1) << 3)

    @property
    def index_optw(self):
        return (self.reg >> 4) & 0x1

    @index_optw.setter
    def index_optw(self, value):
        self.reg = (self.reg & ~(0x1 << 4)) | ((value & 0x1) << 4)

    @property
    def index_step(self):
        return (self.reg >> 5) & 0x1

    @index_step.setter
    def index_step(self, value):
        self.reg = (self.reg & ~(0x1 << 5)) | ((value & 0x1) << 5)

    @property
    def pdn_disable(self):
        return (self.reg >> 6) & 0x1

    @pdn_disable.setter
    def pdn_disable(self, value):
        self.reg = (self.reg & ~(0x1 << 6)) | ((value & 0x1) << 6)

    @property
    def mstep_reg_select(self):
        return (self.reg >> 7) & 0x1

    @mstep_reg_select.setter
    def mstep_reg_select(self, value):
        self.reg = (self.reg & ~(0x1 << 7)) | ((value & 0x1) << 7)

    @property
    def multistep_filt(self):
        return (self.reg >> 8) & 0x1

    @multistep_filt.setter
    def multistep_filt(self, value):
        self.reg = (self.reg & ~(0x1 << 8)) | ((value & 0x1) << 8)

    @property
    def test_mode(self):
        return (self.reg >> 9) & 0x1

    @test_mode.setter
    def test_mode(self, value):
        self.reg = (self.reg & ~(0x1 << 9)) | ((value & 0x1) << 9)

    def __repr__(self):
        """
        String representation of the GCONF register showing bitfields and the full register value.
        """
        return f"GCONF(reg={self.reg:032b})"



class GSTAT:
    """
    Represents the GSTAT register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the GSTAT register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def reset(self):
        return (self.reg >> 0) & 0x1

    @reset.setter
    def reset(self, value):
        self.reg = (self.reg & ~(0x1 << 0)) | ((value & 0x1) << 0)

    @property
    def drv_err(self):
        return (self.reg >> 1) & 0x1

    @drv_err.setter
    def drv_err(self, value):
        self.reg = (self.reg & ~(0x1 << 1)) | ((value & 0x1) << 1)

    @property
    def uv_cp(self):
        return (self.reg >> 2) & 0x1

    @uv_cp.setter
    def uv_cp(self, value):
        self.reg = (self.reg & ~(0x1 << 2)) | ((value & 0x1) << 2)

    def __repr__(self):
        """
        String representation of the GSTAT register showing bitfields and the full register value.
        """
        return (
            f"GSTAT(reg={self.reg:032b}, reset={self.reset}, drv_err={self.drv_err}, uv_cp={self.uv_cp})"
        )


class IFCNT:
    """
    Represents the IFCNT register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the IFCNT register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def count(self):
        """
        Get the 8-bit count field (bits 0–7).
        """
        return (self.reg >> 0) & 0xFF

    @count.setter
    def count(self, value):
        """
        Set the 8-bit count field (bits 0–7).
        """
        self.reg = (self.reg & ~(0xFF << 0)) | ((value & 0xFF) << 0)

    @property
    def reserved(self):
        """
        Get the 24-bit reserved field (bits 8–31).
        """
        return (self.reg >> 8) & 0xFFFFFF

    def __repr__(self):
        """
        String representation of the IFCNT register showing bitfields and the full register value.
        """
        return f"IFCNT(reg={self.reg:032b}, count={self.count}, reserved={self.reserved:06X})"



class NODECONF:
    """
    Represents the NODECONF register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the NODECONF register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def reserved1(self):
        """
        Get the 8-bit reserved1 field (bits 0–7).
        """
        return (self.reg >> 0) & 0xFF

    @reserved1.setter
    def reserved1(self, value):
        """
        Set the 8-bit reserved1 field (bits 0–7).
        """
        self.reg = (self.reg & ~(0xFF << 0)) | ((value & 0xFF) << 0)

    @property
    def SENDDELAY(self):
        """
        Get the 4-bit SENDDELAY field (bits 8–11).
        """
        return (self.reg >> 8) & 0xF

    @SENDDELAY.setter
    def SENDDELAY(self, value):
        """
        Set the 4-bit SENDDELAY field (bits 8–11).
        """
        self.reg = (self.reg & ~(0xF << 8)) | ((value & 0xF) << 8)

    @property
    def reserved2(self):
        """
        Get the 20-bit reserved2 field (bits 12–31).
        """
        return (self.reg >> 12) & 0xFFFFF

    def __repr__(self):
        """
        String representation of the NODECONF register showing bitfields and the full register value.
        """
        return (
            f"NODECONF(reg={self.reg:032b}, reserved1={self.reserved1}, "
            f"SENDDELAY={self.SENDDELAY}, reserved2={self.reserved2:05X})"
        )

class OTP_PROG:
    """
    Represents the OTP_PROG register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the OTP_PROG register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def OTPBIT(self):
        """
        Get the 3-bit OTPBIT field (bits 0–2).
        """
        return (self.reg >> 0) & 0x7

    @OTPBIT.setter
    def OTPBIT(self, value):
        """
        Set the 3-bit OTPBIT field (bits 0–2).
        """
        self.reg = (self.reg & ~(0x7 << 0)) | ((value & 0x7) << 0)

    @property
    def FREE1(self):
        """
        Get the 1-bit FREE1 field (bit 3).
        """
        return (self.reg >> 3) & 0x1

    @FREE1.setter
    def FREE1(self, value):
        """
        Set the 1-bit FREE1 field (bit 3).
        """
        self.reg = (self.reg & ~(0x1 << 3)) | ((value & 0x1) << 3)

    @property
    def OTPBYTE(self):
        """
        Get the 2-bit OTPBYTE field (bits 4–5).
        """
        return (self.reg >> 4) & 0x3

    @OTPBYTE.setter
    def OTPBYTE(self, value):
        """
        Set the 2-bit OTPBYTE field (bits 4–5).
        """
        self.reg = (self.reg & ~(0x3 << 4)) | ((value & 0x3) << 4)

    @property
    def FREE2(self):
        """
        Get the 2-bit FREE2 field (bits 6–7).
        """
        return (self.reg >> 6) & 0x3

    @FREE2.setter
    def FREE2(self, value):
        """
        Set the 2-bit FREE2 field (bits 6–7).
        """
        self.reg = (self.reg & ~(0x3 << 6)) | ((value & 0x3) << 6)

    @property
    def OTPMAGIC(self):
        """
        Get the 8-bit OTPMAGIC field (bits 8–15).
        """
        return (self.reg >> 8) & 0xFF

    @OTPMAGIC.setter
    def OTPMAGIC(self, value):
        """
        Set the 8-bit OTPMAGIC field (bits 8–15).
        """
        self.reg = (self.reg & ~(0xFF << 8)) | ((value & 0xFF) << 8)

    @property
    def reserved(self):
        """
        Get the 16-bit reserved field (bits 16–31).
        """
        return (self.reg >> 16) & 0xFFFF

    def __repr__(self):
        """
        String representation of the OTP_PROG register showing bitfields and the full register value.
        """
        return (
            f"OTP_PROG(reg={self.reg:032b}, OTPBIT={self.OTPBIT}, FREE1={self.FREE1}, "
            f"OTPBYTE={self.OTPBYTE}, FREE2={self.FREE2}, OTPMAGIC={self.OTPMAGIC}, reserved={self.reserved:04X})"
        )

class OTP_READ:
    """
    Represents the OTP_READ register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the OTP_READ register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    # OTP0
    @property
    def bit_0_0to4(self):
        """
        Get the 4-bit bit_0_0to4 field (bits 0–3).
        """
        return (self.reg >> 0) & 0xF

    @bit_0_0to4.setter
    def bit_0_0to4(self, value):
        """
        Set the 4-bit bit_0_0to4 field (bits 0–3).
        """
        self.reg = (self.reg & ~(0xF << 0)) | ((value & 0xF) << 0)

    @property
    def bit_0_5(self):
        """
        Get the 1-bit bit_0_5 field (bit 4).
        """
        return (self.reg >> 4) & 0x1

    @bit_0_5.setter
    def bit_0_5(self, value):
        """
        Set the 1-bit bit_0_5 field (bit 4).
        """
        self.reg = (self.reg & ~(0x1 << 4)) | ((value & 0x1) << 4)

    @property
    def bit_0_6(self):
        """
        Get the 1-bit bit_0_6 field (bit 5).
        """
        return (self.reg >> 5) & 0x1

    @bit_0_6.setter
    def bit_0_6(self, value):
        """
        Set the 1-bit bit_0_6 field (bit 5).
        """
        self.reg = (self.reg & ~(0x1 << 5)) | ((value & 0x1) << 5)

    @property
    def bit_0_7(self):
        """
        Get the 1-bit bit_0_7 field (bit 6).
        """
        return (self.reg >> 6) & 0x1

    @bit_0_7.setter
    def bit_0_7(self, value):
        """
        Set the 1-bit bit_0_7 field (bit 6).
        """
        self.reg = (self.reg & ~(0x1 << 6)) | ((value & 0x1) << 6)

    # OTP1
    @property
    def bit_1_0to3(self):
        """
        Get the 4-bit bit_1_0to3 field (bits 8–11).
        """
        return (self.reg >> 8) & 0xF

    @bit_1_0to3.setter
    def bit_1_0to3(self, value):
        """
        Set the 4-bit bit_1_0to3 field (bits 8–11).
        """
        self.reg = (self.reg & ~(0xF << 8)) | ((value & 0xF) << 8)

    @property
    def bit_1_4(self):
        """
        Get the 1-bit bit_1_4 field (bit 12).
        """
        return (self.reg >> 12) & 0x1

    @bit_1_4.setter
    def bit_1_4(self, value):
        """
        Set the 1-bit bit_1_4 field (bit 12).
        """
        self.reg = (self.reg & ~(0x1 << 12)) | ((value & 0x1) << 12)

    @property
    def bit_1_5to7(self):
        """
        Get the 3-bit bit_1_5to7 field (bits 13–15).
        """
        return (self.reg >> 13) & 0x7

    @bit_1_5to7.setter
    def bit_1_5to7(self, value):
        """
        Set the 3-bit bit_1_5to7 field (bits 13–15).
        """
        self.reg = (self.reg & ~(0x7 << 13)) | ((value & 0x7) << 13)

    # OTP2
    @property
    def bit_2_0(self):
        """
        Get the 1-bit bit_2_0 field (bit 16).
        """
        return (self.reg >> 16) & 0x1

    @bit_2_0.setter
    def bit_2_0(self, value):
        """
        Set the 1-bit bit_2_0 field (bit 16).
        """
        self.reg = (self.reg & ~(0x1 << 16)) | ((value & 0x1) << 16)

    @property
    def bit_2_1(self):
        """
        Get the 1-bit bit_2_1 field (bit 17).
        """
        return (self.reg >> 17) & 0x1

    @bit_2_1.setter
    def bit_2_1(self, value):
        """
        Set the 1-bit bit_2_1 field (bit 17).
        """
        self.reg = (self.reg & ~(0x1 << 17)) | ((value & 0x1) << 17)

    @property
    def bit_2_2(self):
        """
        Get the 1-bit bit_2_2 field (bit 18).
        """
        return (self.reg >> 18) & 0x1

    @bit_2_2.setter
    def bit_2_2(self, value):
        """
        Set the 1-bit bit_2_2 field (bit 18).
        """
        self.reg = (self.reg & ~(0x1 << 18)) | ((value & 0x1) << 18)

    @property
    def bit_2_3to4(self):
        """
        Get the 2-bit bit_2_3to4 field (bits 19–20).
        """
        return (self.reg >> 19) & 0x3

    @bit_2_3to4.setter
    def bit_2_3to4(self, value):
        """
        Set the 2-bit bit_2_3to4 field (bits 19–20).
        """
        self.reg = (self.reg & ~(0x3 << 19)) | ((value & 0x3) << 19)

    @property
    def bit_2_5to6(self):
        """
        Get the 2-bit bit_2_5to6 field (bits 21–22).
        """
        return (self.reg >> 21) & 0x3

    @bit_2_5to6.setter
    def bit_2_5to6(self, value):
        """
        Set the 2-bit bit_2_5to6 field (bits 21–22).
        """
        self.reg = (self.reg & ~(0x3 << 21)) | ((value & 0x3) << 21)

    @property
    def bit_2_7(self):
        """
        Get the 1-bit bit_2_7 field (bit 23).
        """
        return (self.reg >> 23) & 0x1

    @bit_2_7.setter
    def bit_2_7(self, value):
        """
        Set the 1-bit bit_2_7 field (bit 23).
        """
        self.reg = (self.reg & ~(0x1 << 23)) | ((value & 0x1) << 23)

    @property
    def reserved(self):
        """
        Get the 8-bit reserved field (bits 24–31).
        """
        return (self.reg >> 24) & 0xFF

    def __repr__(self):
        """
        String representation of the OTP_READ register showing bitfields and the full register value.
        """
        return (
            f"OTP_READ(reg={self.reg:032b}, bit_0_0to4={self.bit_0_0to4}, bit_0_5={self.bit_0_5}, "
            f"bit_0_6={self.bit_0_6}, bit_0_7={self.bit_0_7}, bit_1_0to3={self.bit_1_0to3}, "
            f"bit_1_4={self.bit_1_4}, bit_1_5to7={self.bit_1_5to7}, bit_2_0={self.bit_2_0}, "
            f"bit_2_1={self.bit_2_1}, bit_2_2={self.bit_2_2}, bit_2_3to4={self.bit_2_3to4}, "
            f"bit_2_5to6={self.bit_2_5to6}, bit_2_7={self.bit_2_7}, reserved={self.reserved:02X})"
        )


class IOIN:
    """
    Represents the IOIN register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the IOIN register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def ENN(self):
        """Get the 1-bit ENN field (bit 0)."""
        return (self.reg >> 0) & 0x1

    @ENN.setter
    def ENN(self, value):
        """Set the 1-bit ENN field (bit 0)."""
        self.reg = (self.reg & ~(0x1 << 0)) | ((value & 0x1) << 0)

    @property
    def FREE1(self):
        """Get the 1-bit FREE1 field (bit 1)."""
        return (self.reg >> 1) & 0x1

    @FREE1.setter
    def FREE1(self, value):
        """Set the 1-bit FREE1 field (bit 1)."""
        self.reg = (self.reg & ~(0x1 << 1)) | ((value & 0x1) << 1)

    @property
    def MS1(self):
        """Get the 1-bit MS1 field (bit 2)."""
        return (self.reg >> 2) & 0x1

    @MS1.setter
    def MS1(self, value):
        """Set the 1-bit MS1 field (bit 2)."""
        self.reg = (self.reg & ~(0x1 << 2)) | ((value & 0x1) << 2)

    @property
    def MS2(self):
        """Get the 1-bit MS2 field (bit 3)."""
        return (self.reg >> 3) & 0x1

    @MS2.setter
    def MS2(self, value):
        """Set the 1-bit MS2 field (bit 3)."""
        self.reg = (self.reg & ~(0x1 << 3)) | ((value & 0x1) << 3)

    @property
    def DIAG(self):
        """Get the 1-bit DIAG field (bit 4)."""
        return (self.reg >> 4) & 0x1

    @DIAG.setter
    def DIAG(self, value):
        """Set the 1-bit DIAG field (bit 4)."""
        self.reg = (self.reg & ~(0x1 << 4)) | ((value & 0x1) << 4)

    @property
    def FREE2(self):
        """Get the 1-bit FREE2 field (bit 5)."""
        return (self.reg >> 5) & 0x1

    @FREE2.setter
    def FREE2(self, value):
        """Set the 1-bit FREE2 field (bit 5)."""
        self.reg = (self.reg & ~(0x1 << 5)) | ((value & 0x1) << 5)

    @property
    def PDN_UART(self):
        """Get the 1-bit PDN_UART field (bit 6)."""
        return (self.reg >> 6) & 0x1

    @PDN_UART.setter
    def PDN_UART(self, value):
        """Set the 1-bit PDN_UART field (bit 6)."""
        self.reg = (self.reg & ~(0x1 << 6)) | ((value & 0x1) << 6)

    @property
    def STEP(self):
        """Get the 1-bit STEP field (bit 7)."""
        return (self.reg >> 7) & 0x1

    @STEP.setter
    def STEP(self, value):
        """Set the 1-bit STEP field (bit 7)."""
        self.reg = (self.reg & ~(0x1 << 7)) | ((value & 0x1) << 7)

    @property
    def SPREAD_EN(self):
        """Get the 1-bit SPREAD_EN field (bit 8)."""
        return (self.reg >> 8) & 0x1

    @SPREAD_EN.setter
    def SPREAD_EN(self, value):
        """Set the 1-bit SPREAD_EN field (bit 8)."""
        self.reg = (self.reg & ~(0x1 << 8)) | ((value & 0x1) << 8)

    @property
    def DIR(self):
        """Get the 1-bit DIR field (bit 9)."""
        return (self.reg >> 9) & 0x1

    @DIR.setter
    def DIR(self, value):
        """Set the 1-bit DIR field (bit 9)."""
        self.reg = (self.reg & ~(0x1 << 9)) | ((value & 0x1) << 9)

    @property
    def reserved1(self):
        """Get the 14-bit reserved1 field (bits 10–23)."""
        return (self.reg >> 10) & 0x3FFF

    @property
    def VERSION(self):
        """Get the 8-bit VERSION field (bits 24–31)."""
        return (self.reg >> 24) & 0xFF

    @VERSION.setter
    def VERSION(self, value):
        """Set the 8-bit VERSION field (bits 24–31)."""
        self.reg = (self.reg & ~(0xFF << 24)) | ((value & 0xFF) << 24)

    def __repr__(self):
        """
        String representation of the IOIN register showing bitfields and the full register value.
        """
        return (
            f"IOIN(reg={self.reg:032b}, ENN={self.ENN}, FREE1={self.FREE1}, MS1={self.MS1}, "
            f"MS2={self.MS2}, DIAG={self.DIAG}, FREE2={self.FREE2}, PDN_UART={self.PDN_UART}, "
            f"STEP={self.STEP}, SPREAD_EN={self.SPREAD_EN}, DIR={self.DIR}, reserved1={self.reserved1:04X}, "
            f"VERSION={self.VERSION})"
        )

class FACTORY_CONF:
    """
    Represents the FACTORY_CONF register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the FACTORY_CONF register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def FCLKTRIM(self):
        """Get the 5-bit FCLKTRIM field (bits 0–4)."""
        return (self.reg >> 0) & 0x1F

    @FCLKTRIM.setter
    def FCLKTRIM(self, value):
        """Set the 5-bit FCLKTRIM field (bits 0–4)."""
        self.reg = (self.reg & ~(0x1F << 0)) | ((value & 0x1F) << 0)

    @property
    def FREE(self):
        """Get the 3-bit FREE field (bits 5–7)."""
        return (self.reg >> 5) & 0x7

    @FREE.setter
    def FREE(self, value):
        """Set the 3-bit FREE field (bits 5–7)."""
        self.reg = (self.reg & ~(0x7 << 5)) | ((value & 0x7) << 5)

    @property
    def OTTRIM(self):
        """Get the 2-bit OTTRIM field (bits 8–9)."""
        return (self.reg >> 8) & 0x3

    @OTTRIM.setter
    def OTTRIM(self, value):
        """Set the 2-bit OTTRIM field (bits 8–9)."""
        self.reg = (self.reg & ~(0x3 << 8)) | ((value & 0x3) << 8)

    @property
    def reserved1(self):
        """Get the 14-bit reserved1 field (bits 10–23)."""
        return (self.reg >> 10) & 0x3FFF

    def __repr__(self):
        """
        String representation of the FACTORY_CONF register showing bitfields and the full register value.
        """
        return (
            f"FACTORY_CONF(reg={self.reg:032b}, FCLKTRIM={self.FCLKTRIM}, "
            f"FREE={self.FREE}, OTTRIM={self.OTTRIM}, reserved1={self.reserved1:04X})"
        )


class IHOLD_IRUN:
    """
    Represents the IHOLD_IRUN register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the IHOLD_IRUN register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def IHOLD(self):
        """Get the 5-bit IHOLD field (bits 0–4)."""
        return (self.reg >> 0) & 0x1F

    @IHOLD.setter
    def IHOLD(self, value):
        """Set the 5-bit IHOLD field (bits 0–4)."""
        self.reg = (self.reg & ~(0x1F << 0)) | ((value & 0x1F) << 0)

    @property
    def FREE1(self):
        """Get the 3-bit FREE1 field (bits 5–7)."""
        return (self.reg >> 5) & 0x7

    @FREE1.setter
    def FREE1(self, value):
        """Set the 3-bit FREE1 field (bits 5–7)."""
        self.reg = (self.reg & ~(0x7 << 5)) | ((value & 0x7) << 5)

    @property
    def IRUN(self):
        """Get the 5-bit IRUN field (bits 8–12)."""
        return (self.reg >> 8) & 0x1F

    @IRUN.setter
    def IRUN(self, value):
        """Set the 5-bit IRUN field (bits 8–12)."""
        self.reg = (self.reg & ~(0x1F << 8)) | ((value & 0x1F) << 8)

    @property
    def FREE2(self):
        """Get the 3-bit FREE2 field (bits 13–15)."""
        return (self.reg >> 13) & 0x7

    @FREE2.setter
    def FREE2(self, value):
        """Set the 3-bit FREE2 field (bits 13–15)."""
        self.reg = (self.reg & ~(0x7 << 13)) | ((value & 0x7) << 13)

    @property
    def IHOLDDELAY(self):
        """Get the 4-bit IHOLDDELAY field (bits 16–19)."""
        return (self.reg >> 16) & 0xF

    @IHOLDDELAY.setter
    def IHOLDDELAY(self, value):
        """Set the 4-bit IHOLDDELAY field (bits 16–19)."""
        self.reg = (self.reg & ~(0xF << 16)) | ((value & 0xF) << 16)

    @property
    def reserved1(self):
        """Get the 12-bit reserved1 field (bits 20–31)."""
        return (self.reg >> 20) & 0xFFF

    def __repr__(self):
        """
        String representation of the IHOLD_IRUN register showing bitfields and the full register value.
        """
        return (
            f"IHOLD_IRUN(reg={self.reg:032b}, IHOLD={self.IHOLD}, FREE1={self.FREE1}, "
            f"IRUN={self.IRUN}, FREE2={self.FREE2}, IHOLDDELAY={self.IHOLDDELAY}, "
            f"reserved1={self.reserved1:03X})"
        )


class TPOWERDOWN:
    """
    Represents the TPOWERDOWN register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the TPOWERDOWN register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def TPOWERDOWN(self):
        """Get the 8-bit TPOWERDOWN field (bits 0–7)."""
        return (self.reg >> 0) & 0xFF

    @TPOWERDOWN.setter
    def TPOWERDOWN(self, value):
        """Set the 8-bit TPOWERDOWN field (bits 0–7)."""
        self.reg = (self.reg & ~(0xFF << 0)) | ((value & 0xFF) << 0)

    @property
    def reserved1(self):
        """Get the 24-bit reserved1 field (bits 8–31)."""
        return (self.reg >> 8) & 0xFFFFFF

    def __repr__(self):
        """
        String representation of the TPOWERDOWN register showing bitfields and the full register value.
        """
        return (
            f"TPOWERDOWN(reg={self.reg:032b}, TPOWERDOWN={self.TPOWERDOWN}, reserved1={self.reserved1:06X})"
        )

class TSTEP:
    """
    Represents the TSTEP register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the TSTEP register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def TSTEP(self):
        """Get the 20-bit TSTEP field (bits 0–19)."""
        return (self.reg >> 0) & 0xFFFFF

    @TSTEP.setter
    def TSTEP(self, value):
        """Set the 20-bit TSTEP field (bits 0–19)."""
        self.reg = (self.reg & ~(0xFFFFF << 0)) | ((value & 0xFFFFF) << 0)

    @property
    def reserved1(self):
        """Get the 12-bit reserved1 field (bits 20–31)."""
        return (self.reg >> 20) & 0xFFF

    def __repr__(self):
        """
        String representation of the TSTEP register showing bitfields and the full register value.
        """
        return (
            f"TSTEP(reg={self.reg:032b}, TSTEP={self.TSTEP}, reserved1={self.reserved1:03X})"
        )

class TPWMTHRS:
    """
    Represents the TPWMTHRS register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the TPWMTHRS register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def TPWMTHRS(self):
        """Get the 20-bit TPWMTHRS field (bits 0–19)."""
        return (self.reg >> 0) & 0xFFFFF

    @TPWMTHRS.setter
    def TPWMTHRS(self, value):
        """Set the 20-bit TPWMTHRS field (bits 0–19)."""
        self.reg = (self.reg & ~(0xFFFFF << 0)) | ((value & 0xFFFFF) << 0)

    @property
    def reserved1(self):
        """Get the 12-bit reserved1 field (bits 20–31)."""
        return (self.reg >> 20) & 0xFFF

    def __repr__(self):
        """
        String representation of the TPWMTHRS register showing bitfields and the full register value.
        """
        return (
            f"TPWMTHRS(reg={self.reg:032b}, TPWMTHRS={self.TPWMTHRS}, reserved1={self.reserved1:03X})"
        )

class VACTUAL:
    """
    Represents the VACTUAL register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the VACTUAL register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def VACTUAL(self):
        """Get the 24-bit VACTUAL field (bits 0–23)."""
        return (self.reg >> 0) & 0xFFFFFF

    @VACTUAL.setter
    def VACTUAL(self, value):
        """Set the 24-bit VACTUAL field (bits 0–23)."""
        self.reg = (self.reg & ~(0xFFFFFF << 0)) | ((value & 0xFFFFFF) << 0)

    @property
    def reserved(self):
        """Get the 8-bit reserved field (bits 24–31)."""
        return (self.reg >> 24) & 0xFF

    def __repr__(self):
        """
        String representation of the VACTUAL register showing bitfields and the full register value.
        """
        return (
            f"VACTUAL(reg={self.reg:032b}, VACTUAL={self.VACTUAL}, reserved={self.reserved:02X})"
        )

class TCOOLTHRS:
    """
    Represents the TCOOLTHRS register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the TCOOLTHRS register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def TCOOLTHRS(self):
        """Get the 24-bit TCOOLTHRS field (bits 0–23)."""
        return (self.reg >> 0) & 0xFFFFFF

    @TCOOLTHRS.setter
    def TCOOLTHRS(self, value):
        """Set the 24-bit TCOOLTHRS field (bits 0–23)."""
        self.reg = (self.reg & ~(0xFFFFFF << 0)) | ((value & 0xFFFFFF) << 0)

    @property
    def reserved(self):
        """Get the 8-bit reserved field (bits 24–31)."""
        return (self.reg >> 24) & 0xFF

    def __repr__(self):
        """
        String representation of the TCOOLTHRS register showing bitfields and the full register value.
        """
        return (
            f"TCOOLTHRS(reg={self.reg:032b}, TCOOLTHRS={self.TCOOLTHRS}, reserved={self.reserved:02X})"
        )

class SGTHRS:
    """
    Represents the SGTHRS register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the SGTHRS register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def SGTHRS(self):
        """Get the 8-bit SGTHRS field (bits 0–7)."""
        return (self.reg >> 0) & 0xFF

    @SGTHRS.setter
    def SGTHRS(self, value):
        """Set the 8-bit SGTHRS field (bits 0–7)."""
        self.reg = (self.reg & ~(0xFF << 0)) | ((value & 0xFF) << 0)

    @property
    def reserved(self):
        """Get the 24-bit reserved field (bits 8–31)."""
        return (self.reg >> 8) & 0xFFFFFF

    def __repr__(self):
        """
        String representation of the SGTHRS register showing bitfields and the full register value.
        """
        return (
            f"SGTHRS(reg={self.reg:032b}, SGTHRS={self.SGTHRS}, reserved={self.reserved:06X})"
        )

class SG_RESULT:
    """
    Represents the SG_RESULT register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the SG_RESULT register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def SG_RESULT(self):
        """Get the 10-bit SG_RESULT field (bits 0–9)."""
        return (self.reg >> 0) & 0x3FF

    @SG_RESULT.setter
    def SG_RESULT(self, value):
        """Set the 10-bit SG_RESULT field (bits 0–9)."""
        self.reg = (self.reg & ~(0x3FF << 0)) | ((value & 0x3FF) << 0)

    @property
    def reserved(self):
        """Get the 22-bit reserved field (bits 10–31)."""
        return (self.reg >> 10) & 0x3FFFFF

    def __repr__(self):
        """
        String representation of the SG_RESULT register showing bitfields and the full register value.
        """
        return (
            f"SG_RESULT(reg={self.reg:032b}, SG_RESULT={self.SG_RESULT}, reserved={self.reserved:06X})"
        )

class COOLCONF:
    """
    Represents the COOLCONF register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the COOLCONF register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def semin(self):
        """Get the 4-bit semin field (bits 0–3)."""
        return (self.reg >> 0) & 0xF

    @semin.setter
    def semin(self, value):
        """Set the 4-bit semin field (bits 0–3)."""
        self.reg = (self.reg & ~(0xF << 0)) | ((value & 0xF) << 0)

    @property
    def reserved1(self):
        """Get the 1-bit reserved1 field (bit 4)."""
        return (self.reg >> 4) & 0x1

    @property
    def seup(self):
        """Get the 2-bit seup field (bits 5–6)."""
        return (self.reg >> 5) & 0x3

    @seup.setter
    def seup(self, value):
        """Set the 2-bit seup field (bits 5–6)."""
        self.reg = (self.reg & ~(0x3 << 5)) | ((value & 0x3) << 5)

    @property
    def reserved2(self):
        """Get the 1-bit reserved2 field (bit 7)."""
        return (self.reg >> 7) & 0x1

    @property
    def semax(self):
        """Get the 4-bit semax field (bits 8–11)."""
        return (self.reg >> 8) & 0xF

    @semax.setter
    def semax(self, value):
        """Set the 4-bit semax field (bits 8–11)."""
        self.reg = (self.reg & ~(0xF << 8)) | ((value & 0xF) << 8)

    @property
    def reserved3(self):
        """Get the 1-bit reserved3 field (bit 12)."""
        return (self.reg >> 12) & 0x1

    @property
    def sedn(self):
        """Get the 2-bit sedn field (bits 13–14)."""
        return (self.reg >> 13) & 0x3

    @sedn.setter
    def sedn(self, value):
        """Set the 2-bit sedn field (bits 13–14)."""
        self.reg = (self.reg & ~(0x3 << 13)) | ((value & 0x3) << 13)

    @property
    def seimin(self):
        """Get the 1-bit seimin field (bit 15)."""
        return (self.reg >> 15) & 0x1

    @seimin.setter
    def seimin(self, value):
        """Set the 1-bit seimin field (bit 15)."""
        self.reg = (self.reg & ~(0x1 << 15)) | ((value & 0x1) << 15)

    @property
    def reserved4(self):
        """Get the 1-bit reserved4 field (bit 16)."""
        return (self.reg >> 16) & 0x1

    @property
    def reserved(self):
        """Get the 15-bit reserved field (bits 17–31)."""
        return (self.reg >> 17) & 0x7FFF

    def __repr__(self):
        """
        String representation of the COOLCONF register showing bitfields and the full register value.
        """
        return (
            f"COOLCONF(reg={self.reg:032b}, semin={self.semin}, reserved1={self.reserved1}, "
            f"seup={self.seup}, reserved2={self.reserved2}, semax={self.semax}, reserved3={self.reserved3}, "
            f"sedn={self.sedn}, seimin={self.seimin}, reserved4={self.reserved4}, reserved={self.reserved:05X})"
        )

class MSCNT:
    """
    Represents the MSCNT register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the MSCNT register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def MSCNT(self):
        """Get the 10-bit MSCNT field (bits 0–9)."""
        return (self.reg >> 0) & 0x3FF

    @MSCNT.setter
    def MSCNT(self, value):
        """Set the 10-bit MSCNT field (bits 0–9)."""
        self.reg = (self.reg & ~(0x3FF << 0)) | ((value & 0x3FF) << 0)

    @property
    def reserved(self):
        """Get the 22-bit reserved field (bits 10–31)."""
        return (self.reg >> 10) & 0x3FFFFF

    def __repr__(self):
        """
        String representation of the MSCNT register showing bitfields and the full register value.
        """
        return (
            f"MSCNT(reg={self.reg:032b}, MSCNT={self.MSCNT}, reserved={self.reserved:06X})"
        )

class MSCURACT:
    """
    Represents the MSCURACT register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the MSCURACT register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def CUR_B(self):
        """Get the 8-bit CUR_B field (bits 0–7)."""
        return (self.reg >> 0) & 0xFF

    @CUR_B.setter
    def CUR_B(self, value):
        """Set the 8-bit CUR_B field (bits 0–7)."""
        self.reg = (self.reg & ~(0xFF << 0)) | ((value & 0xFF) << 0)

    @property
    def CUR_B_sign(self):
        """Get the 1-bit CUR_B_sign field (bit 8)."""
        return (self.reg >> 8) & 0x1

    @CUR_B_sign.setter
    def CUR_B_sign(self, value):
        """Set the 1-bit CUR_B_sign field (bit 8)."""
        self.reg = (self.reg & ~(0x1 << 8)) | ((value & 0x1) << 8)

    @property
    def FREE(self):
        """Get the 7-bit FREE field (bits 9–15)."""
        return (self.reg >> 9) & 0x7F

    @FREE.setter
    def FREE(self, value):
        """Set the 7-bit FREE field (bits 9–15)."""
        self.reg = (self.reg & ~(0x7F << 9)) | ((value & 0x7F) << 9)

    @property
    def CUR_A(self):
        """Get the 8-bit CUR_A field (bits 16–23)."""
        return (self.reg >> 16) & 0xFF

    @CUR_A.setter
    def CUR_A(self, value):
        """Set the 8-bit CUR_A field (bits 16–23)."""
        self.reg = (self.reg & ~(0xFF << 16)) | ((value & 0xFF) << 16)

    @property
    def CUR_A_sign(self):
        """Get the 1-bit CUR_A_sign field (bit 24)."""
        return (self.reg >> 24) & 0x1

    @CUR_A_sign.setter
    def CUR_A_sign(self, value):
        """Set the 1-bit CUR_A_sign field (bit 24)."""
        self.reg = (self.reg & ~(0x1 << 24)) | ((value & 0x1) << 24)

    @property
    def reserved(self):
        """Get the 7-bit reserved field (bits 25–31)."""
        return (self.reg >> 25) & 0x7F

    def __repr__(self):
        """
        String representation of the MSCURACT register showing bitfields and the full register value.
        """
        return (
            f"MSCURACT(reg={self.reg:032b}, CUR_B={self.CUR_B}, CUR_B_sign={self.CUR_B_sign}, "
            f"FREE={self.FREE}, CUR_A={self.CUR_A}, CUR_A_sign={self.CUR_A_sign}, reserved={self.reserved:02X})"
        )

class CHOPCONF:
    """
    Represents the CHOPCONF register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the CHOPCONF register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def toff(self):
        """Get the 4-bit toff field (bits 0–3)."""
        return (self.reg >> 0) & 0xF

    @toff.setter
    def toff(self, value):
        """Set the 4-bit toff field (bits 0–3)."""
        self.reg = (self.reg & ~(0xF << 0)) | ((value & 0xF) << 0)

    @property
    def hstrt(self):
        """Get the 3-bit hstrt field (bits 4–6)."""
        return (self.reg >> 4) & 0x7

    @hstrt.setter
    def hstrt(self, value):
        """Set the 3-bit hstrt field (bits 4–6)."""
        self.reg = (self.reg & ~(0x7 << 4)) | ((value & 0x7) << 4)

    @property
    def hend(self):
        """Get the 4-bit hend field (bits 7–10)."""
        return (self.reg >> 7) & 0xF

    @hend.setter
    def hend(self, value):
        """Set the 4-bit hend field (bits 7–10)."""
        self.reg = (self.reg & ~(0xF << 7)) | ((value & 0xF) << 7)

    @property
    def tbl(self):
        """Get the 2-bit tbl field (bits 11–12)."""
        return (self.reg >> 11) & 0x3

    @tbl.setter
    def tbl(self, value):
        """Set the 2-bit tbl field (bits 11–12)."""
        self.reg = (self.reg & ~(0x3 << 11)) | ((value & 0x3) << 11)

    @property
    def vsense(self):
        """Get the 1-bit vsense field (bit 13)."""
        return (self.reg >> 13) & 0x1

    @vsense.setter
    def vsense(self, value):
        """Set the 1-bit vsense field (bit 13)."""
        self.reg = (self.reg & ~(0x1 << 13)) | ((value & 0x1) << 13)

    @property
    def mres(self):
        """Get the 4-bit mres field (bits 19–22)."""
        return (self.reg >> 19) & 0xF

    @mres.setter
    def mres(self, value):
        """Set the 4-bit mres field (bits 19–22)."""
        self.reg = (self.reg & ~(0xF << 19)) | ((value & 0xF) << 19)

    @property
    def intpol(self):
        """Get the 1-bit intpol field (bit 23)."""
        return (self.reg >> 23) & 0x1

    @intpol.setter
    def intpol(self, value):
        """Set the 1-bit intpol field (bit 23)."""
        self.reg = (self.reg & ~(0x1 << 23)) | ((value & 0x1) << 23)

    @property
    def dedge(self):
        """Get the 1-bit dedge field (bit 24)."""
        return (self.reg >> 24) & 0x1

    @dedge.setter
    def dedge(self, value):
        """Set the 1-bit dedge field (bit 24)."""
        self.reg = (self.reg & ~(0x1 << 24)) | ((value & 0x1) << 24)

    @property
    def diss2g(self):
        """Get the 1-bit diss2g field (bit 25)."""
        return (self.reg >> 25) & 0x1

    @diss2g.setter
    def diss2g(self, value):
        """Set the 1-bit diss2g field (bit 25)."""
        self.reg = (self.reg & ~(0x1 << 25)) | ((value & 0x1) << 25)

    @property
    def diss2vs(self):
        """Get the 1-bit diss2vs field (bit 26)."""
        return (self.reg >> 26) & 0x1

    @diss2vs.setter
    def diss2vs(self, value):
        """Set the 1-bit diss2vs field (bit 26)."""
        self.reg = (self.reg & ~(0x1 << 26)) | ((value & 0x1) << 26)

    def __repr__(self):
        """
        String representation of the CHOPCONF register showing bitfields and the full register value.
        """
        return (
            f"CHOPCONF(reg={self.reg:032b}, toff={self.toff}, hstrt={self.hstrt}, hend={self.hend}, "
            f"tbl={self.tbl}, vsense={self.vsense}, mres={self.mres}, intpol={self.intpol}, "
            f"dedge={self.dedge}, diss2g={self.diss2g}, diss2vs={self.diss2vs})"
        )

class DRV_STATUS:
    """
    Represents the DRV_STATUS register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the DRV_STATUS register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def otpw(self):
        """Get the 1-bit otpw field (bit 0)."""
        return (self.reg >> 0) & 0x1

    @otpw.setter
    def otpw(self, value):
        """Set the 1-bit otpw field (bit 0)."""
        self.reg = (self.reg & ~(0x1 << 0)) | ((value & 0x1) << 0)

    @property
    def ot(self):
        """Get the 1-bit ot field (bit 1)."""
        return (self.reg >> 1) & 0x1

    @ot.setter
    def ot(self, value):
        """Set the 1-bit ot field (bit 1)."""
        self.reg = (self.reg & ~(0x1 << 1)) | ((value & 0x1) << 1)

    @property
    def s2ga(self):
        """Get the 1-bit s2ga field (bit 2)."""
        return (self.reg >> 2) & 0x1

    @s2ga.setter
    def s2ga(self, value):
        """Set the 1-bit s2ga field (bit 2)."""
        self.reg = (self.reg & ~(0x1 << 2)) | ((value & 0x1) << 2)

    @property
    def s2gb(self):
        """Get the 1-bit s2gb field (bit 3)."""
        return (self.reg >> 3) & 0x1

    @s2gb.setter
    def s2gb(self, value):
        """Set the 1-bit s2gb field (bit 3)."""
        self.reg = (self.reg & ~(0x1 << 3)) | ((value & 0x1) << 3)

    @property
    def s2vsa(self):
        """Get the 1-bit s2vsa field (bit 4)."""
        return (self.reg >> 4) & 0x1

    @s2vsa.setter
    def s2vsa(self, value):
        """Set the 1-bit s2vsa field (bit 4)."""
        self.reg = (self.reg & ~(0x1 << 4)) | ((value & 0x1) << 4)

    @property
    def s2vsb(self):
        """Get the 1-bit s2vsb field (bit 5)."""
        return (self.reg >> 5) & 0x1

    @s2vsb.setter
    def s2vsb(self, value):
        """Set the 1-bit s2vsb field (bit 5)."""
        self.reg = (self.reg & ~(0x1 << 5)) | ((value & 0x1) << 5)

    @property
    def ola(self):
        """Get the 1-bit ola field (bit 6)."""
        return (self.reg >> 6) & 0x1

    @ola.setter
    def ola(self, value):
        """Set the 1-bit ola field (bit 6)."""
        self.reg = (self.reg & ~(0x1 << 6)) | ((value & 0x1) << 6)

    @property
    def olb(self):
        """Get the 1-bit olb field (bit 7)."""
        return (self.reg >> 7) & 0x1

    @olb.setter
    def olb(self, value):
        """Set the 1-bit olb field (bit 7)."""
        self.reg = (self.reg & ~(0x1 << 7)) | ((value & 0x1) << 7)

    @property
    def t120(self):
        """Get the 1-bit t120 field (bit 8)."""
        return (self.reg >> 8) & 0x1

    @t120.setter
    def t120(self, value):
        """Set the 1-bit t120 field (bit 8)."""
        self.reg = (self.reg & ~(0x1 << 8)) | ((value & 0x1) << 8)

    @property
    def t143(self):
        """Get the 1-bit t143 field (bit 9)."""
        return (self.reg >> 9) & 0x1

    @t143.setter
    def t143(self, value):
        """Set the 1-bit t143 field (bit 9)."""
        self.reg = (self.reg & ~(0x1 << 9)) | ((value & 0x1) << 9)

    @property
    def t150(self):
        """Get the 1-bit t150 field (bit 10)."""
        return (self.reg >> 10) & 0x1

    @t150.setter
    def t150(self, value):
        """Set the 1-bit t150 field (bit 10)."""
        self.reg = (self.reg & ~(0x1 << 10)) | ((value & 0x1) << 10)

    @property
    def t157(self):
        """Get the 1-bit t157 field (bit 11)."""
        return (self.reg >> 11) & 0x1

    @t157.setter
    def t157(self, value):
        """Set the 1-bit t157 field (bit 11)."""
        self.reg = (self.reg & ~(0x1 << 11)) | ((value & 0x1) << 11)

    @property
    def CS_ACTUAL(self):
        """Get the 5-bit CS_ACTUAL field (bits 16–20)."""
        return (self.reg >> 16) & 0x1F

    @CS_ACTUAL.setter
    def CS_ACTUAL(self, value):
        """Set the 5-bit CS_ACTUAL field (bits 16–20)."""
        self.reg = (self.reg & ~(0x1F << 16)) | ((value & 0x1F) << 16)

    @property
    def stealth(self):
        """Get the 1-bit stealth field (bit 30)."""
        return (self.reg >> 30) & 0x1

    @stealth.setter
    def stealth(self, value):
        """Set the 1-bit stealth field (bit 30)."""
        self.reg = (self.reg & ~(0x1 << 30)) | ((value & 0x1) << 30)

    @property
    def stst(self):
        """Get the 1-bit stst field (bit 31)."""
        return (self.reg >> 31) & 0x1

    @stst.setter
    def stst(self, value):
        """Set the 1-bit stst field (bit 31)."""
        self.reg = (self.reg & ~(0x1 << 31)) | ((value & 0x1) << 31)

    def __repr__(self):
        """
        String representation of the DRV_STATUS register showing bitfields and the full register value.
        """
        return (
            f"DRV_STATUS(reg={self.reg:032b}, otpw={self.otpw}, ot={self.ot}, s2ga={self.s2ga}, "
            f"s2gb={self.s2gb}, s2vsa={self.s2vsa}, s2vsb={self.s2vsb}, ola={self.ola}, "
            f"olb={self.olb}, t120={self.t120}, t143={self.t143}, t150={self.t150}, "
            f"t157={self.t157}, CS_ACTUAL={self.CS_ACTUAL}, stealth={self.stealth}, stst={self.stst})"
        )

class PWMCONF:
    """
    Represents the PWMCONF register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the PWMCONF register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def PWM_OFS(self):
        """Get the 8-bit PWM_OFS field (bits 0–7)."""
        return (self.reg >> 0) & 0xFF

    @PWM_OFS.setter
    def PWM_OFS(self, value):
        """Set the 8-bit PWM_OFS field (bits 0–7)."""
        self.reg = (self.reg & ~(0xFF << 0)) | ((value & 0xFF) << 0)

    @property
    def PWM_GRAD(self):
        """Get the 8-bit PWM_GRAD field (bits 8–15)."""
        return (self.reg >> 8) & 0xFF

    @PWM_GRAD.setter
    def PWM_GRAD(self, value):
        """Set the 8-bit PWM_GRAD field (bits 8–15)."""
        self.reg = (self.reg & ~(0xFF << 8)) | ((value & 0xFF) << 8)

    @property
    def PWM_FREQ(self):
        """Get the 2-bit PWM_FREQ field (bits 16–17)."""
        return (self.reg >> 16) & 0x3

    @PWM_FREQ.setter
    def PWM_FREQ(self, value):
        """Set the 2-bit PWM_FREQ field (bits 16–17)."""
        self.reg = (self.reg & ~(0x3 << 16)) | ((value & 0x3) << 16)

    @property
    def PWM_autoscale(self):
        """Get the 1-bit PWM_autoscale field (bit 18)."""
        return (self.reg >> 18) & 0x1

    @PWM_autoscale.setter
    def PWM_autoscale(self, value):
        """Set the 1-bit PWM_autoscale field (bit 18)."""
        self.reg = (self.reg & ~(0x1 << 18)) | ((value & 0x1) << 18)

    @property
    def PWM_autograd(self):
        """Get the 1-bit PWM_autograd field (bit 19)."""
        return (self.reg >> 19) & 0x1

    @PWM_autograd.setter
    def PWM_autograd(self, value):
        """Set the 1-bit PWM_autograd field (bit 19)."""
        self.reg = (self.reg & ~(0x1 << 19)) | ((value & 0x1) << 19)

    @property
    def freewheel(self):
        """Get the 2-bit freewheel field (bits 20–21)."""
        return (self.reg >> 20) & 0x3

    @freewheel.setter
    def freewheel(self, value):
        """Set the 2-bit freewheel field (bits 20–21)."""
        self.reg = (self.reg & ~(0x3 << 20)) | ((value & 0x3) << 20)

    @property
    def reserved(self):
        """Get the 2-bit reserved field (bits 22–23)."""
        return (self.reg >> 22) & 0x3

    @property
    def PWM_REG(self):
        """Get the 4-bit PWM_REG field (bits 24–27)."""
        return (self.reg >> 24) & 0xF

    @PWM_REG.setter
    def PWM_REG(self, value):
        """Set the 4-bit PWM_REG field (bits 24–27)."""
        self.reg = (self.reg & ~(0xF << 24)) | ((value & 0xF) << 24)

    @property
    def PWM_LIM(self):
        """Get the 4-bit PWM_LIM field (bits 28–31)."""
        return (self.reg >> 28) & 0xF

    @PWM_LIM.setter
    def PWM_LIM(self, value):
        """Set the 4-bit PWM_LIM field (bits 28–31)."""
        self.reg = (self.reg & ~(0xF << 28)) | ((value & 0xF) << 28)

    def __repr__(self):
        """
        String representation of the PWMCONF register showing bitfields and the full register value.
        """
        return (
            f"PWMCONF(reg={self.reg:032b}, PWM_OFS={self.PWM_OFS}, PWM_GRAD={self.PWM_GRAD}, "
            f"PWM_FREQ={self.PWM_FREQ}, PWM_autoscale={self.PWM_autoscale}, PWM_autograd={self.PWM_autograd}, "
            f"freewheel={self.freewheel}, reserved={self.reserved:02X}, PWM_REG={self.PWM_REG}, PWM_LIM={self.PWM_LIM})"
        )


class PWM_SCALE:
    """
    Represents the PWM_SCALE register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the PWM_SCALE register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def PWM_SCALE_SUM(self):
        """Get the 8-bit PWM_SCALE_SUM field (bits 0–7)."""
        return (self.reg >> 0) & 0xFF

    @PWM_SCALE_SUM.setter
    def PWM_SCALE_SUM(self, value):
        """Set the 8-bit PWM_SCALE_SUM field (bits 0–7)."""
        self.reg = (self.reg & ~(0xFF << 0)) | ((value & 0xFF) << 0)

    @property
    def FREE(self):
        """Get the 8-bit FREE field (bits 8–15)."""
        return (self.reg >> 8) & 0xFF

    @FREE.setter
    def FREE(self, value):
        """Set the 8-bit FREE field (bits 8–15)."""
        self.reg = (self.reg & ~(0xFF << 8)) | ((value & 0xFF) << 8)

    @property
    def PWM_SCALE_AUTO(self):
        """Get the 8-bit PWM_SCALE_AUTO field (bits 16–23)."""
        return (self.reg >> 16) & 0xFF

    @PWM_SCALE_AUTO.setter
    def PWM_SCALE_AUTO(self, value):
        """Set the 8-bit PWM_SCALE_AUTO field (bits 16–23)."""
        self.reg = (self.reg & ~(0xFF << 16)) | ((value & 0xFF) << 16)

    @property
    def PWM_SCALE_AUTO_sign(self):
        """Get the 1-bit PWM_SCALE_AUTO_sign field (bit 24)."""
        return (self.reg >> 24) & 0x1

    @PWM_SCALE_AUTO_sign.setter
    def PWM_SCALE_AUTO_sign(self, value):
        """Set the 1-bit PWM_SCALE_AUTO_sign field (bit 24)."""
        self.reg = (self.reg & ~(0x1 << 24)) | ((value & 0x1) << 24)

    @property
    def reserved(self):
        """Get the 7-bit reserved field (bits 25–31)."""
        return (self.reg >> 25) & 0x7F

    def __repr__(self):
        """
        String representation of the PWM_SCALE register showing bitfields and the full register value.
        """
        return (
            f"PWM_SCALE(reg={self.reg:032b}, PWM_SCALE_SUM={self.PWM_SCALE_SUM}, "
            f"FREE={self.FREE}, PWM_SCALE_AUTO={self.PWM_SCALE_AUTO}, "
            f"PWM_SCALE_AUTO_sign={self.PWM_SCALE_AUTO_sign}, reserved={self.reserved:02X})"
        )

class PWM_AUTO:
    """
    Represents the PWM_AUTO register of TMC2209 with bitfields.
    """
    def __init__(self, reg=0):
        """
        Initialize the PWM_AUTO register with an optional default value.
        :param reg: Initial 32-bit register value (default is 0).
        """
        self.reg = reg

    @property
    def PWM_OFC_AUTO(self):
        """Get the 8-bit PWM_OFC_AUTO field (bits 0–7)."""
        return (self.reg >> 0) & 0xFF

    @PWM_OFC_AUTO.setter
    def PWM_OFC_AUTO(self, value):
        """Set the 8-bit PWM_OFC_AUTO field (bits 0–7)."""
        self.reg = (self.reg & ~(0xFF << 0)) | ((value & 0xFF) << 0)

    @property
    def FREE(self):
        """Get the 9-bit FREE field (bits 8–16)."""
        return (self.reg >> 8) & 0x1FF

    @FREE.setter
    def FREE(self, value):
        """Set the 9-bit FREE field (bits 8–16)."""
        self.reg = (self.reg & ~(0x1FF << 8)) | ((value & 0x1FF) << 8)

    @property
    def PWM_GRAD_AUTO(self):
        """Get the 8-bit PWM_GRAD_AUTO field (bits 17–24)."""
        return (self.reg >> 17) & 0xFF

    @PWM_GRAD_AUTO.setter
    def PWM_GRAD_AUTO(self, value):
        """Set the 8-bit PWM_GRAD_AUTO field (bits 17–24)."""
        self.reg = (self.reg & ~(0xFF << 17)) | ((value & 0xFF) << 17)

    @property
    def reserved(self):
        """Get the 8-bit reserved field (bits 25–31)."""
        return (self.reg >> 25) & 0x7F

    def __repr__(self):
        """
        String representation of the PWM_AUTO register showing bitfields and the full register value.
        """
        return (
            f"PWM_AUTO(reg={self.reg:032b}, PWM_OFC_AUTO={self.PWM_OFC_AUTO}, "
            f"FREE={self.FREE:03X}, PWM_GRAD_AUTO={self.PWM_GRAD_AUTO}, reserved={self.reserved:02X})"
        )
