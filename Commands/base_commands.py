import json

def download_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        out_list = json.load(f)
        return out_list

def save_data(path, input_array):
    with open(path, 'w', encoding='utf-8') as outfile:
        json.dump(input_array, outfile, ensure_ascii=False)

def save_dict_data(name, id, data_array):
    data = {
        'id': id,
        'name': name,
        'number': None
    }
    data_array.append(data)
    save_data('phone_book.json', data_array)