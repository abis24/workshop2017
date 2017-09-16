file = open("../rosalind_input/rna.txt","r")
dnaFromFile = file.readline()
dna = dnaFromFile.strip()
# dna ="GATGGAACTTGACTACGTAAATT"
rna = ""

# this for loop loops through every nucleotide
for nu in dna:
	if nu == "T":
		rna = rna + "U"
	else:
		rna = rna + nu
	
print (rna)
