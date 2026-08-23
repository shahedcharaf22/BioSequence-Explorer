import csv

def read_dna_csv(file_path):
    samples = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["sequence"] = row["sequence"].strip().upper()
            samples.append(row)

    return samples

# Check every nucleotide one by one
def validate_dna(sequence):
    valid_nucleotides = {"A", "T", "C", "G"}

    return set(sequence).issubset(valid_nucleotides)

def find_invalid_nucleotides(sequence):
    valid_nucleotides = {"A", "T", "C", "G"}

    invalid_nucleotides = set(sequence) - valid_nucleotides

    return invalid_nucleotides
    
# Count the nucleotides
def count_nucleotides(sequence):
    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "C": sequence.count("C"),
        "G": sequence.count("G"),
    }

    return counts


# Calculate what percentage of the DNA consists of G and C
def calculate_gc_content(sequence):
    gc_content = (
        (sequence.count("G") + sequence.count("C"))
        / len(sequence)
        * 100
    )

    gc_content = round(gc_content, 2)

    return gc_content


# Generate the DNA complement
def get_complement(sequence):
    complement = ""

    for letter in sequence:
        if letter == "A":
            complement += "T"

        elif letter == "T":
            complement += "A"

        elif letter == "C":
            complement += "G"

        elif letter == "G":
            complement += "C"

    return complement


# Generate the reverse complement using slicing
def get_reverse_complement(sequence):
    complement = get_complement(sequence)

    reverse_complement = complement[::-1]

    return reverse_complement

# FILE-READING 
def read_dna_file(file_path):
    with open(file_path, "r") as file:
        sequence = file.read().strip().upper()

    return sequence

