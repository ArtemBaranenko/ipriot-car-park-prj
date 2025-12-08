# Car Park System – Python Project

A simple Python program that simulates a car park with sensors, displays, logging, and configuration files. This project follows the North Metro Software guidelines and uses classes, docstrings, comments, and JSON configuration.

You may use the guidelines under org/ for assessments and projects in the IP4RIoT cluster.

Project Overview

This project models how a real car park works. It includes:
Entry and Exit Sensors that detect vehicles

- Display screens that show available parking bays
- A CarPark class that stores plates, updates displays, and logs activity
- Logging to a .txt file whenever a car enters or exits
- A JSON config file that saves and loads car park settings

The main goal of the program is to demonstrate object-oriented programming, documentation, and basic file handling in Python.

## Features

- Add and remove cars automatically using sensors
- Generate fake licence plates for testing
- Show available parking bays through connected displays
- Save and load car park settings using config.json
- Write entry/exit logs with timestamps
- Simple, clear structure across multiple Python files

car_park.py - Main CarPark class\
sensor.py - EntrySensor and ExitSensor classes\
display.py - Display class\
main.py - Runs the simulation\
config.json - Stores car park settings\
log.txt - Activity log (auto-generated)

## How to Run

    1.	Make sure all project files are in the same folder.
    2.	Run the main script: python main.py

    This will:
    •	Load the configuration
    •	Create sensors and a display
    •	Simulate cars entering and leaving
    •	Print updates to the terminal
    •	Write logs to a file

## Requirements

This project uses only standard Python libraries:

- json
- pathlib
- datetime
- abc
- random

No external installation is needed.
