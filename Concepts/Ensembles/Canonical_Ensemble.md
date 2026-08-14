---
aliases: [NVT Ensemble, Gibbs Ensemble]
tags: [concept, ensembles, statistical-mechanics]
primary_sources:
  - "[[Sources/Books/Pathria_Beale_2011#Ch3]]"
source_register: "[[Source_Registers/Canonical_Ensemble_Sources]]"
---

# Canonical Ensemble

## One‑liner
Statistical ensemble representing a macro system in thermal equilibrium with a heat bath at fixed temperature $T$, volume $V$, and particle number $N$.

## Core idea
- Probability of microstate $r$ with energy $E_r$ is proportional to the Boltzmann factor $e^{-\beta E_r}$.
- Heat exchange occurs with the reservoir; total energy fluctuates around an average value $\langle E \rangle$.
- Temperature $T$ is fixed by the reservoir, where $\beta = 1 / (k_B T)$.
- Normalization factor is the canonical partition function $Z$.

## Key equations
- $$ P_r = \frac{e^{-\beta E_r}}{Z} $$
  - Microstate probability distribution in canonical ensemble.
- $$ Z = \sum_r e^{-\beta E_r} $$
  - Canonical partition function over all quantum states $r$.

## Related concepts
- **Depends on**: [[Concepts/Thermodynamics/Entropy]], [[Concepts/Ensembles/Partition_Function]]
- **Used in**: [[Concepts/Thermodynamics/Free_Energy]]
- **Contrast with**: [[Concepts/Ensembles/Microcanonical_Ensemble]], [[Concepts/Ensembles/Grand_Canonical_Ensemble]]

## Common pitfalls
- Confusing state sum over energy levels with sum over microstates (which requires density of states factor $g(E)$).

## See also
- Primary sources listed above. For full source list, see [[Source_Registers/Canonical_Ensemble_Sources]].
