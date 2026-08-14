---
aliases: [Canonical Partition Function, State Sum]
tags: [concept, ensembles, statistical-mechanics]
primary_sources:
  - "[[Sources/Books/Pathria_Beale_2011#Ch3]]"
source_register: "[[Source_Registers/Partition_Function_Sources]]"
---

# Partition Function

## One‑liner
Central generating function in statistical mechanics encoding the statistical properties of a system in thermal equilibrium.

## Core idea
- Encodes all thermodynamic observables (internal energy, pressure, entropy, heat capacity) via derivatives of $\ln Z$.
- Factorizes for non-interacting systems: $Z_N = Z_1^N / N!$ for identical indistinguishable particles.
- Sums over all microstates weighted by their Boltzmann factor $e^{-\beta E_r}$.

## Key equations
- $$ Z = \sum_r e^{-\beta E_r} $$
  - Discrete state sum for quantum canonical partition function.
- $$ \langle E \rangle = -\frac{\partial \ln Z}{\partial \beta} $$
  - Average internal energy calculated from logarithmic derivative of $Z$.

## Related concepts
- **Depends on**: [[Concepts/Ensembles/Canonical_Ensemble]]
- **Used in**: [[Concepts/Thermodynamics/Free_Energy]], [[Concepts/Thermodynamics/Entropy]]
- **Contrast with**: [[Concepts/Ensembles/Grand_Partition_Function]]

## Common pitfalls
- Forgetting the $1/N!$ factor for indistinguishable classical particles (Gibbs paradox).

## See also
- Primary sources listed above.
