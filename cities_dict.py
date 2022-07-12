def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    list1 = {}
    for i in range(len(cities)):
        list1[i] = cities[i]

    return list1
cities = ["Bukhara", "Khiva", "Namangan", "Samarkand", "Tashkent"]
print(cities_dict(cities))