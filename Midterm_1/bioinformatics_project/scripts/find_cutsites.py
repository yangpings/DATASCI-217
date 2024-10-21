import sys
#define reading the fasta file
def read_fasta(file_path):
    with open(file_path, 'r') as file:
        #ignore the first seq >
        sequence = ''.join(line.strip() for line in file if not line.startswith('>'))
    return sequence

#find cut sites
def find_cut_sites(dna_seq, cut_site):
    cut_site_length = len(cut_site.replace('|', ''))  # Remove '|' and get length
    #initialize cut position list
    cut_site_positions = []
    # Find first occurrence of the cut site
    index = dna_seq.find(cut_site.replace('|', ''))
    #while there is still sequences
    while index != -1:
        cut_site_positions.append(index)  # Store start position
        index = dna_seq.find(cut_site.replace('|', ''), index + 1)  # Search next occurrence
    return cut_site_positions

#find pairs in the sequence
def find_distant_pairs(positions, min_distance=80000, max_distance=120000):
    #initialize pairs list
    pairs = []
    num_positions = len(positions)
    #find pairs distantly in range 80000-120000
    for i in range(num_positions):
        for j in range(i + 1, num_positions):
            distance = positions[j] - positions[i]
            if min_distance <= distance <= max_distance:
                pairs.append((positions[i], positions[j]))
    return pairs

def main():
    #set system messages and criteria for input files with three arguments
    if len(sys.argv) != 3:
        print("Usage: python find_cutsites.py <FASTA_file_path> <cut_site_sequence>")
        sys.exit(1)
    # set first and second argument
    fasta_path = sys.argv[1]
    cut_site_sequence = sys.argv[2]
    # Read the DNA sequence
    dna_seq = read_fasta(fasta_path)
    # Find all occurrences of the cut site
    cut_site_positions = find_cut_sites(dna_seq, cut_site_sequence)
    # Find pairs 80,000 to 120,000 pairs apart
    distant_pairs = find_distant_pairs(cut_site_positions)
    # Print results
    print(f"Analyzing cut site: {cut_site_sequence}")
    print(f"Total cut sites found: {len(cut_site_positions)}")
    print(f"Cut site pairs 80-120 kbp apart: {len(distant_pairs)}")
    print("First 5 pairs:")
    for i, (pos1, pos2) in enumerate(distant_pairs[:5]):
        print(f"{i + 1}. {pos1} - {pos2}")

    # Save results to distant_cutsite_summary.txt in the results directory
    with open('C:/Users/ericy/PycharmProjects/DATASCI-217/Midterm_1/bioinformatics_project/results/distant_cutsite_summary.txt', 'w') as summary_file:
        summary_file.write(f"Analyzing cut site: {cut_site_sequence}\n")
        summary_file.write(f"Total cut sites found: {len(cut_site_positions)}\n")
        summary_file.write(f"Cut site pairs 80-120 kbp apart: {len(distant_pairs)}\n")
        summary_file.write("First 5 pairs:\n")
        for i, (pos1, pos2) in enumerate(distant_pairs[:5]):
            summary_file.write(f"{i + 1}. {pos1} - {pos2}\n")


if __name__ == "__main__":
    main()