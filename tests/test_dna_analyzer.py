from dna_analyzer import analyze_dataset


def test_analyze_dataset():
    samples = [
        {"sample_id": "sample_1", "sequence": "ATGC"},
        {"sample_id": "sample_2", "sequence": "GGCC"},
        {"sample_id": "sample_3", "sequence": "ATGX"},
    ]

    result = analyze_dataset(samples)

    assert result["total_samples"] == 3
    assert result["valid_samples"] == 2
    assert result["invalid_samples"] == 1
    assert result["average_gc"] == 75.0


def test_analyze_dataset_all_invalid():
    samples = [
        {"sample_id": "sample_1", "sequence": "ATGX"},
        {"sample_id": "sample_2", "sequence": "XYZ"},
    ]

    result = analyze_dataset(samples)

    assert result["total_samples"] == 2
    assert result["valid_samples"] == 0
    assert result["invalid_samples"] == 2
    assert result["average_gc"] == 0