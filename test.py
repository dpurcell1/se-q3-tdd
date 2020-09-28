import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.'
    )
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    return parser


parser = create_parser()
parser
