import sys
import inspect
from pprint import pp


def show(caller_location: str = "", die: bool = False):
    """Show locals at call site, and maybe die."""
    print(f"{caller_location}\n", file=sys.stderr)
    frame = inspect.currentframe()
    try:
        locs = frame.f_back.f_locals
        pp(locs, stream=sys.stderr)
    finally:
        del frame

    if die:
        print("AAAARRRRGGGHHH\n\n\n", file=sys.stderr)
        sys.exit(0)
