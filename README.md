# L02: Smart Calculator

A menu-driven command-line calculator written in Python. It bundles three everyday tools into one program: a bill splitter, a unit converter and a BMI calculator.

Part of my **CS Gauntlet**, a 100-level roadmap of personal projects that scale from easy to advanced. This is **Level 2** (Zone 1: Spark).

## Features

| Option | What it does |
|--------|--------------|
| **Split bill** | Takes the bill amount and number of people, adds a 5% tip, and shows each person's share and the tip amount |
| **Convert units** | Kilometres to miles, and Celsius to Fahrenheit |
| **BMI calculator** | Takes height (m) and weight (kg), prints the BMI and its category (underweight, normal, overweight, obese) |
| **Exit** | Quits the program |

## How to run

You need Python 3.6 or newer (f-strings are used).

```bash
git clone https://github.com/sakshamhada-tech/gauntlet-L02-smart-calculator.git
cd gauntlet-L02-smart-calculator
python3 main.py
```

## Example

```
----------------------------------------------
1. Split Bill among your friends
2. Convert units (km to miles, celcius to farenheit)
3. Calculate your BMI
4. Exit
-----------------------------------------------
Please choose what do you want to do: 2

Converting units...

1. Convert km to mi
2. Convert celcius to farenheit
3. Back
Choose what do you want to do: 1

Enter the no. of km: 10

10km is equal to 6.21mi.
```

## What I practised

- Splitting a program into small functions with parameters
- A `while True` menu loop controlled with `break` and `continue`
- A nested sub-menu for the unit converter
- `if / elif / else` and chained comparisons (e.g. `18.5 <= bmi <= 24.9`)
- Formatting output with f-strings (e.g. `{bmi:.2f}`)
