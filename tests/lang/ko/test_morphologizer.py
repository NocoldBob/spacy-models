import pytest
from spacy.tokens import Doc
from spacy.symbols import SPACE
from pathlib import Path
from ...util import evaluate_corpus


TEST_FILES_DIR = Path(__file__).parent / "test_files"


@pytest.mark.parametrize(
    "test_file,pos_threshold",
    [("ko_kaist-ud-dev001_1.json", 0.86)],
)
def test_ko_tagger_corpus(NLP, test_file, pos_threshold):
    data_path = TEST_FILES_DIR / test_file
    evaluate_corpus(
        NLP, data_path, {"pos_acc": pos_threshold}
    )
