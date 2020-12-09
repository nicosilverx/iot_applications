import json, requests, threading, time

codonDict = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': 'STOP', 'TAG': 'STOP',
    'TGC': 'C', 'TGT': 'C', 'TGA': 'STOP', 'TGG': 'W',
}

class Chromosome(threading.Thread):
    def __init__(self, chromosomeID):
        threading.Thread.__init__(self)
        self.chromosomeID = chromosomeID
    
    def run(self):
        protein_list = []
        protein = ""
        resp = (requests.get(f"https://api.genome.ucsc.edu/getData/sequence?genome=hg38;chrom={self.chromosomeID}")).json()
        i = 0
        while (i <= len(resp["dna"])):
            codon = ""
            try:
                codon += (resp["dna"][i].upper())
            except:
                pass
            try:
                codon += (resp["dna"][i+1].upper())
            except:
                pass
            try:
                codon += (resp["dna"][i+2].upper())
            except:
                pass

            translated_codon = codonDict.get(codon)

            if(translated_codon != 'STOP'):
                protein += str(translated_codon)
            else:
                protein_list.append(str(protein))
                protein = ""

            i += 3
        print(f"{self.chromosomeID} -> {protein_list}")

def parallel_execution():
    chromosome_list = json.load(open("chromosomes.json"))
    thread_list = []

    for chromosome in chromosome_list["chromosomes"]:
        thread = Chromosome(chromosome)
        thread_list.append(thread)
        thread.start()
    for thread in thread_list:
        thread.join()

def iterative_execution():
    chromosome_list = json.load(open("chromosomes.json"))
    for chromosome in chromosome_list["chromosomes"]: 
        protein_list = []
        protein = ""
        resp = (requests.get(f"https://api.genome.ucsc.edu/getData/sequence?genome=hg38;chrom={chromosome}")).json()
        i = 0
        while (i <= len(resp["dna"])):
            codon = ""
            try:
                codon += (resp["dna"][i].upper())
            except:
                pass
            try:
                codon += (resp["dna"][i+1].upper())
            except:
                pass
            try:
                codon += (resp["dna"][i+2].upper())
            except:
                pass

            translated_codon = codonDict.get(codon)

            if(translated_codon != 'STOP'):
                protein += str(translated_codon)
            else:
                protein_list.append(str(protein))
                protein = ""

            i += 3
        print(f"{chromosome} -> {protein_list}")

if __name__ == "__main__":
    start = time.time()
    parallel_execution()
    stop = time.time()
    execution_time = stop-start

    print(f"Execution time: {execution_time} s")
