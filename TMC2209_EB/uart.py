import serial

class UART:
    """
    Represents a UART communication interface using the pyserial library.
    """
    def __init__(self, port: str, baudrate: int = 115200, timeout: float = 1.0):
        """
        Initialize the UART connection.

        :param port: UART port (e.g., "COM3" or "/dev/ttyS0").
        :param baudrate: Baud rate for communication.
        :param timeout: Read timeout in seconds.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)

    def write(self, data: bytes):
        """
        Write data to the UART.

        :param data: Byte array to send.
        """
        if not self.connection.is_open:
            self.connection.open()
        self.connection.write(data)

    def read(self, size: int) -> bytes:
        """
        Read data from the UART.

        :param size: Number of bytes to read.
        :return: Received byte array.
        """
        if not self.connection.is_open:
            self.connection.open()
        return self.connection.read(size)

    def close(self):
        """
        Close the UART connection.
        """
        if self.connection.is_open:
            self.connection.close()

    def __repr__(self):
        return f"UART(port={self.port}, baudrate={self.baudrate}, timeout={self.timeout})"
