User Prompt (Detailed Context): We are studying neonatal brain endothelial cells (ECs) using in vivo Perturb-seq. Specifically, we deliver AAVs expressing guide RNAs (gRNAs) targeting various genes into ECs, aiming to find regulators of arterial EC differentiation. Each cell receives from 1–20 AAV copies, but as cells divide, these AAVs and the gRNAs get diluted or lost. Consequently, after about one week:

More slowly dividing cell types (particularly pre-artery and arterial ECs) are overrepresented in the final single-cell library.

Rapidly dividing subtypes (vein and cycling ECs) are underrepresented, because they lose the gRNAs faster.

Biologically, we know:

Arterial ECs typically differentiate from capillary ECs.

Cell cycle activity can inhibit arterial differentiation.

We have multiple time points (e.g., short ~2 days control vs. long ~8 days), but the long incubation especially enriches for arterial and pre-artery clusters.

We previously ranked gene perturbations by how much they increased “artery scores” (or proportion of arterial-like cells) relative to control guides. Now, however, we worry that some top-ranking hits might merely be genes whose knockdown disrupts proliferation, leading those cells to retain more AAV/gRNAs artificially, thus appearing to shift toward an arterial fate.

Our key questions and goals:

Distinguish genuine arterial-fate regulators from perturbations that only slow cell division.

Refine the ranking of gene perturbations by factoring out cell-cycle confounds and AAV-dilution artifacts.

Leverage multiple time-point data (e.g., 2 days control vs. 8 days) to see whether a gene’s effect is consistent or emerges only after extended culturing.

Further examine the data at a system-level for deeper insights, such as:

Pathway or regulatory network analysis to identify how genes converge on arterial specification.

Potential synergy/epistasis among gene perturbations.

Pseudotime or trajectory analyses that help trace transitions from capillary → pre-arterial → arterial states.

