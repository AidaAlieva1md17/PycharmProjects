countries_dict = {"Австрия":"Вена","Азербайджан":"Баку","Армения":"Ереван","Бельгия":"Брюссель","Великобритания":"Лондон","Франция":"Париж","Белоруссия":"Минск",
             "Болгария":"София","Сербия":"Белград","Польша":"Варшава","Ирландия":"Дублин","Чехия":"Прага","США":"Вашингтон",}
print(countries_dict)
for key in sorted (countries_dict):
    print (key,"-", countries_dict[key])