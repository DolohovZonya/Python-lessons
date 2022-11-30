from Bio import motifs
with open('8.2 sequences.txt') as fin:
    instances = [i.strip() for i in fin]
    m = motifs.create(instances)
    pwm = m.counts.normalize()
    print(pwm.log_odds())
