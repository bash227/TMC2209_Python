
# **TMC2209 Python Library**
A Python library to configure and communicate with the TMC2209 stepper motor driver via UART. This library enables reading and writing to the TMC2209 registers, configuring microstepping, and setting driver parameters.

## __Features__
- **Read and write registers** of TMC2209
- **Configure driver settings** (e.g., current, voltage, microsteps)
- **UART communication** with TMC2209
- **Register-level access and control**
## **Installation**
This library depends on **pyserial** for UART communication. Install the required dependencies using:
```bash
pip install pyserial
```

## __Before usage__
Please read the [datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/tmc2209_datasheet_rev1.09.pdf) of TMC2209 to understand the registers and their bits
## __Usage__
### 1. Initialize UART Communication
First, create a **UART** instance to establish serial communication.
```python
from uart import UART

uart = UART(port="/dev/ttyS0")  # Use appropriate port
```
### 2. Configure the TMC2209 Driver
Create an instance of **TMC2209Configure** to control the stepper motor.

```python
from TMC2209 import TMC2209Configure

tmc = TMC2209Configure(uart=uart, MS1=17, MS2=27, EN=22, node_address=0x00)
```
### 3. Initialize and Configure the Driver
To set up the motor driver:

```python
tmc.initialize()
```
You can use this function to make sure that the connections are correct
### 4. Reading and Writing Registers
#### 1. __Writing to a Register__

To write to a register, follow these steps:

1. Set or reset the desired bits.
2. Send the updated register values.

#### Syntax:
```python
tmcModel.<RegisterName>.<BitName> = <Value>  # Set the bit in the register
tmcModel.write_<RegisterName>()  # Write the updated register value
```

#### Example:
```python
tmc.gconf.shaft = 1 # Setting the shaft bit in GCONF register to reverse the direction
tmc.write_GCONF()  # Writes GCONF register settings
```

#### 2. __Reading a Register__
To read the value of a register, follow these steps:
1. Call the corresponding `read_<RegisterName>()` function.
2. Store the returned value in a variable.

#### Syntax:
```python
<variable_name> = tmc.read_<RegisterName>()  # Read the register value
```

#### Example:
```python
gstat_value = tmc.read_GSTAT()
print(f"GSTAT Register Value: {gstat_value}")
```

### 5. Closing the UART Connection
```python
uart.close()
```


## __Full Example Code__

Below is a complete example that:
- **Initializes** the UART connection.
- **Configures** the TMC2209 driver.
- **Writes to the VACTUAL register** to move the motor.
- **Reads a register value**.
- **Closes the UART connection** when done.

```python
from uart import UART
from TMC2209 import TMC2209Configure

# Initialize UART communication
uart = UART(port="/dev/ttyS0")

# Configure the TMC2209 driver
tmc = TMC2209Configure(uart=uart, MS1=17, MS2=27, EN=22, node_address=0x00)

# Initialize the driver settings
tmc.initialize()

# Example: Writing 1000 to VACTUAL register in order to move the motor
tmc.vactual.VACTUAL = 1000
tmc.write_VACTUAL()

# Read a register value
gstat_value = tmc.read_GSTAT()
print(f"GSTAT Register Value: {gstat_value}")

# Close the UART connection when done
uart.close()
```

**Note:**
The MS1 and MS2 pins in the uart interface determine the **node address** of the TMC2209 driver. 
If your node address is different from `0x00`, ensure that you correctly set the **digital values of MS1 and MS2**.


### Extending the Library
The library is designed to be **hardware-agnostic** so it works on multiple platforms like **Jetson Nano, Raspberry Pi, and other SBCs**.
You can **extend it by subclassing** `TMC2209Configure` to add your own methods for custom behavior.

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.