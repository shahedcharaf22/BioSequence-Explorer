from dna_utils import (
    validate_dna,
    find_invalid_nucleotides,
    count_nucleotides,
    calculate_gc_content,
    get_complement,
    get_reverse_complement,
    read_dna_file,
    read_dna_csv,
    
)

# -----------------------------
# USER INPUT + Error Handling 
# -----------------------------

def analyze_sequence(sequence):
    if not sequence:
        raise ValueError("DNA sequence cannot be empty.")

    sequence_length = len(sequence)
    print("Sequence Length:", sequence_length)

    is_valid = validate_dna(sequence)
    print("Valid DNA:", is_valid)

    if not is_valid:
        invalid_nucleotides = find_invalid_nucleotides(sequence)
        formatted_invalid = ", ".join(sorted(invalid_nucleotides))
        raise ValueError(
            f"Invalid nucleotides found: {formatted_invalid}"
        )

    nucleotide_counts = count_nucleotides(sequence)
    print("Nucleotide Counts:", nucleotide_counts)

    gc_content = calculate_gc_content(sequence)
    print("GC Content:", f"{gc_content}%")

    complement = get_complement(sequence)
    print("Complement:", complement)

    reverse_complement = get_reverse_complement(sequence)
    print("Reverse Complement:", reverse_complement)

    return gc_content

def analyze_dataset(samples):
    total_samples = 0
    valid_samples = 0
    invalid_samples = 0
    gc_values = []

    for sample in samples:
        total_samples += 1
    
        sample_id = sample["sample_id"]
        sequence = sample["sequence"]
    
        print("\nSample:", sample_id)
        print("Sequence:", sequence)
        
        try:
            gc_content = analyze_sequence(sequence)
            valid_samples += 1
            gc_values.append(gc_content)
    
        except ValueError as error:
            invalid_samples += 1
            print("Error:", error)
    
    if gc_values:
        average_gc = sum(gc_values) / len(gc_values)
    else:
        average_gc = 0
            
    print("\nDataset Summary")
    print("----------------")
    print("Total samples:", total_samples)
    print("Valid samples:", valid_samples)
    print("Invalid samples:", invalid_samples)
    print("Average GC content:", f"{round(average_gc, 2)}%")

    return {
        "total_samples": total_samples,
        "valid_samples": valid_samples,
        "invalid_samples": invalid_samples,
        "average_gc": round(average_gc, 2),
    }

def main():
    
    try:
        
        input_choice = input(
            "Choose input method (1 = manual, 2 = file, 3 = csv): "
        )

        if input_choice == "1":
            dna_sequence = input("Enter the DNA sequence: ").strip().upper()
            analyze_sequence(dna_sequence)

        elif input_choice == "2":
            file_name = input("Enter DNA file name: ").strip()
            file_path = f"data/{file_name}"
            dna_sequence = read_dna_file(file_path)
            analyze_sequence(dna_sequence)

        elif input_choice == "3":
            file_name = input("Enter CSV file name: ").strip()
            file_path = f"data/{file_name}"

            samples = read_dna_csv(file_path)
            analyze_dataset(samples)

        else:
            raise ValueError("Invalid input method. Choose 1, 2 or 3.")

    except ValueError as error:
        print ("Error:", error)

    except FileNotFoundError:
        print("Error: DNA file was not found.")

if __name__ == "__main__":
       main()

        
       