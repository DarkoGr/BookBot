

def words_count(tekst):
    lista = tekst.split()
    return len(lista)

def char_count(tekst):
    dict_count = {}
    
    for ch in tekst:
        ch = ch.lower()
        if ch.isalpha() and ch not in dict_count:
            dict_count[ch] = 1
        elif ch.isalpha() and ch in dict_count:
            dict_count[ch] += 1
        
    return dict_count

def report(char_count_dict):
    dict_list = []
    for char, num in char_count_dict.items():
        dict_list.append({"char":char, "num":num})
    dict_list.sort(key=lambda item: item["num"], reverse=True)
    return dict_list
    








    