#!/usr/bin/python3
def safe_print_integer_err(value):
    """Print an integer."""
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        import sys
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
