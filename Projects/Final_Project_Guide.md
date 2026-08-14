---
title: "🎓 Guía del Proyecto Final (40%)"
tags: [project, guidelines, evaluation, stat-phys]
---

# 🎓 Guía del Proyecto Final (40%)

El proyecto final del curso de **Física Estadística (FE)** impartido por el **Dr. Roberto Antonio Zamora Zamora** consiste en el estudio, condensación crítica, derivación analítica o reproducción numérica de un artículo científico publicado en una revista internacional indexada (*American Journal of Physics*, *Journal of Mathematical Physics*, *Physica A*, etc.).

---

## 🗓️ Cronograma y Entregables

| Etapa | Semana / Sesión | Entregable | Ponderación en el Proyecto |
| :--- | :---: | :--- | :---: |
| **1. Selección de Artículo & Propuesta** | **Semana 8–9** | Propuesta escrita de 1 página según formato [[Projects/Paper_Proposal_Template]]. | **10%** |
| **2. Avance Opcional / Script** | **Semana 12** | Asesoría para resolver dudas analíticas o depurar código en Python/Julia. | Feedback |
| **3. Entregable en Video** | **Cierre Semestre** | Video dinámico de 7 a 15 minutos en YouTube/Vimeo/Drive. | **40%** |
| **4. Defensa Oral** | **[[Lectures/Sesion_48_Cierre_Proyectos_Finales|Sesión 48]]** | Entrevista y discusión oral de 15 minutos con el profesor. | **50%** |

---

## 📚 Catálogo de Artículos Recomendados por Bloque

Los estudiantes pueden seleccionar libremente uno de los siguientes 20 artículos del catálogo oficial del curso o proponer un artículo equivalente previa autorización del profesor:

### Bloque 1: Probabilidad, Caminos Aleatorios y Distribución de Velocidades
1. **[[Sources/Papers/Franceschetti_1993|Franceschetti et al. (1993)]]**: *The random walk as an eigenvalue problem*, Am. J. Phys. 61, 1111–1113.
2. **[[Sources/Papers/Kostinski_2016|Kostinski & Amir (2016)]]**: *An elementary derivation of first and last return times of 1D random walks*, Am. J. Phys. 84, 57–60.
3. **[[Sources/Papers/Shirts_2007|Shirts (2007)]]**: *Derivation of the Maxwell-Boltzmann distribution function from the microcanonical ensemble*, Am. J. Phys. 75, 915–920.
4. **[[Sources/Papers/Novak_1970|Novak & Bortz (1970)]]**: *The Evolution of the Two-Dimensional Maxwell-Boltzmann Distribution*, Am. J. Phys. 38, 1402–1406.

### Bloque 2: Mecánica Estadística a la Gibbs y Ensambles
5. **[[Sources/Papers/Salagaram_2011|Salagaram & Chetty (2011)]]**: *Enhancing the understanding of entropy through computation*, Am. J. Phys. 79, 1127–1132.
6. **[[Sources/Papers/Touchette_2008|Touchette (2008)]]**: *Simple spin models with non-concave entropies*, Am. J. Phys. 76, 26–30.
7. **[[Sources/Papers/deOliveira_1998|de Oliveira (1998)]]**: *Thermodynamic and statistical properties of the classical ideal gas*, Am. J. Phys. 66, 1097–1101.
8. **[[Sources/Papers/Lima_2015|Lima (2015)]]**: *Generalized equipartition theorem and confining walls*, Am. J. Phys. 83, 539–544.
9. **[[Sources/Papers/Griffiths_1969|Griffiths (1969)]]**: *Statistical ensembles and thermodynamic functions*, Am. J. Phys. 37, 65–67.

