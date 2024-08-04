from functools import partial
from pathlib import Path

from panflute import RawBlock, RawInline

from util import process_file, report_occurences

_THIS_DIR = Path(__file__).parent


def test_doc_contains_raw_block_after_filter():
    # TODO create doc fixture
    doc = process_file(_THIS_DIR / "assets/test.md")
    counter = {}
    reporter = partial(report_occurences, klass=RawBlock, counter=counter)
    doc.walk(reporter, doc=doc)
    assert counter[RawBlock] == 2


def test_doc_contains_raw_inline_after_filter():
    doc = process_file(_THIS_DIR / "assets/test.md")
    counter = {}
    reporter = partial(report_occurences, klass=RawInline, counter=counter)
    doc.walk(reporter, doc=doc)
    assert counter[RawInline] == 2
