def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, 
    return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    older = []
    for i in people:
        older.append(people[i])
    x = max(older)
    for j in people:
        if people[j]==x:
            return x
people = {"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}
print(oldest(people))

