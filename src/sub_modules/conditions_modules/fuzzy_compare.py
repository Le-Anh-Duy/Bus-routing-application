from thefuzz import fuzz
from unidecode import unidecode

def fuzzy_compare(a, b):
    a = unidecode(a)
    a = a.lower()
    b = unidecode(b)
    b = b.lower()
    # if fuzz.ratio(a, b) >= 50:
    #     print(a, '----------', b)
    return fuzz.ratio(a, b) >= 90