---
aliases: [Boltzmann Entropy, Gibbs Entropy, Shannon Entropy]
tags: [concept, thermodynamics, statistical-mechanics]
primary_sources:
  - "[[Sources/Books/Callen_1985#Ch1]]"
source_register: "[[Source_Registers/Entropy_Sources]]"
---

# Entropy

## One‑liner
Quantitative measure of microscopic disorder or available microstates corresponding to a macroscopic equilibrium state.

## Core idea
- In the microcanonical ensemble, entropy is proportional to the logarithm of accessible microstates $\Omega(E, V, N)$.
- In statistical mechanics, Gibbs entropy formula generalizes Boltzmann formula to arbitrary probability distributions.
- Entropy is extensive and reaches a maximum at equilibrium in isolated systems (Second Law).

## Key equations
- $$ S = k_B \ln \Omega $$
  - Boltzmann's entropy formula for microcanonical ensemble.
- $$ S = -k_B \sum_r P_r \ln P_r $$
  - Gibbs entropy formula for general probability distribution $P_r$.

## Related concepts
- **Depends on**: [[Concepts/Ensembles/Microcanonical_Ensemble]]
- **Used in**: [[Concepts/Thermodynamics/Free_Energy]], [[Concepts/Ensembles/Canonical_Ensemble]]
- **Contrast with**: [[Concepts/Thermodynamics/Enthalpy]]

## Common pitfalls
- Assuming $S = k_B \ln \Omega$ applies directly to non-isolated systems without accounting for reservoir coupling.

## See also
- Primary sources listed above.
