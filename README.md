# -General-IoT
Task for Oralens

IoT Device Control System

This repository contains the code for an IoT device control system designed to collect environmental and positional data. The system utilizes a Raspberry Pi platform along with various sensors and actuators for data collection and user interaction.

Overview
The IoT device control system consists of the following components:

Raspberry Pi 3 Model B: Acts as the central processing unit for data processing and control.

Stepper Motor: Used for height adjustment functionality.

Continuous Rotation Micro Servo (FS90R): Enables pan and tilt adjustments.
Sensors:

Methane, Butane, LPG, and Smoke Gas Sensor (MQ-2)

DHT22/11 Humidity and Temperature Sensor

Electret Microphone Breakout

Other Components:

EasyDriver - Stepper Motor Driver

MCP3008 - 8-Channel 10-Bit ADC With SPI Interface

Breadboard, resistors, jumper wires, power supply, etc.

Features

Control GUI: Provides a tkinter-based GUI for controlling the stepper motor.

Movement Control: Allows users to move the stepper motor forward, backward, and stop its movement.

User Interaction: Intuitive interface with buttons for easy control.

Getting Started

To get started with the IoT device control system, follow these steps:

Hardware Setup:

Connect the Raspberry Pi and other components as per the hardware schematic provided.

Ensure all connections are secure and components are powered appropriately.

Software Installation:

Clone this repository to your Raspberry Pi or development environment.

Install the necessary dependencies, including tkinter if not already installed (sudo apt-get install python3-tk).

Run the Application:

Navigate to the directory containing the code.

Execute the Python script.

