import pandas as pd
from dna_utils import (
    validate_dna,
    calculate_gc_content,
) 

def get_gc_content_if_valid(sequence):
    if validate_dna(sequence):
        return calculate_gc_content(sequence)

    return None
    
def load_dna_dataframe(file_path):
    df = pd.read_csv(file_path)

    df["length"] = df["sequence"].str.len()
    df["valid"] = df["sequence"].apply(validate_dna)
    df["gc_content"] = df["sequence"].apply(get_gc_content_if_valid)

    return df

def summarize_dataframe(df):
    total_samples = len(df)
    valid_samples = df["valid"].sum()
    invalid_samples = total_samples - valid_samples
    average_gc = df["gc_content"].mean()

    if pd.isna(average_gc):
        average_gc = 0

    return {
        "total_samples": total_samples,
        "valid_samples": int(valid_samples),
        "invalid_samples": int(invalid_samples),
        "average_gc": round(float(average_gc), 2),
    }