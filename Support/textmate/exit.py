from __future__ import print_function

from sys import exit, stderr


def discard():
    exit(200)


def replace_text(out=None):
    if out:
        print(out)
    exit(201)


def replace_document(out=None):
    if out:
        print(out)
    exit(202)


def insert_text(out=None):
    if out:
        print(out)
    exit(203)


def insert_snippet(out=None):
    if out:
        print(out)
    exit(204)


def show_html(out=None):
    if out:
        print(out)
    exit(205)


def show_tool_tip(out=None):
    if out:
        print(out, file=stderr)
    exit(206)


def create_new_document(out=None):
    if out:
        print(out)
    exit(207)


def insert_snippet_no_indent(out=None):
    if out:
        print(out)
    exit(208)
