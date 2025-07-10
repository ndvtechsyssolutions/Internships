Tax Calculator 💰🧾

📂 Project Overview

    This Python script calculates income tax under Old Regime and New Regime based on your total income (CTC + Bonus). It compares both and tells you which saves more tax.

Files in This Folder

    -tax_calculator.py 🐍
     Contains the full tax calculation and comparison logic.

Key Components
    1. Old Regime Tax Calculation

        Applies standard deductions:
            ₹50,000 (Standard Deduction)
            ₹50,000 (HRA)
            ₹1,50,000 (Section 80C)
            
            Calculates tax based on slabs: 0%, 5%, 20%, 30%.

    2. New Regime Tax Calculation

        No standard deductions.

        Uses slabs with progressive rates from 0% to 30% starting at ₹3,00,000 income.

    3. Main Program Flow
    
        Takes user input for CTC and Bonus.

        Calculates total income.

        Computes tax for both regimes.

        Prints the tax amounts and the better saving option.

How to Run ▶️
Ensure Python is installed.

Run the script:
    python tax_calculator.py  

Input Total CTC and Bonus when prompted.

See your tax comparison results.

Example Usage 📝

    Enter your Total CTC: ₹1200000  
    Enter your Bonus Amount: ₹100000  

    --- Income Details ---  
    Total Income (CTC + Bonus): ₹1300000  

    --- Tax Comparison ---  
    Old Regime Tax: ₹135000.0  
    New Regime Tax: ₹95000.0  
    You save ₹40000.00 more using the New Regime 💸  

Author ✍️
    Simple Python script by you, built for quick and clear tax comparisons.

