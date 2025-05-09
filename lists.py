
def remove_elements(lst):
    # Elimina el primer (índice 0), quinto (índice 4) y sexto (índice 5) elementos, si existen
    def remove_elements(lst):
    lst = lst[:]  # Make a copy so the original list is not modified
    # remove  6th element (index 5)
    if len(lst) > 5:
        del lst[5]
    # remove  5th element (index 4)
    if len(lst) > 4:
        del lst[4]
    # remove  1st element (index 0)
    if len(lst) > 0:
        del lst[0]
    return lst

def add_elements(lst):
    # add pink and yellow to the start and end of list
    return ['Pink'] + lst + ['Yellow']

def is_empty(lst):
    # return true if the list is empty
    return len(lst) == 0

def check_lists(lst1, lst2):
    # Verifica si ambas listas tienen el mismo 3er elemento (índice 2)
    if len(lst1) > 2 and len(lst2) > 2:
        return lst1[2] == lst2[2]
    return False


def list_of_lists(lst_of_lsts):
    return [
        lst_of_lsts[0][:2],     # first 2 elements of the first list
        lst_of_lsts[1][1:4],    # Elements from index 1 to 3 (4 is not included)
        lst_of_lsts[2][-2:]     # Last 2 elements of the third list
    ]


