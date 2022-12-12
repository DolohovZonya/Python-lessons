from Bio import SeqIO
import re
geneticCode = {'TTT':'F', 'TTC':'F', 'TCT':'S', 'TCC':'S',
               'TAT':'Y', 'TAC':'Y', 'TGT':'C', 'TGC':'C',
               'TTA':'L', 'TCA':'S', 'TAA':None, 'TGA':None,
               'TTG':'L', 'TCG':'S', 'TAG':None, 'TGG':'W',
               'CTT':'L', 'CTC':'L', 'CCT':'P', 'CCC':'P',
               'CAT':'H', 'CAC':'H', 'CGT':'R', 'CGC':'R',
               'CTA':'L', 'CTG':'L', 'CCA':'P', 'CCG':'P',
               'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGG':'R',
               'ATT':'I', 'ATC':'I', 'ACT':'T', 'ACC':'T',
               'AAT':'N', 'AAC':'N', 'AGT':'S', 'AGC':'S',
               'ATA':'I', 'ACA':'T', 'AAA':'K', 'AGA':'R',
               'ATG':'M', 'ACG':'T', 'AAG':'K', 'AGG':'R',
               'GTT':'V', 'GTC':'V', 'GCT':'A', 'GCC':'A',
               'GAT':'D', 'GAC':'D', 'GGT':'G', 'GGC':'G',
               'GTA':'V', 'GTG':'V', 'GCA':'A', 'GCG':'A',
               'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGG':'G'}

class orf:
  def __init__(self, seq, seq1, frame, geneticCode):
    self.seq = seq
    self.frame = int(frame)
    self.geneticCode = geneticCode
    self.stt = []
    self.att = []
    self.translation = ''
    self.stop = []
    self.start = []
    self.seq1 = seq1
  def find_orf(self):
    self.seq = self.seq[self.frame:]
    stop_codons = ['TGA', 'TAG', 'TAA']
    sc, start = 0, 0
    for i in range(0, len(self.seq), 3):
      if self.seq[i:i+3] in stop_codons:
        self.stt.append(str(self.seq[sc:i+3]))
        sc, start = i+3, 0
        self.stop.append(i)
      elif self.seq[i:i+3] == 'ATG':
        sc = i
        start = 1
        self.start.append(sc)
      if start == 1 and (i+3 == len(self.seq)):
        self.stt.append(str(self.seq[sc:i+3]))
    if self.stt == []:
      self.stt.append(str(self.seq))
    for subseq in self.stt:
      for i in range(0,len(subseq), 3):
        for k, v in self.geneticCode.items():
          if subseq[i:i+3] == k and str(v):
            self.translation += str(v)
      self.att.append(self.translation)
      self.translation = ''
    for s in self.att:
      if s == 'None':
        self.att.remove(s)
    for i in self.stop:
      if i == 0:
        self.stop.remove(i)
    file_out = open("output.4.2.txt", "r")
    file_out.close()
    file_out = open("output.4.2.txt", "a")
    for i in range(len(self.att)):
      sub3 = str(self.att[i])
      sub2 = sub3.replace('None', '')
      if sub3[0] == 'M' and sub3[len(sub3)-4:len(sub3)] == 'None':
        string = sub2 + '|' + seq1 + '|' + 'complete' + '|' + str(self.start[i]) + '|' + str(self.stop[i]) + '\n'
        file_out.write(string)
      if sub3[0] == 'M' and sub3[len(sub3)-4:len(sub3)] != 'None':
        string = sub2 + '|' + seq1 + '|' + 'start' + '|' + str(self.start[i]) + '\n'
        file_out.write(string)
      if sub3[0] != 'M' and sub3[len(sub3)-4:len(sub3)] == 'None':
        string = sub2 + '|' + seq1 + '|' + 'stop' + '|' + str(self.stop[i]) + '\n'
        file_out.write(string)
      if sub3[0] != 'M' and sub3[len(sub3)-4:len(sub3)] != 'None':
        string = sub2 + '|' + seq1 + '|' + 'empty' + '\n'
        file_out.write(string)
    file_out.close()
#ввод рамки считывания
frame = input()
for record in SeqIO.parse('input.4.2.txt', 'fasta'):
  seq = record.seq
  seq1 = record.id
  trans = orf(seq, seq1, frame, geneticCode)
  trans.find_orf()
