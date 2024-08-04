import sys
import inspect
from io import StringIO
from pathlib import Path

from pprint import pp
from typing import Type

from panflute import convert_text, Doc, Element, load

from displaymath2equation.main import main


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


def report_occurences(elem: Element, doc: Doc | None = None, *, klass: Type, counter: dict[Type, int]) -> None:
    """
    Partial apply klass and counter. Then walk the document with the resulting reporter.
    The passed counter will hold number of occurrences afterwards.

    :param elem: An element in the document stream.
    :param doc: Possibly the document.
    :param klass: A klass of which to count occurrences.
    :param counter: A dict that acts as a counter/memory.
    """
    if isinstance(elem, klass):
        if klass not in counter:
            counter[klass] = 0
        counter[klass] += 1


def process_file(path: Path) -> Doc:
    """
    Filter a file with the main method.

    :param path: The file to filter.
    :return: The resulting document.
    """
    with path.open() as file:
        dump = convert_text(file.read(), output_format="json")

    with StringIO(dump) as input, StringIO() as output:
        main(input_stream=input, output_stream=output)
        json_result = output.getvalue()

    with StringIO(json_result) as result:
        return load(result)
