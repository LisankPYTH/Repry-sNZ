calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    strochka = (str(string))
    itog = (len(strochka), strochka.upper(), strochka.lower())
    count_calls()
    return itog


def it_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result


print(string_info("Resultat"))
print(string_info("Avitomoika"))
print(it_contains("Ichi", ["iskAt", "iCHI", "ichuschii"]))
print(it_contains("Ne_ichi", ["Ne_ichitca", "Ne_naiti", "Ne_poimat"]))
print(calls)
