# 📊 Grouped Frequency Distribution Statistical Calculator

A terminal-based Python tool that computes a comprehensive set of descriptive statistics from grouped frequency distribution data — all in one run, with neatly formatted tabular output.

---

## 📄 Description

This project is a command-line statistical calculator designed for students and educators working with **grouped frequency distributions**. Given a set of class intervals and their corresponding frequencies, the program automatically computes and displays a full statistical summary including measures of central tendency, dispersion, and position.

Instead of manually crunching numbers through multiple formulas, users simply enter their class boundaries and frequency values — and the calculator handles everything else, printing organized tables and results directly in the terminal.

---

## ⚙️ Installation

No external libraries are required. This project runs on **pure Python 3**.

**Steps:**

1. Make sure Python 3 is installed on your system:
   ```bash
   python --version
   ```

2. Clone or download this repository:
   ```bash
   git clone https://github.com/Anup-Koirala-codes/BASIC-STATISTICS-CALCULATOR.git
   cd BASIC-STATISTICS-CALCULATOR
   ```

3. Run the script:
   ```bash
   python calc.py
   ```

---

## 🚀 Usage

When you run the program, it will prompt you to enter:

1. **Lowest value of the first class** (e.g., `10`)
2. **Highest value of the last class** (e.g., `60`)
3. **Class interval width** (e.g., `10`)
4. **Frequency for each class**, entered one by one as the table is printed

**Example session:**

```
Enter a lowest value of first class : 10
Enter a highest value of last class (3 digit number doesnt look nice): 60
Enter a value of class interval : 10

Class (X)    |   frequency (f)   |
10 - 20      |        5
20 - 30      |        12
30 - 40      |        20
40 - 50      |        8
50 - 60      |        5
```

**Example output:**

```
x       | f  | cf | m    | fm    | m²     | fm²      |
___________________________________________________________
10 - 20 |  5 |  5 | 15.0 |  75.0 | 225.0  | 1125.0   |
20 - 30 | 12 | 17 | 25.0 | 300.0 | 625.0  | 7500.0   |
...
___________________________________________________________

Mean = 31.800
Mode = 32.500

Standard Deviation = 9.644
Coefficient of Variation = 30.327%
Variance = 93.010

Median = 31.750
Q1 = 22.917
Q3 = 40.625

Quartile Deviation = 8.854
Coefficient of Quartile Deviation = 0.278

Mean Deviation from Mean = 7.632
Mean Deviation from Median = 7.590
```

---

## ✨ Features

- **Automated class interval table** — builds the frequency distribution table interactively from user input
- **Cumulative frequency (cf)** — calculated and displayed for each class
- **Midpoint calculations (m, fm, m², fm²)** — full working shown in tabular form
- **Measures of Central Tendency**
  - Mean
  - Median (using interpolation formula)
  - Mode (using grouping formula)
- **Measures of Dispersion**
  - Variance
  - Standard Deviation
  - Coefficient of Variation
  - Coefficient of Standard Deviation
- **Quartile Analysis**
  - Q1, Q3 positions and values
  - Quartile Deviation (QD)
  - Coefficient of Quartile Deviation
- **Mean Deviation**
  - MD from Mean and MD from Median
  - Coefficients of both
- **Formatted terminal output** — all results printed in clean, aligned tables

---

## 📋 Requirements

| Requirement | Version  |
|-------------|----------|
| Python      | 3.x      |
| Libraries   | None     |

---

## 📁 Project Structure

```
BASIC-STATISTICS-CALCULATOR/
│
└── calc.py       # Main script containing the calc() function
```

---

## 📝 Notes

- The highest class value should form a clean boundary with the interval (e.g., if start is `10` and interval is `10`, use `60` not `61`).
- 3-digit class boundaries may affect terminal alignment slightly (as noted in the prompt).
- All results are rounded to **3 decimal places** for readability.

---

## 🪪 License

This project is open-source and free to use for academic and educational purposes.