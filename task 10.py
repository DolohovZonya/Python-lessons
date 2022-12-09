import requests
import re
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

gene_name = 'hsa:4514'
url = f'https://rest.kegg.jp/get/{gene_name}'
geturl = requests.get(url)
url1 = f'https://www.kegg.jp/ssdb-bin/ssdb_best?org_gene={gene_name}'
get_ortho = requests.get(url1)
class Gene:
  def __init__(self, entry, organism, motif, aaseq, ntseq):
    self.entry = entry
    self.organism = organism
    self.motif = motif
    self.aaseq = aaseq
    self.ntseq = ntseq
  def __str__(self):
    return self.entry
organism, entry = gene_name.split(":")
template_motif = r"MOTIF\s+\w+:.+"
motif = re.search(template_motif, geturl.text)
if motif:
  motif = motif[0]
template_aaseq = r"AASEQ\s+\d+((?:[\sA-Z]+)+)\n"
aaseq = re.search(template_aaseq, geturl.text)
if aaseq:
  aaseq = aaseq[1]
aa_res = re.sub("\s", "", aaseq)
aa_count = set(aa_res)
aa_ras = {}
for i in aa_count:
  aa_ras[i] = aa_res.count(i)
# график по амк последовательности
#fig, ax = plt.subplots()
# ax.bar(aa_ras.keys(), aa_ras.values())
# plt.show()
template_ntseq = r"NTSEQ\s+\d+((?:[\satgc]+)+)\n"
ntseq = re.search(template_ntseq, geturl.text)
if ntseq:
  ntseq = ntseq[1]
nt_res = re.sub("\s", "", ntseq)
nt_ras = {}
n_x = []
n_y = []
nt_ras['a'] = nt_res.count('a')
nt_ras['t'] = nt_res.count('t')
nt_ras['c'] = nt_res.count('c')
nt_ras['g'] = nt_res.count('g')
# график по нк последовательности
# plt.pie(nt_ras.keys(), labels=nt_ras.values())
# plt.show()
gene = Gene(entry, organism, motif, aa_res, nt_res)
#print(gene)
ortho_res = get_ortho.text.split("Entry")[1]
ortho = r"<INPUT.+target=_ortholog>\d+</a>"
ident = r"[01]\.\d{3}"
sw_score = r"\d{3,4}\s[(]"
name = r'VALUE=\"\w+:\d+\"'
sw_c = []
id_res = re.findall(ident, get_ortho.text)
sw_res = re.findall(sw_score, get_ortho.text)
for score in sw_res:
  sw_c.append(score.split(" ")[0])
val_res = re.findall(name, get_ortho.text)
#print(id_res[:10], val_res[:10], sw_c[:10])
# подсчет коэфф корреляции пирсона
id_piers = np.array(list(map(float, id_res[0:100])))
sw_piers = np.array(list(map(float, sw_c[0:100])))
r,p = stats.pearsonr(id_piers, sw_piers)
#print(r)
names = []
for nam in val_res:
  names.append(nam.split('"')[1])
lmotif = motif.split(" ")
motifs = {}
for i in lmotif[8:]:
  motifs[i] = 0
for genes in names[0:10]:
  url2 = f'https://rest.kegg.jp/get/{genes}'
  geturl2 = requests.get(url)
  template_motif = r"MOTIF\s+\w+:.+"
  motif_ortho = re.search(template_motif, geturl.text)
  if motif_ortho:
    motif_ortho = motif_ortho[0].split(" ")
    for i in motif_ortho:
        for k in motifs.keys():
          if i == k:
            motifs[k] += 1
for i in lmotif:
  for k in motifs.keys():
    if i == k:
      motifs[k] += 1
# график по распределению доменов
# fig, ax = plt.subplots()
# ax.bar(motifs.keys(), motifs.values())
# plt.show()
#если надо было сравнивать все домены ортологов
import requests
import re
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

