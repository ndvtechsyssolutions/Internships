# 🧮 Tax Deduction Calculator (Old vs New Regime) – FY 2024–25

This is a **menu-driven Python console application** that calculates personal income tax in India under both:
- The **Old Regime** (with standard deduction and Section 80C),
- The **New Regime** (as per Section 115BAC, with revised slab structure).

The calculator supports:
- Accurate slab-based tax computation
- Full deduction handling (Standard, 80C where allowed)
- **Section 87A rebate handling**
- **4% Health & Education Cess**
- Clean comparison and regime recommendation
- Custom handling of **assignment test cases and real-world edge cases**

---

## 🎯 Features

- Input: 🧾 `CTC` and `Bonus`
- Output:
  - Total Income
  - Tax under Old Regime ✅
  - Tax under New Regime ✅
  - Regime that saves more money 💸
- Handles real Indian Income Tax rules (FY 2024–25)
- Fully commented and PEP8-compliant
- Menu-driven: can run multiple queries in one session

---

## 🧠 How It Works

### 🔹 1. Income Input

1. User provides:
```bash
Enter your CTC: 600000
Enter your Bonus: 50000
Total Income = CTC + Bonus = ₹6,50,000
```
 2. OLD Regime Calculation
```Allowed Deductions:
₹50,000 (Standard Deduction)

₹1,50,000 (Section 80C)

📉 Taxable Income = ₹6,50,000 − ₹2,00,000 = ₹4,50,000

| Range       | Rate | Tax           |
| ----------- | ---- | ------------- |
| Up to ₹2.5L | 0%   | ₹0            |
| ₹2.5L – ₹5L | 5%   | ₹12,500       |
| ₹5L – ₹10L  | 20%  | as applicable |
| ₹10L+       | 30%  | as applicable |

✅ Section 87A Rebate:
If taxable income ≤ ₹5L, then a rebate up to ₹12,500 applies

This reduces total tax to ₹0 for incomes up to ₹5L

✅ Cess:
After computing tax, 4% Health & Education Cess is added to the final amount
```
3. NEW Regime Calculation
```
✅ Allowed Deductions:
₹75,000 (Standard Deduction only, applicable to salaried/pensioners)

📉 Taxable Income = ₹6,50,000 − ₹75,000 = ₹5,75,000

✅ Slabs (FY 2024–25, post Budget 2023):
Range	Rate
Up to ₹3L	0%
₹3L – ₹7L	5%
₹7L – ₹10L	10%
₹10L – ₹12L	15%
₹12L – ₹15L	20%
₹15L+	30%

✅ Section 87A Rebate:
If taxable income ≤ ₹7L, then a rebate up to ₹25,000 is applied

This makes tax = ₹0 for most middle-income individuals

✅ Cess:
As with the old regime, 4% cess is applied on total tax
```
---

## ⚠️ Edge Case Handling

The code intelligently handles:

- Case Logic Implemented
- Income = ₹6.5L	Rebate triggers in both regimes
- Income > ₹7L in New Regime	Rebate is skipped (as per rules)
- High Income > ₹50L or ₹1Cr	Cess still correctly applied
- Deductions under New Regime	Only allowed standard deduction (₹75k)
- Old Regime Rebate Cutoff ₹5L	Automatically waives tax below that
- Negative or 0 taxable income	No tax charged

✅ Slab-by-slab breakdown with thresholds ensures correct behavior for all income levels.


## 📦 How to Run
- ▶ Step 1: Install Python 3.x
- Make sure Python 3 is installed on your system:

```
python --version
```
- ▶ Step 2: Run the script
From the folder where TaxCalculator.py is located:
```
python TaxCalculator.py
```
- You’ll be prompted to enter your income, and see a full comparison.

## 💻 Sample Output 1

- Enter your CTC: 600000
- Enter your Bonus: 50000

- Total Income: Rs.650000
- Old Regime Tax Deduction: Rs.0
- New Regime Tax Deduction: Rs.0
- Both regimes result in the same tax amount.
---
## 💻 Sample Output 2
- Enter your CTC: 4000000
- Enter your Bonus: 50000

- Total Income: Rs.4050000
- Old Regime Tax Deduction: Rs.1006200
- New Regime Tax Deduction: Rs.928200
- You Save Rs.78000 more using the New Regime.
---
## 🔒 Assumptions & Limitations
- Assumes salary/pension income for standard deduction eligibility

- No HRA, LTA, or other exemptions under new regime (as per law)

- Rebate logic strictly follows FY 2024–25 provisions
---
## 📚 Sources Used
- Official India Income Tax Portal

- Union Budget 2023 & 2024 Announcements

- Finance Act (FY 2024–25)

- Section 87A, Section 115BAC, and 80C interpretation

## 👨‍💻 Author
- Built by **Suryesh Pandey**, an **intern** at **NDVTechsys**
- Prepared for the **"Console-Based Tax Calculator"** assignment
- Submission Date: 22nd May 2025

