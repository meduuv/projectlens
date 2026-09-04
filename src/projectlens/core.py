"""Project structure summarization helpers."""

def summarize(files: list[str]) -> dict[str, object]:
    """Summarize source, test, and documentation paths."""
    paths = sorted(set(files))
    return {
        "files": len(paths),
        "tests": sum("test" in p.lower() for p in paths),
        "docs": sum(p.lower().endswith((".md", ".rst")) for p in paths),
    }
