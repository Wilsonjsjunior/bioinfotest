
import itertools

def overlap(a, b, min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start) 
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1

def scs(ss):
    shortest_sup = []
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0] 
        for i in range(len(ss)-1):
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            sup += ssperm[i+1][olen:]
        if len(shortest_sup) == 0 or len(sup) < len(shortest_sup[0]):
            shortest_sup = [sup]
        elif len(sup) == len(shortest_sup[0]):
            shortest_sup.append(sup)
    return shortest_sup
def pick_maximal_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0
    for a,b in itertools.permutations(reads, 2):
        olen = overlap(a, b, k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, best_olen

def greedy_scs(reads, k):
    read_a, read_b, olen = pick_maximal_overlap(reads, k)
    while olen > 0:
        print(len(reads))
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads)

def pick_maximal_overlap_index(reads, k):
    index = {}
    for read in reads:
        kmers = []
        for i in range(len(read) - k + 1):
            kmers.append(read[i:i+k])
        for kmer in kmers:
            if kmer not in index:
                index[kmer] = set()
            index[kmer].add(read)
    for read in reads:
        for i in range(len(read)-k+1):
            dummy = read[i:i+k]
            if dummy not in index:
                index[dummy] = set()
            index[dummy].add(read)
    reada, readb = None, None
    best_olen = 0
    for a in reads:
        for b in index[a[-k:]]:
            if a != b:
                olen = overlap(a, b, k)
                if olen > best_olen:
                    reada, readb = a, b
                    best_olen = olen
    return reada, readb, best_olen


def greedy_scs_index(reads, k):
    read_a, read_b, olen = pick_maximal_overlap_index(reads, k)
    while olen > 0:
        print(len(reads))
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_maximal_overlap_index(reads, k)
    return ''.join(reads)      


import sys
fragmentos = []
entrada = open(sys.argv[1])
for line in entrada:
    fragmentos.append(line.strip("\n").strip(" ").strip("\r"))

entrada.close()
print((scs(fragmentos)[0]))

