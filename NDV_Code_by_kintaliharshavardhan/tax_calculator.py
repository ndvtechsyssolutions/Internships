while True:
    #taking inputs
    ctc=float(input("enter your cost to company"))
    bonus=float(input("enter your bonus"))
    total_income=ctc+bonus
    deducted_income=total_income-50000-150000
    #old regime
    old_regime=0
    if total_income<=250000:
        old_regime=deducted_income*0
    elif total_income<=500000:
        old_regime=(deducted_income-250000)*0.05
    elif total_income<=1000000:
        old_regime=250000*0.05+(deducted_income-500000)*0.20
    elif total_income>=1000000:
        old_regime=(deducted_income-100000)*0.30+(500000*0.20)+(250000*0.05)
        #new regime
    new_regime=0
    total_income1=total_income
    if  total_income1<=300000:
        new_regime=total_income1*0
    elif total_income1<=600000:
        new_regime=(total_income1-300000)*0.05
    elif total_income1<=900000:
        new_regime=(total_income1-600000)*0.10+(300000*0.05)
    elif total_income1<=1200000:
        new_regime=(total_income1-900000)*0.15+(300000*0.05)+(600000*0.10)
    elif total_income1<=1500000:
        new_regime=(total_income1-1200000)*0.20+(300000*0.05)+(600000*0.10)+(900000*0.15)
    elif total_income1>=1500000:
        new_regime=(total_income1-1500000)*0.30+(300000*0.05)+(600000*0.10)+(900000*0.15)+(1200000*0.20)
    print("old regime tax deduction: Rs.",old_regime) 
    print("new regime tax deduction: Rs.",new_regime)
    save=new_regime-old_regime
    if save==0:
        print("both old and new regime ares same",save)
    elif save<=0:
        print("You use up Rs.",save,"using the new regime")
    elif save>=0:
        print("You save Rs.",save,"using the new regime")
    comparision=save
    if comparision==0:
        print("both regime are best")
    elif save<=0:
        print("new regime is best")
    elif save>=0:
        print("old regime is best")
    #to repeat
    option=input("do you want to calculate again{yes,no}")
    if option=="no":
        print("tax calculation ended")
        break
