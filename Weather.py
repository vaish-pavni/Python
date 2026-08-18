def temp(temprature):
    temperature=20
    if temperature >20 :
        print("The weather is not good , it is hot outside.")
    else:
        print("The weather is good outside.")

    #USING BOOLEAN.
    #AND , OR , NOT OPERATION WITH IF-ELSE STATEMENTS.
    temperature=24
    is_sunny=True
    if temperature >20 and is_sunny :
        print("The weather is not good , it is hot outside.")
    elif temperature <=20 and is_sunny:
        print("The weather is cold outside.")
    else:
        print("The weather is good outside.")


    temperature=-4
    is_raining=True
    if temperature >20 or is_raining:
        print("The weather is hot outside.")
    elif temperature <=20 or is_raining:
        print("The weather is cold outside.")
    else:
        print("The event is still running.")

    temperature=24
    is_sunny=False
    if temperature >20 and not is_sunny :
        print("The weather is not good , it is hot outside.")
    elif temperature <=20 and not is_sunny:
        print("The weather is cold outside.")
    else:
        print("The weather is good outside.")

temp(10)