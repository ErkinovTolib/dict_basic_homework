def count_all(txt):
    """
    Given a function that takes a string and calculates the number of 
    letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    text = {}
    num = 0
    lat = 0
    for i in txt:
        if txt.isdigit():
            num += 1
        if not(txt.isdigit()):
            lat += 1
    text["LATTERS"]= lat
    text["DIGITS"] = num

    return text
print(count_all("Hello_World"))