def list2dict(lista: list) -> dict:
    """Devuelve el diccionario equivalente a una lista."""
    return { i:e for i, e in enumerate(lista) }
    
#    res = {}
#    for i, e in enumerate(lista):
#        res[i] = e
#    return res
     
def dict2list(dic: dict) -> list:
    """
    dict2list({0: 'a', 2: 'c', 1: 'b'}) # => ['a', 'b', 'c']
    dict2list({2: 'c', 0: 'a'}) # => ['a', None, 'c']
    """
    res = [None] * (max(dic) + 1)
    for k, v in dic.items():
        res[k] = v
    return res


add_name({}, "Brutus", 300) == {"Brutus": 300}
add_name({"piano": 500}, "Brutus", 400) == {"piano": 500, "Brutus": 400}
add_name({"piano": 500, "stereo": 300}, "Caligula", 440)
== {"piano": 500, "stereo": 300, "Caligula": 440}


def add_name(obj, name, value):
    res = obj.copy()
    res[name] = value
    return res
