# Financial Calculator CLI

A simple command-line program to apply key financial mathematical concepts from COMM1180 Week 5, including Time Value of Money, Annuities, Perpetuities, and APR⇄EAR conversions. Designed for Python 3.10+ with an optional learning mode for concept reinforcement.

This mini-project is exclusively serving UNSW undergraduates who take COMM1180 in Term 2, 2025, by students, for students.

---

## Table of Contents

* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Running the Program](#running-the-program)
* [Using the Calculator](#using-the-calculator)

  * [Time Value of Money](#time-value-of-money)
  * [Annuity Calculations](#annuity-calculations)
  * [Perpetuity Calculations](#perpetuity-calculations)
  * [APR⇄EAR Conversions](#aprear-conversions)
* [Troubleshooting](#troubleshooting)
* [License](#license)

---

## Features

* **Future Value & Present Value** for single lump-sum cash flows.
* **Required Rate & Required Time** calculations.
* **Ordinary & Due Annuity** present and future value.
* **Advance & Arrears Perpetuity** present value.
* **APR to EAR** and **EAR to APR** conversions with real-world examples.
* **Learning Mode** toggles on-screen concept reminders and formulas.

---

## Prerequisites

* **Python 3.10 or higher**
* **pip** (the Python package installer)
* **Git** (optional, for cloning the repository)

### Installing Python

* **Windows/macOS:** Download and install from [python.org](https://www.python.org/downloads/).
* **Linux (Debian/Ubuntu):**

  ```bash
  sudo apt update && sudo apt install python3 python3-pip
  ```

Verify installation:

```bash
python3 --version
pip3 --version
```

---

## Installation

1. **Clone or download the code**

   ```bash
   git clone https://github.com/jinhaoli-alex/unsw-comm1180-w5-financial-calculator.git
   cd financial-calculator
   ```

   *Or* download the `financial_calculator.py` file directly.

2. **Install dependencies**

   The only external library is `rich` for styled console output.

   ```bash
   pip3 install rich
   ```

---

## Running the Program

From the project directory, run:

```bash
python3 w5_financial_calculator.py
```

> On Windows, you may need to use `python` instead of `python3`.

---

## Using the Calculator

1. **Enable Learning Mode**

   * When prompted, type `y` to see concept explanations alongside calculations.

2. **Main Menu Options**

   * **1**: Time Value of Money (single cash flows)
   * **2**: Annuity calculations
   * **3**: Perpetuity calculations
   * **4**: APR⇄EAR conversions
   * **5**: Exit the program

3. **Enter Inputs**

   * Follow on-screen prompts. Enter numbers when requested.
   * **Rates:** enter as percentages (e.g., `3.24%`) when prompted, or as decimals (e.g., `0.0324`) if specified.

### Time Value of Money

* **Future Value:** calculate how much a lump sum grows.
* **Present Value:** discount a future lump sum back to today.
* **Required Rate:** find interest rate needed.
* **Required Time:** find number of periods needed.

### Annuity Calculations

* **Ordinary Annuity:** payments at period end.
* **Annuity-Due:** payments at period beginning.
* Compute either present value or future value of series of payments.

### Perpetuity Calculations

* **Arrears (end-of-period)** or **Advance (beginning)** payments.
* Compute present value of infinite payment series.

### APR⇄EAR Conversions

* **APR → EAR:** enter nominal APR and compounding frequency.
* **EAR → APR:** enter effective annual rate and periods per year.

---

## Troubleshooting

* **ImportError (rich):** run `pip3 install rich` and restart.
* **SyntaxError:** ensure you are using Python 3.10+.
* **Permission Errors:** you may need to run commands with `sudo` on Unix systems.

---

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