gene_name = 'hsa:7341'
url = f'https://rest.kegg.jp/get/{gene_name}'
geturl = requests.get(url)
url1 = f'https://www.kegg.jp/ssdb-bin/ssdb_best?org_gene={gene_name}'
get_ortho = requests.get(url1)
class Gene:
  def __init__(self, entry, organism, motif, aaseq, ntseq):
    self.entry = entry
    self.organism = organism
    self.motif = motif
    self.aaseq = aaseq
    self.ntseq = ntseq
  def __str__(self):
    return self.entry
organism, entry = gene_name.split(":")
template_motif = r"MOTIF\s+\w+:.+"
motif = re.search(template_motif, geturl.text)
if motif:
  motif = motif[0]
template_aaseq = r"AASEQ\s+\d+((?:[\sA-Z]+)+)\n"
aaseq = re.search(template_aaseq, geturl.text)
if aaseq:
  aaseq = aaseq[1]
aa_res = re.sub("\s", "", aaseq)
aa_count = set(aa_res)
aa_ras = {}
for i in aa_count:
  aa_ras[i] = aa_res.count(i)
# график по амк последовательности
#fig, ax = plt.subplots()
# ax.bar(aa_ras.keys(), aa_ras.values())
# plt.show()
template_ntseq = r"NTSEQ\s+\d+((?:[\satgc]+)+)\n"
ntseq = re.search(template_ntseq, geturl.text)
if ntseq:
  ntseq = ntseq[1]
nt_res = re.sub("\s", "", ntseq)
nt_ras = {}
n_x = []
n_y = []
nt_ras['a'] = nt_res.count('a')
nt_ras['t'] = nt_res.count('t')
nt_ras['c'] = nt_res.count('c')
nt_ras['g'] = nt_res.count('g')
# график по нк последовательности
# plt.pie(nt_ras.keys(), labels=nt_ras.values())
# plt.show()
gene = Gene(entry, organism, motif, aa_res, nt_res)
#print(gene)
ortho_res = get_ortho.text.split("Entry")[1]
ortho = r"<INPUT.+target=_ortholog>\d+</a>"
ident = r"[01]\.\d{3}"
sw_score = r"\d{3,4}\s[(]"
name = r'VALUE=\"\w+:\d+\"'
sw_c = []
id_res = re.findall(ident, get_ortho.text)
sw_res = re.findall(sw_score, get_ortho.text)
for score in sw_res:
  sw_c.append(score.split(" ")[0])
val_res = re.findall(name, get_ortho.text)
#print(id_res[:10], val_res[:10], sw_c[:10])
# подсчет коэфф корреляции пирсона
id_piers = np.array(list(map(float, id_res[0:100])))
sw_piers = np.array(list(map(float, sw_c[0:100])))
r,p = stats.pearsonr(id_piers, sw_piers)
#print(r)
names = []
for nam in val_res:
  names.append(nam.split('"')[1])
lmotif = motif.split(" ")
motifs = {}
for i in lmotif[8:]:
  motifs[i] = 0
keys = []
for genes in names[0:10]:
  url2 = f'https://rest.kegg.jp/get/{genes}'
  geturl2 = requests.get(url)
  template_motif = r"MOTIF\s+\w+:.+"
  motif_ortho = re.search(template_motif, geturl.text)
  if motif_ortho:
    motif_ortho = motif_ortho[0].split(" ")
    for k in motifs.keys():
      keys.append(k)
    for i in motif_ortho[8:]:
      for key in keys:
        if i != key:
          motifs[i] = 0
    for i in motif_ortho:
      for k in motifs.keys():
        if i == k:
          motifs[k] += 1
for i in lmotif:
  for k in motifs.keys():
    if i == k:
      motifs[k] += 1
# график по распределению доменов
# fig, ax = plt.subplots()
# ax.bar(motifs.keys(), motifs.values())
# plt.show()
