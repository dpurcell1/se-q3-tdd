#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = """Darrell Purcell"""


import sys
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


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    if ns.upper and ns.lower and ns.title:
        text = ns.text.title()
        print(text)
    elif ns.title:
        text = ns.text.title()
        print(text)
    elif ns.lower:
        text = ns.text.lower()
        print(text)
    elif ns.upper:
        text = ns.text.upper()
        print(text)
    elif ns.text:
        print(ns.text)


if __name__ == '__main__':
    main(sys.argv[1:])
