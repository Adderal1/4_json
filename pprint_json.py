import json
import pprint

def load_data(filepath):
    with open(filepath, encoding='Latin-1') as row_data:
        make_json_pretty = row_data.read()
    row_data.close()
    return json.load(make_json_pretty)


def pretty_print_json(data):
    pprint.pprint(data, depth=10, width=10)


if __name__ == '__main__':
    make_json_pretty = load_data(input('Enter the path to the file: '))
    pretty_print_json(make_json_pretty)
