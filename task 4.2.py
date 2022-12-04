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
  def __init__(self, seq, frame, geneticCode):
    self.seq = seq
    self.frame = int(frame)
    self.geneticCode = geneticCode
    self.stt = []
    self.start = 0
    self.stop = 0
    self.translation = ''
    self.a = 0
    self.b = 0
  def find_orf(self):
    #выбор рамки считывания
    for i in range(int(self.frame), len(self.seq)-2,3):
      self.stt.append(str(self.seq[i:i+3]))
    try:
      self.start += self.stt.index("ATG")*3
    except:
      self.start = -1
    try:
      self.stop += self.stt.index("TGA")*3 or self.stt.index("TAG")*3 or self.stt.index("TAA")*3
    except:
      self.stop = -1
    print(self.start, self.stop)
    print(self.stt)
    #определение условий трансляции
    while self.a != -1 and self.b != -1:
      if self.stop > self.start:
        for i in range(int(self.start/3), int(self.stop/3)):
          for k, v in self.geneticCode.items():
            if k == self.stt[i]:
                self.translation += str(v)
            self.a += str(self.stt).find('ATG')
            if self.a != -1:
              self.start = self.a
            self.b += str(self.stt).find('TAG') or str(self.stt).find('TGA') or str(self.stt).find('TAA')
            if self.b != -1:
                self.stop = self.b
        for i in range(int(self.stop/3), len(self.stt)):
          for k, v in self.geneticCode.items():
              if k == self.stt[i]:
                  self.translation += str(v)
              self.a += str(self.stt).find('ATG')
              if self.a != -1:
                self.start = self.a
              self.b += str(self.stt).find('TAG') or str(self.stt).find('TGA') or str(self.stt).find('TAA')
              if self.b != -1:
                  self.stop = self.b
        if self.stop < self.start:
          for i in range(0, int(self.stop/3)):
            for k, v in self.geneticCode.items():
              if k == self.stt[i]:
                  self.translation += str(v)
          self.a += str(self.stt).find('ATG')
          if self.a != -1:
            self.start = self.a
          self.b += str(self.stt).find('TAG') or str(self.stt).find('TGA') or str(self.stt).find('TAA')
          if self.b != -1:
              self.stop = self.b
      print(str(self.translation))
      print(self.start, self.stop)
frame = input() 
for record in SeqIO.parse('input.4.2 - Copy.txt', 'fasta'):
  seq = record.seq
  trans = orf(seq, frame, geneticCode)
  trans.find_orf()
