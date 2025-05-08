
def remove_elements(lst):
    # Elimina el primer (índice 0), quinto (índice 4) y sexto (índice 5) elementos, si existen
    indices_to_remove = [0, 4, 5]
    return [el for i, el in enumerate(lst) if i not in indices_to_remove]

def add_elements(lst):
    # Agrega 'Pink' al inicio y 'Yellow' al final
    return ['Pink'] + lst + ['Yellow']

def is_empty(lst):
    # Devuelve True si la lista está vacía
    return len(lst) == 0

def check_lists(lst1, lst2):
    # Verifica si ambas listas tienen el mismo 3er elemento (índice 2)
    if len(lst1) > 2 and len(lst2) > 2:
        return lst1[2] == lst2[2]
    return False

def list_of_lists(lst_of_lsts):
    # Aplica recortes específicos a las 3 listas internas
    modified = []
    if len(lst_of_lsts) >= 1:
        modified.append(lst_of_lsts[0][:2])  # Primeros 2 elementos
    if len(lst_of_lsts) >= 2:
        modified.append(lst_of_lsts[1][1:4])  # Elementos del índice 1 al 3
    if len(lst_of_lsts) >= 3:
        modified.append(lst_of_lsts[2][-2:])  # Últimos 2 elementos
    return modified
