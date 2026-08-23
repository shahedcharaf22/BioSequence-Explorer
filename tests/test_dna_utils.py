from dna_utils import (
    validate_dna,
    count_nucleotides,
    calculate_gc_content,
    get_complement,
    get_reverse_complement,
    find_invalid_nucleotides
)

def test_valid_dna():
    assert validate_dna("ATGC") == True

def test_invalid_dna():
    assert validate_dna("ATGX") == False

def test_count_nucleotides():
    result = count_nucleotides("AATCGG")

    assert result["A"] == 2
    assert result["T"] == 1
    assert result["C"] == 1
    assert result["G"] == 2

def test_gc_content():
    result = calculate_gc_content("GGCC")

    assert result == 100.0

def test_complement():
    result = get_complement("ATGC")

    assert result == "TACG"

def test_reverse_complement():
    result = get_reverse_complement("ATGC")

    assert result == "GCAT"

def test_find_invalid_nucleotides():
    result = find_invalid_nucleotides("ATGCXZ")

    assert result == {"X", "Z"}