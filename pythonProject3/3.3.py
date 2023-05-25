while (word:= str(input())) != "stop":
    if "ф" in word or "Ф" in word:
        print ("Ого! Это редкое слово")
    else:
        print ("Эх, это  не очень редкое слово")