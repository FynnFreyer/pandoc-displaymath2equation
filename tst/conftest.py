from pathlib import Path
from pydoc import Doc

from pytest import fixture

from util import process_file


@fixture(scope="session")
def tst_dir() -> Path:
    return Path(__file__).parent

@fixture(scope="session")
def md_dir(tst_dir) -> Path:
    return tst_dir / "assets/markdown"


@fixture(scope="session")
def labeled_doc(md_dir) -> Doc:
    return process_file(md_dir / "labeled.md")


@fixture(scope="session")
def reflist_doc(md_dir) -> Doc:
    return process_file(md_dir / "refs_in_lists.md")


@fixture(scope="session")
def eqlist_doc(md_dir) -> Doc:
    return process_file(md_dir / "eqs_in_lists.md")
