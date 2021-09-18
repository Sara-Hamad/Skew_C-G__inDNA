import numpy as np
from matplotlib import pyplot as plt

def skew (genome):
    track = []
    track_of_base=0
    for base in genome:
        if base == "C":
            track_of_base -= 1
            track .append(track_of_base)
        elif base == "G":
            track_of_base += 1
            track.append(track_of_base)
        else:
            track.append(track_of_base)
    x =np.zeros(len(genome))
    for i in range(len(x)):
        x[i]=i+1
    plt.plot(x, track)
    plt.show()



with open("DNA.fasta", "r") as fasta:
    genome = fasta.read()
    skew(genome)
