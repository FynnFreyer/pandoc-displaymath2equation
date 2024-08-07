from pathlib import Path
from pydoc import Doc

from pytest import fixture

from util import process_file


@fixture(scope="session")
def tst_dir() -> Path:
    return Path(__file__).parent


@fixture(scope="session")
def labeled_doc(tst_dir) -> Doc:
    return process_file(tst_dir / "assets/labeled.md")


@fixture(scope="session")
def reflist_doc(tst_dir) -> Doc:
    return process_file(tst_dir / "assets/refs_in_lists.md")


@fixture(scope="session")
def eqlist_doc(tst_dir) -> Doc:
    return process_file(tst_dir / "assets/eqs_in_lists.md")
