ingridient ="Pasta"
ingridient2 = "Sausage"

if ingridient == "Pasta":
    if ingridient2 == "Meatballs":
        print("I reccomend making pasta and meatballs")
    else:
        print("I recommend making plain pasta")
else:
    print("I have no recommedations")

if ingridient == "Pasta" and ingridient2 == "Meatballs":
    print("I reccomend making pasta and meatballs")
elif ingridient == "Pasta":
    print("I recommed making plain pasta!")