from projectlens.core import summarize

def test_summarize():
    assert summarize(["src/a.py", "tests/test_a.py", "README.md"]) == {"files": 3, "tests": 1, "docs": 1}
