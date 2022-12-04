import requests
import re

gene_name = 'hsa:7314'
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
template_ntseq = r"NTSEQ\s+\d+((?:[\satgc]+)+)\n"
ntseq = re.search(template_ntseq, geturl.text)
if ntseq:
  ntseq = ntseq[1]
nt_res = re.sub("\s", "", ntseq)
gene = Gene(entry, organism, motif, aa_res, nt_res)
print(gene)
ortho_res = get_ortho.text.split("Entry")[1]
ident = r"[01]\.\d{3}"
sw_score = r"\d{1-4}\("
name = r'VALUE=\"\w+:\d+\"'
id_res = re.search(ident, get_ortho.text)
sw_res = re.search(sw_score, get_ortho.text)
val_res = re.search(name, get_ortho.text)
#print(id_res, "\n", sw_res, "\n", val_res)
print(ortho_res)
