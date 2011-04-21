"""Adjust Python path to include ../"""
import os
import sys

_SCRIPT_DIR = os.path.realpath(os.path.dirname(sys.argv[0]))


def fix():
    # Include ../ on Python path to pick up local phonenumbers/ directory
    sys.path.insert(0, os.path.join(_SCRIPT_DIR, ".."))
