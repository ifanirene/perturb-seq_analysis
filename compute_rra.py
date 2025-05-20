"""Compute Robust Rank Aggregation across multiple score tables."""

import csv
from math import comb

# files
FILES = [
    'artery_score/discovery_FP_moi15_seq2_thresh10_Ucell30-celltype_artery_1_UCell_positive_weighted_scores.csv',
    'artery_score/discovery_FP_moi15_seq2_tresh10_trajectory-celltype_cap4_artery_1_positive_weighted_scores.csv',
    'artery_score/sceptre_artery_enrichment_stats_positive_weighted_scores.csv',
    'artery_score/sceptre_artery_enrichment_vs_ntc_by_grna_id_stats_d8filter10_positive_weighted_scores.csv'
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

# union of genes across all lists
genes = set()
for r in rankings:
    genes.update(r.keys())

k = len(FILES)


def beta_cdf(x: float, a: int, b: int) -> float:
    """Beta distribution CDF for integer parameters."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    n = a + b - 1
    total = 0.0
    for i in range(a, n + 1):
        total += comb(n, i) * (x ** i) * ((1 - x) ** (n - i))
    return total


results = []
for g in sorted(genes):
    norm_ranks = []
    for r, L in zip(rankings, lengths):
        rank = r.get(g, L + 1)
        norm_ranks.append(rank / (L + 1))
    norm_ranks.sort()
    # order-specific p-values based on Beta distribution
    order_pvals = [beta_cdf(norm_ranks[j], j + 1, k - j) for j in range(k)]
    pvalue = min(order_pvals)
    score = norm_ranks[0]
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
with open('artery_score/rra_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['gene', 'score', 'pvalue', 'fdr'])
    for row in results:
        writer.writerow(row)
