dna_sequence = input("Enter the DNA sequence: ").strip()

# calcualte dna sequence length
sequence_length = len(dna_sequence)

print("DNA Sequence: " + dna_sequence )
print("Sequence Length: ", sequence_length)

# checks every nucleotide one by one.
def validate_dna(sequence):

    # assume it's valid
    is_valid = True

    # For Loop: check whether a DNA sequence is valid
    for letter in sequence :
       if letter not in "ATCG":
          is_valid = False

    return is_valid 

# 1. Take dna_sequence
# 2. send it to the validate_dna() function to check it
# 3. store the result (True or False) inside is_valid
is_valid = validate_dna(dna_sequence)

print("Valid DNA Sequence:", is_valid)

# function: count the nucleotides
def count_nucleotides(sequence):
    
    counts = {
     "A" : sequence.count("A"),
     "T" : sequence.count("T"),
     "C" : sequence.count("C"),
     "G" : sequence.count("G"),
}
    return counts

# What percentage of the DNA sequence consists of G and C.
def calculate_gc_content(sequence):
    gc_content = ((sequence.count("G") + sequence.count("C") ))/(len(sequence)) * 100 
    gc_content = round(gc_content, 2)

    return gc_content

# DNA complement
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

# reverse complement using slicing
def get_reverse_complement(sequence):
    complement = get_complement(sequence)

    reverse_complement = complement[::-1]

    return reverse_complement 

if is_valid:

   nucleotide_counts = count_nucleotides(dna_sequence)

   # get the value stored under the key "letter"
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
     
else:
    print("Error: DNA sequence contains invalid nucleotides.")