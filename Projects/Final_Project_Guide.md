---
title: "🎓 Guía del Proyecto Final (40%)"
tags: [project, guidelines, evaluation, stat-phys]
---

# 🎓 Guía del Proyecto Final (40%)

El proyecto final del curso de **Física Estadística (FE)** consiste en el estudio crítico, derivación analítica y/o reproducción numérica de un artículo científico publicado en una revista internacional indexada (*American Journal of Physics*, *Journal of Mathematical Physics*, *Physica A*, *Physical Review*, etc.) o en su defecto un tema de frontera relacionado con los contenidos del curso.

> [!IMPORTANT]
> **Modalidad y Reporte**: El proyecto puede realizarse individualmente o en equipos (máximo 3 integrantes). **No se requiere reporte escrito final**; la evaluación se basa en la propuesta con justificación a mitad de semestre, el entregable en video/materiales complementarios y la **defensa oral individual** de cada estudiante.

---

## 🗓️ Cronograma y Ponderación de Entregables

| Etapa | Sesión / Fecha | Entregable | Ponderación en el Proyecto | Ponderación Final Curso |
| :--- | :---: | :--- | :---: | :---: |
| **1. Propuesta con Justificación** | **[[Lectures/Sesion_15_Aplicaciones_Computacionales_Funciones_Particion\|Sesión 15]]** | Documento breve (1–2 páginas) según [[Projects/Paper_Proposal_Template\|Plantilla de Propuesta]]. | **10%** | **4%** |
| **2. Video + Materiales Complementarios** | **[[Lectures/Sesion_43_Ecuaciones_Hidrodinamica_Navier_Stokes\|Sesión 43]]** | Video explicativo (7 a 15 min) + código en Colab (Python/Julia) y diapositivas. | **30%** | **12%** |
| **3. Defensa Oral Individual** | **[[Lectures/Sesion_47_Defensas_Orales_Proyectos_Ronda_1\|Sesiones 47]]–[[Lectures/Sesion_48_Defensas_Orales_Ronda_2_Cierre_Curso\|48]]** | Entrevista y discusión oral individual (10–15 min por estudiante). | **60%** | **24%** |

---

## 📑 1. Requisitos de la Propuesta con Justificación (Sesión 15)

La entrega de la propuesta se realiza a mitad del semestre (**Sesión 15**) subiendo el documento (1–2 páginas en Markdown o PDF) al repositorio según la [[Projects/Paper_Proposal_Template|Plantilla de Propuesta]].

Esta propuesta cumple tres funciones pedagógicas indispensables:
1. **Evitar artículos imposibles**: Garantizar que el artículo no sea inaccesible, puramente experimental sin teoría reproducible, o desconectado del nivel del curso.
2. **Lectura y planeación temprana**: Fomentar la asimilación del paper antes de la recta final del semestre.
3. **Entrenamiento de criterio científico**: Argumentar con rigor por qué el artículo es relevante para el temario, qué herramientas analíticas o computacionales se usarán y cuál es la estrategia de solución.

### Contenido obligatorio de la propuesta:
1. **Ficha Bibliográfica**: Título, autores, revista, año y DOI/enlace.
2. **Justificación de Elección**: Conexión explícita con al menos un bloque del curso (ej. Bloques 3, 5, 6 u 8).
3. **Metodología y Objetivos**: Especificar si el proyecto es preponderantemente analítico/teórico, numérico/computacional (reproducción en Colab), o mixto.
4. **Viabilidad**: Herramientas a utilizar (cálculo analítico, simulaciones Monte Carlo, caminatas aleatorias, diagonalización, etc.).
5. **Declaración y Prompts de IA**: Se permite el uso de IA generativa para explorar candidatos bibliográficos o sintetizar literatura, siempre que se documenten los *prompts* utilizados en el apéndice. La justificación debe reflejar criterio propio.

---

## 📹 2. Requisitos del Video y Materiales (Sesión 43)

El video debe tener una duración de **7 a 15 minutos** y compartirse mediante un enlace público o accesible (YouTube, Vimeo, Google Drive):
- **Introducción y Motivación** (2–3 min): Contexto del problema físico y relevancia en física estadística.
- **Desarrollo Metodológico** (4–8 min): Presentación de las derivaciones matemáticas clave o demostración interactiva de las simulaciones en Python/Julia.
- **Resultados y Discusión Crítica** (2–4 min): Análisis de los hallazgos, contraste con la literatura y conclusiones.
- **Materiales adjuntos**: Cuaderno de Google Colab (`.ipynb` o `.jl`) debidamente documentado, ejecutable y reproducibles, junto con las diapositivas o figuras de apoyo.

---

## 🗣️ 3. Defensa Oral Individual (Sesiones 47 y 48)

- **Formato**: Discusión oral individual de **10 a 15 minutos por estudiante** con el profesor.
- **Evaluación**: Se evaluará el dominio conceptual individual, la comprensión de las hipótesis y aproximaciones físicas, y la coherencia con la justificación planteada en la Sesión 15.
- **Logística**: Si el número de alumnos requiere tiempo adicional fuera de las sesiones 47 y 48, se agendarán turnos en horarios de oficina durante esa misma semana.

---

## ⚖️ Criterios de Evaluación del Proyecto Final

| Criterio | Descripción | Ponderación |
| :--- | :--- | :---: |
| **Propuesta & Justificación Científica (Sesión 15)** | Claridad en la selección, viabilidad, conexión sólida con el temario y transparencia en IA. | **10%** |
| **Calidad del Video & Materiales (Sesión 43)** | Síntesis concisa (7–15 min), audio/imagen claros, código reproducible en Colab (Python/Julia) y rigor visual. | **30%** |
| **Defensa Oral Individual & Dominio Físico (Sesiones 47–48)** | Comprensión individual profunda, solidez conceptual en respuestas y capacidad de análisis crítico. | **60%** |

---

## 📚 Catálogo de Artículos Recomendados por Bloque

Los estudiantes pueden seleccionar libremente uno de los siguientes artículos del catálogo oficial del curso o proponer un artículo equivalente previa autorización:

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
