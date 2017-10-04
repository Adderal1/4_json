import json
import pprint

def load_data(filepath):
    with open(filepath, encoding='Latin-1') as row_data:
        unreadable_json = row_data.read()
    row_data.close()
    return json.load(unreadable_json)


def pretty_print_json(data):
    pprint.pprint(data, depth=10, width=10)


if __name__ == '__main__':
    unreadable_json = load_data(input('Enter the path to the file: '))
    pretty_print_json(unreadable_json)
