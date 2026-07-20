# Project-Aircraft-Monitoring-System
# ✈️ Aircraft Monitoring System

## Overview

The **Aircraft Monitoring System** is a Python learning project focused on simulating a simple aircraft monitoring application.

The project reads aircraft data, evaluates important flight parameters, and generates status reports based on predefined safety rules. It was created to practice Python programming, software testing, and clean code principles commonly used in software engineering.

---

## Features

* Read aircraft information from a CSV file
* Store aircraft data in Python dictionaries and lists
* Generate aircraft status reports
* Check fuel level
* Detect engine overheating
* Process multiple aircraft using loops
* Validate program behavior with automated unit tests

---

## Technologies

* Python 3
* CSV file handling
* Functions
* Lists and dictionaries
* For loops
* Conditional statements (`if / else`)
* Assertions (`assert`)
* Unit testing concepts

---

## Project Structure

```text
Aircraft_Monitoring_System/
│
├── main.py               # Main application
├── aircraft.csv          # Aircraft data
├── test_aircraft.py      # Unit tests
└── README.md
```

---

## Example Output

```text
LH123 ('LOW FUEL', 'ENGINE OK')
BA456 ('FUEL OK', 'ENGINE OVERHEAT')
LH7811 ('FUEL OK', 'ENGINE OK')
```

---

## Example Safety Rules

### Fuel Monitoring

* Fuel ≥ 50 → `FUEL OK`
* Fuel < 50 → `LOW FUEL`

### Critical Fuel Warning

* Fuel < 20 → `CRITICALLY LOW FUEL, LAND IMMEDIATELY`

### Engine Monitoring

* Engine temperature ≥ 100°C → `ENGINE OVERHEAT`
* Engine temperature < 100°C → `ENGINE OK`

---

## Testing

The project includes automated unit tests covering:

* Normal fuel level
* Low fuel condition
* Engine overheating
* Critical fuel warning

The tests verify that the monitoring logic produces the expected output for different scenarios.

---

## Learning Goals

This project was built to practice:

* Python fundamentals
* Writing reusable functions
* Processing structured data
* Reading external files
* Software testing
* Test-driven thinking
* Clean and readable code
* Git and GitHub workflow

---

## Future Improvements

Planned enhancements include:

* Object-Oriented Programming (classes)
* Reading CSV using Python's `csv` module
* Pytest framework
* Logging
* Exception handling
* Data validation
* Configuration files
* CI/CD with GitHub Actions

---

## Author

This project is part of my software engineering and cybersecurity learning journey, with a focus on Python development, software testing, and building practical programming skills.
