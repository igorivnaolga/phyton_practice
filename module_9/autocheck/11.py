class IDException(Exception):
    pass

def add_id(id_list, employee_id):
    if not (isinstance(employee_id, str) and len(employee_id) > 1 and employee_id[0] == "0" and employee_id[1] == "1"):
        raise IDException("Wrong format of ID")
    
    id_list.append(employee_id)
    return id_list