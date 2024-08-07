from panflute import RawBlock, RawInline

from displaymath2equation.config import Config
from util import report_occurences


def test_labeled_doc_contains_eq_blocks_after_filter(labeled_doc):
    """Displaymath is turned into RawBlock elements."""
    counter = {}
    reporter = report_occurences(klass=RawBlock, counter=counter)
    labeled_doc.walk(reporter, doc=labeled_doc)
    assert len(counter[RawBlock]) == 2


def test_labeled_doc_contains_rendered_eq_refs_after_filter(labeled_doc):
    """Eq-refs get rendered as RawInline elements."""
    counter = {}
    reporter = report_occurences(klass=RawInline, counter=counter)
    labeled_doc.walk(reporter, doc=labeled_doc)
    assert len(counter[RawInline]) == 2


def test_labeled_doc_yields_config(labeled_doc):
    config = Config.from_doc(labeled_doc)
    assert config.labeled_only


def test_reflist_doc_contains_rendered_eq_refs_after_filter(reflist_doc):
    counter = {}
    reporter = report_occurences(klass=RawInline, counter=counter)
    reflist_doc.walk(reporter, doc=reflist_doc)
    assert len(counter[RawInline]) == 6

def test_eqlist_doc_contains_rendered_eq_blocks_after_filter(eqlist_doc):
    counter = {}
    reporter = report_occurences(klass=RawBlock, counter=counter)
    eqlist_doc.walk(reporter, doc=eqlist_doc)
    assert len(counter[RawBlock]) == 3
