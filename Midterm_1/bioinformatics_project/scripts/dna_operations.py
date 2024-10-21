import sys
#finding the complement sequence
def complement(dna_sequence):
    #create a map for ATGC
    complement_map = {
        'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A',
    }
    #create an empty list
    complement_seq = []
    #replace with the complement map
    for base in dna_sequence:
        if base in complement_map:
            complement_seq.append(complement_map[base])
        else:
            complement_seq.append(base)
    #single string
    return ''.join(complement_seq)

#find the reverse sequence
def reverse(sequence):
    return sequence[::-1]

#find the reverse complement
def reverse_complement(sequence):
    return reverse(complement(sequence))

def main():
    if len(sys.argv) != 2:
        print("Usage: python dna_operations.py <DNA_sequence>")
        sys.exit(1)
    input_sequence = sys.argv[1]
    # Print outputs
    print(f"Original sequence: {input_sequence}")
    print(f"Complement: {complement(input_sequence)}")
    print(f"Reverse: {reverse(input_sequence)}")
    print(f"Reverse complement: {reverse_complement(input_sequence)}")


if __name__ == "__main__":
    main()