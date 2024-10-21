import random
import os
#setting dimensions
dna_length = 1000000
dna_width = 80
dna_sequence = []
formatted_sequence = []
#generate nucleotides
nucleotides = ['A', 'C', 'G', 'T']
#sample from four letter 1 million times with replacement
for _ in range(dna_length):
    dna_sequence.append(random.choice(nucleotides))
#joining in as a string
dna_sequence = ''.join(dna_sequence)
# 80 chars in one line
for i in range(0, dna_length, dna_width):
    formatted_sequence.append(dna_sequence[i:i + dna_width])
#make into a single string
formatted_sequence = '\n'.join(formatted_sequence)
#generate directory and file name
output_dir = "C:/Users/ericy/PycharmProjects/DATASCI-217/Midterm_1/bioinformatics_project/data"
output_name = "random_sequence.fasta"
#check if the directory exists
os.makedirs(output_dir, exist_ok=True)
#write out the file as a fasta file.
with open(os.path.join(output_dir, output_name), 'w') as fasta_file:
    # Optionally add a header
    fasta_file.write(f">random_sequence\n")
    fasta_file.write(formatted_sequence + "\n")
print(f"Random DNA sequence generated and saved to {os.path.join(output_dir, output_name)}")


