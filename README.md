
# **TMC2209 Python Library**
A Python library to configure and communicate with the TMC2209 stepper motor driver via UART. This library enables reading and writing to the TMC2209 registers, configuring microstepping, and setting driver parameters.

## __Features__
- **Read and write registers** of TMC2209
- **Configure driver settings** (e.g., current, voltage, microsteps)
- **UART communication** with TMC2209
- **Register-level access and control**
## 📥 **Installation**
This library depends on **pyserial** for UART communication. Install the required dependencies using:
```bash
pip install pyserial
```

## __Before usage__
Please read the datasheet of TMC2209 to understand the registers and their bits
## 🔧 __Usage__
### 1️⃣ Initialize UART Communication
First, create a **UART** instance to establish serial communication.
```python
from uart import UART

uart = UART(port="/dev/ttyS0")  # Use appropriate port
```
### 2️⃣ Configure the TMC2209 Driver
Create an instance of **TMC2209Configure** to control the stepper motor.

```python
from TMC2209 import TMC2209Configure

tmc = TMC2209Configure(uart=uart, MS1=17, MS2=27, EN=22, node_address=0x00)
```
### 3️⃣ Initialize and Configure the Driver
To set up the motor driver:

```python
tmc.initialize()
```
You can use this function to make sure that the connections are correct
### 4️⃣ Reading and Writing Registers
✅ Writing to a Register
```python
tmc.gcong.shaft = 1 # Setting the shaft bit in GCONF register to reverse the direction
tmc.write_GCONF()  # Writes GCONF register settings
```
✅ Reading a Register
```python
gstat_value = tmc.read_GSTAT()
print(f"GSTAT Register Value: {gstat_value}")
```
### 5️⃣ Closing the UART Connection
```python
uart.close()
```


## 📝 __Full Example Code__

```python
from uart import UART
from TMC2209 import TMC2209Configure

# Initialize UART communication
uart = UART(port="/dev/ttyS0", baudrate=115200)

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