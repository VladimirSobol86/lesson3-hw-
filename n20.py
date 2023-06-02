let_rus = {1:'авеинорстАВЕИНОРСТ', 2: 'дклмпуДКЛМПУ', 3: 'бгёьяБГЁЬЯ', 4: 'йыЙЫ', 5: 'жзхцчЖЗХЦЧ', 8: 'шэюШЭЮ', 10: 'фщъФЩЪ'}
let_eng = {1:'aeioulnstrAEIOULNSTR', 2: 'dgDG', 3: 'bcmpBCMP', 4: 'fhvwyFHVWY', 5: 'kK', 8: 'jzJZ', 10: 'qzQZ'}
price = 0
lang = input("Введите язык e = eng или r = rus: ")
if lang == "r":
    word = input("Введите ваше слово: ")
    for i in word:
        for let in let_rus:
            if i in let_rus[let]:
                price = price + let
    print(price)
elif lang == "e":
    word = input("Enter your word: ")
    for i in word:
        for let in let_eng:
            if i in let_eng[let]:
                price = price + let
    print(price)
else:
    print("Неправильный индефикатор языка")