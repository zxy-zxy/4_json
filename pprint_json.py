import sys
import json
from json import JSONDecodeError
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-filepath",
        type=str,
        help="Please provide a filepath.",
        required=True
    )
    return parser


def load_data_from_file(filepath):
    with open(filepath) as file:
        return json.load(file)


def pretty_print_json(json_content_loaded):
    json_content_dumped = json.dumps(json_content_loaded, indent=4, ensure_ascii=False)
    print(json_content_dumped)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    try:
        json_content_loaded = load_data_from_file(args.filepath)
    except FileNotFoundError as e:
        sys.exit(e)
    except JSONDecodeError as e:
        sys.exit(e)
    pretty_print_json(json_content_loaded)
