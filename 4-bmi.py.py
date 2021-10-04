
    
        weight=float(input("enter Kilogram : "))
        height=float(input("enter Meter : "))

        bmi=float((weight)/(height**2))

        if bmi<18.5:
            print("Underweight")

        elif bmi>=18.5 and bmi<=24.9:
            print("Normal")

        elif bmi>=25 and bmi<=29.9:
            print("Overweight")
        
        elif bmi>=30 and bmi<=34.9 :
            print("Obese")

        else bmi>=35:
            print("Extremely obese")

        
   