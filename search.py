def search_record(dataset, search_type,value):
# value - is part or full number (1)
    result={}
    if search_type == 'sp':
        for phone in dataset:
            if value in phone:
                result.update({phone: dataset[phone]})
    elif search_type == 'sf':
        for phone, data in dataset.items():
            if value in data['first_name']:
                result.update({phone: dataset[phone]})
    elif search_type == 'sl':
        for phone, data in dataset.items():
            if value in data['last_name']:
                result.update({phone: dataset[phone]})
    elif search_type == 'sfl':
        value_2=value.split(' ')
        for phone, data in dataset.items():
            if value_2[0] in data['first_name']:
                if value_2[1] in data['last_name']:
                    result.update({phone: dataset[phone]})
    elif search_type == 'sct':
        for phone, data in dataset.items():
            if value in data['city']:
                result.update({phone: dataset[phone]})
    elif search_type == 'sc':
        for phone, data in dataset.items():
            if value in data['country']:
                result.update({phone: dataset[phone]})
    return result


