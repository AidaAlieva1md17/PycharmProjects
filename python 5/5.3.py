nedelia = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
vopros = int(input("Сколько выходных на неделе Вы хотите иметь? "))
print("Ваши рабочие дни: ", nedelia[:-vopros])
print("Ваши выходные дни: ", nedelia[-vopros:])