from io import StringIO
from pathlib import Path

from displaymath2equation.main import main

from panflute import Doc, Element, RawBlock
from panflute.io import load

_THIS_DIR = Path(__file__).parent

_result_contains_raw_block = False


def mark_raw_blocks(elem: Element, doc: Doc | None = None) -> None:
    if isinstance(elem, RawBlock):
        global _result_contains_raw_block
        _result_contains_raw_block = True


def test_doc_contains_raw_block_after_filter():
    with open(_THIS_DIR / "assets/test.json") as file, StringIO() as out:
        main(input_stream=file, output_stream=out)
        json_result = out.getvalue()
    with StringIO(json_result) as result:
        doc = load(result)
    doc.walk(mark_raw_blocks, doc=doc)
    assert _result_contains_raw_block
