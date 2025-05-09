def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        del list_to_remove_elements[5]
    if len(list_to_remove_elements) >= 5:
        del list_to_remove_elements[4]
    if len(list_to_remove_elements) >= 1:
        del list_to_remove_elements[0]
    return list_to_remove_elements

    
def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, 'Pink')
    list_to_add_elements.append('Yellow')
    return list_to_add_elements


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
    return False



def list_of_lists(list_of_lists_to_modify):
    nueva = []

    if len(list_of_lists_to_modify) > 0:
        nueva.append(lista[0][:2])
    if len(list_of_lists_to_modify) > 1:
        nueva.append(lista[1][1:4])
    if len(list_of_lists_to_modify) > 2:
        nueva.append(lista[2][-2:])

    return nueva

