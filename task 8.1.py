from Bio import SeqIO
for seq_record in SeqIO.parse('8.1 sequence.gb','genbank'):
    if seq_record.features:
        for feature in seq_record.features:
            if feature.type == "gene":
                if feature.strand == -1:
                    print(feature.location)
                    print(feature.location.extract(seq_record).seq, 
                          end="\n gene \n")
