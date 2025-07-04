## Basic Python Tax Calculator (Old vs New Regime)

A simple command-line Python program to help Indian taxpayers compare their tax deductions under the **Old Tax Regime** and the **New Tax Regime**.

------------------------------------------------------------------------------------------------------

## 📋 Features

- Takes input of **CTC** and **Bonus**.
- Calculates total income.
- Applies deductions under the **Old Regime** (Standard Deduction, HRA, Section 80C).
- Calculates tax under both regimes using applicable **income slabs and cess**.
- Compares both tax amounts and suggests the **more beneficial regime**.

--------------------------------------------------------------------------------------------------------

## How to Run

1. Make sure Python is installed on your system (Python 3.x).
2. Copy the code into a file named `tax_calculator.py`.
3. Open terminal/command prompt and run:
```bash
python tax_calculator.py 
```
4.  Enter your CTC and Bonus when prompted

---------------------------------------------------------------------------------------------------------
## Tax Slabs Used
Old Regime Deductions:
Standard Deduction: ₹50,000
HRA: ₹20,000
Section 80C: ₹1,50,000

Old Regime Tax Slabs:
Income Range  	Tax Rate
₹0 – ₹2.5 Lakhs  	0%
₹2.5L – ₹5L      	5%
₹5L – ₹10L	      20%
Above ₹10L      	30%

New Regime Tax Slabs:
Income Range	Tax Rate
₹0 – ₹3L	      0%
₹3L – ₹6L      	5%
₹6L – ₹9L      	10%
₹9L – ₹12L     	15%
₹12L – ₹15L	    20%
Above ₹15L	    30%

Note: 4% cess is applied in both regimes.
-----------------------------------------------------------------------------------------------------------
## Example Output

==== TAX DEDUCTION CALCULATOR ====
Enter your CTC (₹): 1200000
Enter your Bonus (₹): 100000
Total Income (CTC + Bonus): ₹ 1300000.0
Old Regime Tax Deduction: ₹ 155800
New Regime Tax Deduction: ₹ 120120
You save ₹ 35680 more using the New Regime.

Author
Lasya
