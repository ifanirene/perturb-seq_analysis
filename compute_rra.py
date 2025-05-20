
import csv
from math import comb

# files
FILES = [
    # artery score tables
    "artery_score/discovery_FP_moi15_seq2_thresh10_Ucell30-celltype_artery_1_UCell_positive_weighted_scores.csv",
    "artery_score/discovery_FP_moi15_seq2_tresh10_trajectory-celltype_cap4_artery_1_positive_weighted_scores.csv",
    "artery_score/sceptre_artery_enrichment_stats_positive_weighted_scores.csv",
    "artery_score/sceptre_artery_enrichment_vs_ntc_by_grna_id_stats_d8filter10_positive_weighted_scores.csv",
    # pre-artery score tables
    "pre-artery_score/discovery_FP_moi15_seq2_thresh10_Ucell30-celltype_pre-artery_UCell_positive_weighted_scores.csv",
    "pre-artery_score/discovery_FP_moi15_seq2_tresh10_trajectory-celltype_cap4_pre.artery_positive_weighted_scores.csv",
    "pre-artery_score/sceptre_preartery_enrichment_stats_positive_weighted_scores.csv",
    "pre-artery_score/sceptre_stats_artery_pre-artery_enrichment_vs_non-targeting_by_grna_id_d8_minD8cells10_positive_weighted_scores.csv"
]

# read each file and create ranking dictionary
def read_ranking(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        gene_col = header[0]
        score_col = header[1]
        data = [row for row in reader if row]
    # sort by weighted_score descending
    data.sort(key=lambda x: float(x[1]), reverse=True)
    ranking = {}
    for idx, row in enumerate(data, start=1):
        ranking[row[0]] = idx
    length = len(data)
    return ranking, length

rankings = []
lengths = []
for f in FILES:
    r, L = read_ranking(f)
    rankings.append(r)
    lengths.append(L)


# union of genes

genes = set()
for r in rankings:
    genes.update(r.keys())

k = len(FILES)
results = []

for g in sorted(genes):
    norm_ranks = []
    for r, L in zip(rankings, lengths):
        rank = r.get(g, L + 1)
        norm_ranks.append(rank / (L + 1))
    score = min(norm_ranks)
    pvalue = 1 - (1 - score) ** k

    results.append([g, score, pvalue])

# benjamini-hochberg FDR
results.sort(key=lambda x: x[2])
N = len(results)
prev_fdr = 1.0
for i, item in enumerate(results, start=1):
    p = item[2]
    fdr = p * N / i
    if fdr > prev_fdr:
        fdr = prev_fdr
    else:
        prev_fdr = fdr
    item.append(fdr)

# save csv
# write results to a new file to avoid overwriting previous analyses
OUT_FILE = 'artery_score/rra_results_v2.csv'
with open(OUT_FILE, 'w', newline='') as f:

    writer = csv.writer(f)
    writer.writerow(['gene', 'score', 'pvalue', 'fdr'])
    for row in results:
        writer.writerow(row)
