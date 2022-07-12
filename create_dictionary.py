def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    dic = {}
    for i in range(len(key)):
        dic[i] = value[i]


    return dic
key = [1, 2, 3] 
value = ["one", "two", "three"]
print(create_dictionary(key,value))