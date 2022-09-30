def choices_to_json(choices):
    data = []
    for item in choices:
        data.append({"text": item[1], "value": item[0]})

    return data

def data_to_json(choices):
    data = []
    for item in choices:
        data.append({"text": item[1], "value": item[0]})

    return data