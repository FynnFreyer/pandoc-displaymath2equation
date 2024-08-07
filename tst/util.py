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


def find_occurences(elem: Doc | Element, klass: Type) -> list:
    """
    Find all child elements of a certain type in a document.
    Will return a list of those elements afterwards.

    :param klass: A class of which to count occurrences.
    :param elem: An element (or doc) to search for childelements of type ``klass``.
    :return: The list of child elements of type ``klass``.
    """
    occurences = []

    def reporter(elem: Doc | Element, doc: Doc | None = None) -> None:
        """
        Reporter function to walk the document tree and capture elements of type ``klass``.

        :param elem: An element in the document stream.
        :param doc: Possibly the document.
        """

        if isinstance(elem, klass):
            occurences.append(elem)

    elem.walk(reporter)
    return occurences


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
