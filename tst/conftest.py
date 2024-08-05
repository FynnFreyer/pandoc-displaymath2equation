from pathlib import Path
from pydoc import Doc

from pytest import fixture

from util import process_file


@fixture(scope="session")
def tst_dir() -> Path:
    return Path(__file__).parent

@fixture(scope="session")
def doc_test_md(tst_dir) -> Doc:
    return process_file(tst_dir / "assets/test.md")