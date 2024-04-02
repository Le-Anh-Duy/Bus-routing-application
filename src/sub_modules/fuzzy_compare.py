from thefuzz import fuzz
from unidecode import unidecode

def fuzzy_compare(str1, str2):
    return fuzz.ratio(unidecode(str1).lower(), unidecode(str2).lower()) >= 85

def keyword_check(str1, str2):
    return (fuzz.ratio(unidecode(str1).lower(), unidecode(str2).lower()) >= 40 and len(str2) > 20) or (fuzz.ratio(unidecode(str1).lower(), unidecode(str2).lower()) >= 85)