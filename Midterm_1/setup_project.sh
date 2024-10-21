#this is the shell script for setting up directories and working files
set -e # just in case any command fails
#Create a main project directory called "bioinformatics_project" and create the following subdirectories:
#data
mkdir -p bioinformatics_project/data
#scripts
mkdir -p bioinformatics_project/scripts
#results
mkdir -p bioinformatics_project/results
#create python files in scripts directory
touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py
#In the results directory, create an empty file named "cutsite_summary.txt".
touch bioinformatics_project/results/distant_cutsite_summary.txt
#In the data directory, create an empty file named "random_sequence.fasta".
touch bioinformatics_project/data/random_sequence.fasta
#Create a README.md file in the main project directory with a brief description of the project structure.
touch bioinformatics_project/README.md
#writing contents in README.md
echo "The bioinformatics project consists of three working directories: data, scripts, and results." >> bioinformatics_project/README.md
echo "Data has a raw DNA random_sequence.fasta, Scripts has generate_fasta.py, dna_operations.py, and find_cutsites.py" >> bioinformatics_project/README.md
echo "Finally, Results has a cutsite_summary.txt" >> bioinformatics_project/README.md
echo "Project directory structure created successfully:
your_repository/
├── data/
├── scripts/
│   ├── generate_fasta.py
│   ├── dna_operations.py
│   └── find_cutsites.py
├── results/
└── README.md"
#make it executable
#chmod +x setup_project.sh
#executable using bash setup_project.sh


