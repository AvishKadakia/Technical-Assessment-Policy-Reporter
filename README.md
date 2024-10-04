
# Technical Assessment Project

This repo contains solutions for two assignments
- **Assignment 1**: Find the best threshold for a binary classification model where recall >= 0.9.
- **Assignment 2**: Implement a generic Finite State Machine (FSM) using Object-Oriented Design principles and use it to compute the remainder when an unsigned binary number is divided by three. 

---

## Table of Contents

- [Technical Assessment Project](#technical-assessment-project)
  - [Table of Contents](#table-of-contents)
  - [General Requirements](#general-requirements)
  - [Project Structure](#project-structure)
  - [Assignment 1](#assignment-1)
    - [Problem Description](#problem-description)
    - [Solution Overview](#solution-overview)
    - [Files](#files)
    - [How to Run](#how-to-run)
    - [Running Tests](#running-tests)
  - [Assignment 2](#assignment-2)
    - [Problem Description](#problem-description-1)
    - [Solution Overview](#solution-overview-1)
    - [Files](#files-1)
    - [How to Run](#how-to-run-1)
    - [Running Tests](#running-tests-1)
  - [Dependencies](#dependencies)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

---

## General Requirements

- **Python Version**: The project requires **Python 3.6** or higher.
- **No External Libraries Required**: The solutions use only standard Python libraries.

---

## Project Structure

```
. 
├── assignment_1.py 
├── assignment_2.py 
├── test_assignment_1.py 
├── test_assignment_2.py 
└── README.md
```

---

## Assignment 1

### Problem Description


**Objective**: Gievn counts of true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN) at different confidence score thresholds (0.1, 0.2, ..., 0.9). Write a function to return the **best threshold** that yields a recall of at least **0.9**. The "best" threshold is then defined as the one with the highest precision. If multiple thresholds have the same precision, then the one with the highest threshold value is selected.

### Solution Overview

The `find_best_threshold` function processes a list of performance metrics at different thresholds and:

1. Calculates precision and recall for each threshold.
2. Filters thresholds where recall is at least 0.9.
3. Selects the threshold with the highest precision.
   - In case of ties, selects the highest threshold value.

### Files

- `assignment_1.py`: Contains the `find_best_threshold` function and example usage.
- `test_assignment_1.py`: Contains unit tests for the function.

### How to Run

1. **Clone the Repository** (if not already done):

   ```bash
   git clone https://github.com/AvishKadakia/Technical-Assessment-Policy-Reporter.git
   cd technical-assessment
   ```

2. **Run the Script**:

   ```bash
   python assignment_1.py
   ```

   **Expected Output**:

   ```
   Best Threshold: 0.2
   ```

### Running Tests

Run the Unit Tests:

```bash
python -m unittest test_assignment_1.py
```

**Expected Test Output**:

```
Best Threshold: 0.2
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s
```

## Assignment 2

### Problem Description

Design and implement a generic class for a Finite State Machine (FSM). Then use it to compute the remainder when an unsigned binary integer (represented as a string of ones and zeros) is divided by three.


### Solution Overview

**Finite Automaton Definition**:

- **States**: S0, S1, S2 (representing remainders 0, 1, 2).
- **Input Alphabet**: '0', '1'.
- **Initial State**: S0.
- **Transition Function**: Defined based on the current state and input symbol.
- **Final States**: A set of accepting/final states (F).
  
**Implementation**:

- A generic `FiniteAutomaton` class is implemented for any FSM.
- A subclass `ModThreeAutomaton` implements the specific FSM for modulo three calculations.
- The FSM processes the binary string and determines the final state, which corresponds to the remainder.

### Files

- `assignment_2.py`: Contains the `FiniteAutomaton` base class, the `ModThreeAutomaton` subclass, and example usage.
- `test_assignment_2.py`: Contains unit tests for both classes.

### How to Run

**Run the Script**:

```bash
python assignment_2.py
```

**Expected Output**:

```
Input: '1101' => Remainder: 1
Input: '1110' => Remainder: 2
Input: '1111' => Remainder: 0
Input: '110' => Remainder: 0
Input: '1010' => Remainder: 1
```

### Running Tests

Run the Unit Tests:

```bash
python -m unittest test_assignment_2.py
```

**Expected Test Output**:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

## Dependencies

- Python 3.6+

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
