# perturb-seq_analysis
Tools for analyzing perturb-seq data.

The `compute_rra.py` script aggregates gene rankings from the four tables in the
`artery_score` directory and generates an RRA results file. The latest analysis
writes to `artery_score/rra_results_v2.csv` so previous results remain intact.
