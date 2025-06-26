# perturb-seq_analysis
Tools for analyzing perturb-seq data.

## Repository structure

```
perturb-seq_analysis/
├── data/                 # input score tables
│   ├── artery_score/
│   └── pre-artery_score/
├── docs/                 # project background, reports
├── output/               # generated figures and tables
├── src/                  # source code modules
│   ├── data_processing/
│   ├── visualization/
│   └── utils/
├── tools/                # standalone scripts
└── environment.yml       # conda environment specification
```

The `tools/compute_rra.py` script aggregates gene rankings from the CSV files in
`data/artery_score` and `data/pre-artery_score`. It writes results to
`data/artery_score/rra_results_v2.csv` so previous analyses remain intact.

An interactive volcano plot produced from the analysis is available at
`docs/interactive_perturbation_effect_volcano.html`.

Run it from the repository root with:

```bash
python tools/compute_rra.py
```
