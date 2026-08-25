import pandas as pd

from data_analysis import (
    load_dna_dataframe,
    summarize_dataframe,
)

def test_load_dna_dataframe():
    df = load_dna_dataframe("data/dna_samples.csv")

    assert len(df) == 4
    assert "length" in df.columns
    assert "valid" in df.columns
    assert "gc_content" in df.columns

def test_summarize_dataframe():
    df = load_dna_dataframe("data/dna_samples.csv")

    summary = summarize_dataframe(df)

    assert summary["total_samples"] == 4
    assert summary["valid_samples"] == 3
    assert summary["invalid_samples"] == 1
    assert summary["average_gc"] == 50.0

def test_summarize_dataframe_all_invalid():
    df = pd.DataFrame({
        "valid": [False, False],
        "gc_content": [None, None],
    })

    summary = summarize_dataframe(df)

    assert summary["total_samples"] == 2
    assert summary["valid_samples"] == 0
    assert summary["invalid_samples"] == 2
    assert summary["average_gc"] == 0