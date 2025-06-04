local_name_class = {}

def add_id(class_name):
    global  local_name_class
    if class_name not in local_name_class:
        local_name_class[class_name] = 0
    else:
        local_name_class[class_name] += 1
    return local_name_class[class_name]