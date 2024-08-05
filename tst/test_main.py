from panflute import RawBlock, RawInline

from util import process_file, report_occurences
from util import report_occurences


def test_doc_contains_raw_block_after_filter(doc_test_md):
    counter = {}
    reporter = report_occurences(klass=RawBlock, counter=counter)
    doc_test_md.walk(reporter, doc=doc_test_md)
    assert len(counter[RawBlock]) == 2


def test_doc_contains_raw_inline_after_filter(doc_test_md):
    counter = {}
    reporter = report_occurences(klass=RawInline, counter=counter)
    doc_test_md.walk(reporter, doc=doc_test_md)
    assert len(counter[RawInline]) == 2
