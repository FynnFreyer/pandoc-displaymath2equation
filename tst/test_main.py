from panflute import RawBlock, RawInline

from displaymath2equation.config import Config
from util import find_occurences


def test_labeled_doc_contains_eq_blocks_after_filter(labeled_doc):
    """Displaymath is turned into RawBlock elements."""
    eq_blocks = find_occurences(labeled_doc, klass=RawBlock)
    assert len(eq_blocks) == 2


def test_labeled_doc_contains_rendered_eq_refs_after_filter(labeled_doc):
    """Eq-refs get rendered as RawInline elements."""
    eq_refs = find_occurences(labeled_doc, klass=RawInline)
    assert len(eq_refs) == 2


def test_labeled_doc_yields_config(labeled_doc):
    config = Config.from_doc(labeled_doc)
    assert config.labeled_only


def test_reflist_doc_contains_rendered_eq_refs_after_filter(reflist_doc):
    eq_refs = find_occurences(reflist_doc, klass=RawInline)
    assert len(eq_refs) == 6


def test_eqlist_doc_contains_rendered_eq_blocks_after_filter(eqlist_doc):
    eq_blocks = find_occurences(eqlist_doc, klass=RawBlock)
    assert len(eq_blocks) == 3
