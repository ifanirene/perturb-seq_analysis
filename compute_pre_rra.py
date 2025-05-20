import csv
from math import comb

FILES = [
    'pre-artery_score/discovery_FP_moi15_seq2_thresh10_Ucell30-celltype_pre-artery_1_UCell_positive_weighted_scores.csv',
    'pre-artery_score/discovery_FP_moi15_seq2_tresh10_trajectory-celltype_cap4_pre-artery_1_positive_weighted_scores.csv',
    'pre-artery_score/sceptre_pre-artery_enrichment_stats_positive_weighted_scores.csv',
    'pre-artery_score/sceptre_pre-artery_enrichment_vs_ntc_by_grna_id_stats_d8filter10_positive_weighted_scores.csv',
]


def read_ranking(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        data = [row for row in reader if row]
    data.sort(key=lambda x: float(x[1]), reverse=True)
    ranking = {row[0]: idx for idx, row in enumerate(data, start=1)}
    return ranking, len(data)


# Beta CDF for small integer parameters using binomial series

def beta_cdf(x, a, b):
    n = a + b - 1
    prob = 0.0
    for i in range(a, n + 1):
        prob += comb(n, i) * (x ** i) * ((1 - x) ** (n - i))
    return prob


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
    norm = []
    for r, L in zip(rankings, lengths):
        rank = r.get(g, L + 1)
        norm.append(rank / (L + 1))
    norm.sort()
    pvals = [beta_cdf(n, j + 1, k - j) for j, n in enumerate(norm)]
    pvalue = min(pvals)
    score = norm[0]
    results.append([g, score, pvalue])

# Benjamini-Hochberg FDR
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

with open('pre-artery_score/rra_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['gene', 'score', 'pvalue', 'fdr'])
    for row in results:
        writer.writerow(row)
