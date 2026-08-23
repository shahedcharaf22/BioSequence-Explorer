from dna_utils import (
    validate_dna,
    find_invalid_nucleotides,
    count_nucleotides,
    calculate_gc_content,
    get_complement,
    get_reverse_complement,
    read_dna_file,
)

# -----------------------------
# USER INPUT + Error Handling 
# -----------------------------

try:
    
    input_choice = input(
        "Choose input method (1 = manual, 2 = file): "
    )

    if input_choice == "1":
        dna_sequence = input("Enter the DNA sequence: ").strip().upper()

    elif input_choice == "2":
        file_name = input("Enter DNA file name: ").strip()
        file_path = f"data/{file_name}"
        dna_sequence = read_dna_file(file_path)

    else:
        raise ValueError("Invalid input method. Choose 1 or 2.")


    if not dna_sequence:
        raise ValueError("DNA sequence cannot be empty.")

    # Calculate DNA sequence length
    sequence_length = len(dna_sequence)

    print("DNA Sequence:", dna_sequence)
    print("Sequence Length:", sequence_length)

    # Validate DNA
    is_valid = validate_dna(dna_sequence)

    print("Valid DNA Sequence:", is_valid)

    if not is_valid:
        
        invalid_nucleotides = find_invalid_nucleotides(dna_sequence)
        formatted_invalid = ", ".join(sorted(invalid_nucleotides))

        raise ValueError(
              f"Invalid nucleotides found: {formatted_invalid}"
        )

    # Only analyze valid DNA
    nucleotide_counts = count_nucleotides(dna_sequence)

    # Get the value stored under each nucleotide key
    print("A count:", nucleotide_counts["A"])
    print("T count:", nucleotide_counts["T"])
    print("C count:", nucleotide_counts["C"])
    print("G count:", nucleotide_counts["G"])

    gc_content = calculate_gc_content(dna_sequence)
    print(f"GC Content: {gc_content}%")

    complement = get_complement(dna_sequence)
    print("Complement:", complement)

    reverse_complement = get_reverse_complement(dna_sequence)
    print("Reverse complement:", reverse_complement)


except ValueError as error:
    print ("Error:", error)

except FileNotFoundError:
    print("Error: DNA file was not found.")



        

        
       