### Bloque 3: Mecánica Estadística Cuántica (Fermi & Bose)
10. **[[Sources/Papers/Siegert_1957|Siegert (1957)]]**: *Derivation of the Energy-Distribution Formulas of Quantum Statistics*, Am. J. Phys. 25, 411–414.
11. **[[Sources/Papers/Vigfusson_1981|Vigfusson (1981)]]**: *Applications of Mellin transforms to the statistical mechanics of ideal quantum gases*, Am. J. Phys. 49, 1141–1145.
12. **[[Sources/Papers/Kanchanapusakit_2023|Kanchanapusakit & Tanalikhit (2023)]]**: *Force on a moving object in an ideal quantum gas*, Am. J. Phys. 91, 932–942.

### Bloque 4: Radiación de Cuerpo Negro
13. **[[Sources/Papers/Marr_2012|Marr & Wilkin (2012)]]**: *A better presentation of Planck's radiation law*, Am. J. Phys. 80, 399–405.
14. **[[Sources/Papers/Boyer_2018|Boyer (2018)]]**: *Blackbody radiation in classical physics: A historical perspective*, Am. J. Phys. 86, 495–509.

### Bloque 5: Transiciones de Fase, Gases Reales y Modelo de Ising
15. **[[Sources/Papers/Valladares_1975|Valladares (1975)]]**: *The Debye model in n dimensions*, Am. J. Phys. 43, 308–311.
16. **[[Sources/Papers/Nairn_1972|Nairn & Kilpatrick (1972)]]**: *van der Waals, Boltzmann, and the Fourth Virial Coefficient of Hard Spheres*, Am. J. Phys. 40, 503–515.
17. **[[Sources/Papers/Stephen_1972|Stephen & Mittag (1972)]]**: *A new representation of the solution of the Ising model*, J. Math. Phys. 13, 1944–1951.
18. **[[Sources/Papers/Baxter_1991|Baxter (1991)]]**: *On solving the Ising model functional relation without elliptic functions*, Physica A 177, 101–108.

### Bloque 6: Fluctuaciones, Movimiento Browniano e Irreversibilidad
19. **[[Sources/Papers/Gillespie_1993|Gillespie (1993)]]**: *Fluctuation and dissipation in Brownian motion*, Am. J. Phys. 61, 1077–1083.
20. **[[Sources/Papers/deGrooth_1999|de Grooth (1999)]]**: *A simple model for Brownian motion leading to the Langevin equation*, Am. J. Phys. 67, 1248–1252.
21. **[[Sources/Papers/Allahverdyan_2012|Allahverdyan & Hovhannisyan (2012)]]**: *Origin of the thermodynamic time arrow demonstrated in a realistic statistical system*, Am. J. Phys. 80, 700–707.

---

## 📑 Requisitos de la Propuesta (Semana 8-9)

Entregar la propuesta en Markdown o PDF con el formato [[Projects/Paper_Proposal_Template]]:
1. **Ficha Bibliográfica**: Título, autores, revista, año y DOI.
2. **Justificación**: Conexión con los temas vistos en el curso.
3. **Objetivos**: Especificar si el proyecto es preponderantemente analítico/teórico o numérico/computacional (reproducción de figuras en Python/Julia).
4. **Declaración de IA**: Transparencia sobre herramientas LLM consultadas.

---

## 📹 Requisitos del Video (7–15 min)

- **Introducción** (2–3 min): Planteamiento del problema físico.
- **Desarrollo** (4–8 min): Deducciones matemáticas clave o demostración del código en Colab.
- **Conclusiones** (2–4 min): Análisis crítico de los resultados y discusión.

---

## 🗣️ Defensa Oral (Sesión 48)

- Exposición directa y sesión de preguntas conceptuales individuales/equipo de 15 minutos con el profesor.

---

## ⚖️ Rúbrica de Evaluación

| Criterio | Descripción | Puntaje |
| :--- | :--- | :---: |
| **Comprensión Física & Rigor** | Dominio de las ecuaciones, aproximaciones y fundamentos. | 35% |
| **Calidad del Video & Claridad** | Síntesis concisa, audio claro y apoyos visuales (7–15 min). | 25% |
| **Defensa Oral & Intuición** | Respuestas precisas durante la entrevista en Sesión 48. | 30% |
| **Transparencia en IA & Formato** | Entrega puntual de propuesta y bitácora de prompts. | 10% |
