---
title: "📋 Syllabus: Física Estadística"
course: "Física Estadística"
institution: "Facultad de Ciencias, UNAM"
instructor: "Dr. Roberto Antonio Zamora Zamora"
email: "roberto.zamorazamora@ciencias.unam.mx"
tags: [syllabus, course-policy, stat-phys]
---

# 📋 Syllabus: Física Estadística

**Facultad de Ciencias, UNAM**  
**Profesor:** Dr. Roberto Antonio Zamora Zamora  
**Contacto:** `roberto.zamorazamora@ciencias.unam.mx`  
**Horario y Duración:** 48 clases efectivas (2.0 horas por clase: Lunes, Miércoles y Viernes)
**Inicio del curso:** 17.08.2026

---

## 🎯 Descripción del Curso

Este curso cubre el temario oficial de **Física Estadística (FE)** de la Licenciatura en Física en la Facultad de Ciencias de la UNAM. El curso conecta los principios microscópicos de la mecánica clásica y cuántica con las leyes macroscópicas de la termodinámica, explorando la teoría de ensambles de Gibbs, estadísticas cuánticas ideales (Fermi-Dirac y Bose-Einstein), radiación de cuerpo negro, transiciones de fase y fenómenos de transporte fuera del equilibrio. 

El curso incluye un **énfasis especial en sistemas cuánticos ultrafríos y dinámica en redes**, así como herramientas computacionales en **Python** y/o **Julia** (simulaciones Monte Carlo, caminatas aleatorias clásicas/cuánticas y análisis de espacio de fases).

---

## 💯 Criterios de Evaluación

| Elemento | Porcentaje | Detalles y Reglas |
| :--- | :---: | :--- |
| **3 Exámenes Parciales** | **50%** | • **Parcial 1 (Sesión 16)**: Bloques 1 y 2.<br>• **Parcial 2 (Sesión 25)**: Bloques 3 y 4.<br>• **Parcial 3 (Sesión 36)**: Bloques 5 y 6.<br>*Punto Extra (+1 pt por examen)*: Al entregar 1 cuartilla manuscrita de síntesis/formulario. |
| **Proyecto Final** | **40%** | Trabajo en equipos (máx. 3 integrantes) o individual sobre un artículo científico de la literatura.<br>• **Semana 8–9 (Propuesta)**: 10% de la nota del proyecto.<br>• **Sesión 42 (Entrega Video 7–15 min & Código)**: 40% de la nota del proyecto.<br>• **Sesiones 43–47 (Defensas Orales 15 min)**: 50% de la nota del proyecto. |
| **Google Forms** | **10%** | Participación y retroalimentación continua (>90% de formularios semanales contestados). |

---

## 📅 Calendario

```
┌────────────────────────────────────────────────────────────────────────┐
│                      CALENDARIO Física Estadística                     │
├───────────────────────┬──────────┬─────────────────────────────────────┤
│ Bloque / Actividad    │ Sesiones │ Temas Principales                   │
├───────────────────────┼──────────┼─────────────────────────────────────┤
│ Bloque 1              │ 1 - 6    │ Probabilidad, Camino Aleatorio      │
│ Bloque 2              │ 7 - 15   │ Ensambles de Gibbs (Micro/Can/Gran) │
│ Examen Parcial 1      │ 16       │ Evaluación Bloques 1 y 2            │
│ Bloque 3              │ 17 - 22  │ Estadística Cuántica (Bose/Fermi)   │
│ Bloque 4              │ 23 - 24  │ Radiación de Cuerpo Negro           │
│ Examen Parcial 2      │ 25       │ Evaluación Bloques 3 y 4            │
│ Bloque 5              │ 26 - 30  │ Gases No Ideales e Ising            │
│ Bloque 6              │ 31 - 35  │ Fluctuaciones, Langevin y Cinética  │
│ Examen Parcial 3      │ 36       │ Evaluación Bloques 5 y 6            │
│ Bloque 7 (Especial)   │ 37 - 39  │ Ultrafríos y Redes (Seminario Colab)│
│ Talleres de Proyecto  │ 40 - 42  │ Asesoría teórica/numérica y videos  │
│ Defensas de Proyecto  │ 43 - 47  │ Defensas orales (15 min/equipo)     │
│ Cierre del Curso      │ 48       │ Calificaciones y retroalimentación  │
└───────────────────────┴──────────┴─────────────────────────────────────┘
```

---

## 📚 Plan por Sesión (48 Sesiones) 

### Bloque 1: Probabilidad en Física Estadística (Sesiones 1 a 6)
- **[[Lectures/Sesion_01_Enfoque_Microscopico_Macroscopico|Sesión 1]]**: Enfoque microscópico vs. macroscópico. Configuración de Obsidian, GitHub y Colab.
- **[[Lectures/Sesion_02_Camino_Aleatorio_1D_Distribucion_Binomial|Sesión 2]]**: Camino aleatorio 1D y distribución binomial.
- **[[Lectures/Sesion_03_Valores_Medios_Momentos_Distribucion_Gaussiana|Sesión 3]]**: Cálculo de valores medios, momentos y distribución Gaussiana para grande $N$.
- **[[Lectures/Sesion_04_Caminante_Multivariable_Distribuciones_Continuas|Sesión 4]]**: Caminante aleatorio multivariable y distribuciones continuas.
- **[[Lectures/Sesion_05_Difusion_Fisica_Distribucion_Maxwell_Boltzmann|Sesión 5]]**: Difusión física y distribución de velocidades de Maxwell-Boltzmann como caminante en el espacio de fases.
- **[[Lectures/Sesion_06_Taller_Colab_Simulacion_Caminantes_Difusion|Sesión 6]]**: Taller Colab: Simulación de caminantes aleatorios y procesos de difusión en Julia/Python.

### Bloque 2: Mecánica Estadística a la Gibbs (Sesiones 7 a 15)
- **[[Lectures/Sesion_07_Espacio_Fases_Ensamble_Microcanonico|Sesión 7]]**: Espacio de fases y ensamble Microcanónico. Postulado de probabilidades a priori iguales.
- **[[Lectures/Sesion_08_Entropia_Boltzmann_Gas_Ideal_Paradoja_Gibbs|Sesión 8]]**: Entropía de Boltzmann ($S = k_B \ln \Omega$) y gas ideal clásico. Paradoja de Gibbs.
- **[[Lectures/Sesion_09_Ensamble_Canonico_Factor_Boltzmann_Particion|Sesión 9]]**: Ensamble Canónico: Factor de Boltzmann y Función de Partición $Z$.
- **[[Lectures/Sesion_10_Conexion_Termodinamica_Energia_Libre_Helmholtz|Sesión 10]]**: Conexión con la Termodinámica: energía libre de Helmholtz, trabajo y calor.
- **[[Lectures/Sesion_11_Teorema_Equiparticion_Energia_Limites|Sesión 11]]**: Teorema de equipartición de la energía y sus límites de validez.
- **[[Lectures/Sesion_12_Ensamble_Gran_Canonico_Potencial_Quimico|Sesión 12]]**: Ensamble Gran Canónico: potencial químico $\mu$ y gran función de partición $\Xi$.
- **[[Lectures/Sesion_13_Multiplicadores_Lagrange_Derivacion_Distribuciones|Sesión 13]]**: Multiplicadores de Lagrange para la derivación de distribuciones.
- **[[Lectures/Sesion_14_Aplicaciones_Computacionales_Funciones_Particion|Sesión 14]]**: Aplicaciones computacionales de funciones de partición en Colab.
- **[[Lectures/Sesion_15_Repaso_General_Ensambles|Sesión 15]]**: Repaso general de ensambles estadísticos.

---

### 📝 Evaluación Parcial 1
- **[[Lectures/Sesion_16_Examen_Parcial_1|Sesión 16]]**: **EXAMEN PARCIAL 1** (Evaluación Bloques 1 y 2).

---

### Bloque 3: Mecánica Estadística Cuántica (Sesiones 17 a 22)
- **[[Lectures/Sesion_17_Estados_Cuanticos_Indistinguibilidad|Sesión 17]]**: Estados cuánticos de muchas partículas e indistinguibilidad.
- **[[Lectures/Sesion_18_Estadistica_Fermi_Dirac_Bose_Einstein|Sesión 18]]**: Estadística de Fermi-Dirac y Bose-Einstein desde el ensamble Gran Canónico.
- **[[Lectures/Sesion_19_Limite_Clasico_No_Degenerado_vs_Degenerado|Sesión 19]]**: Límite clásico no degenerado vs. regímenes degenerados.
- **[[Lectures/Sesion_20_Gases_Fermiones_Energia_Fermi_Presion_Degeneracion|Sesión 20]]**: Gases de Fermiones: energía de Fermi, presión de degeneración y capacidad térmica de electrones.
- **[[Lectures/Sesion_21_Gases_Bosones_Condensacion_Bose_Einstein_Ideal|Sesión 21]]**: Gases de Bosones: Condensación de Bose-Einstein (BEC) ideal y temperatura crítica $T_c$.
- **[[Lectures/Sesion_22_Capacidad_Termica_Sistemas_Bosonicos|Sesión 22]]**: Capacidad térmica en sistemas bosónicos.

### Bloque 4: Radiación de Cuerpo Negro (Sesiones 23 a 24)
- **[[Lectures/Sesion_23_Termodinamica_Estadistica_Gas_Fotones_Planck|Sesión 23]]**: Termodinámica y estadística del gas de fotones (Ley de Planck).
- **[[Lectures/Sesion_24_Limites_Stefan_Boltzmann_Wien|Sesión 24]]**: Límites de Stefan-Boltzmann y Wien.

---

### 📝 Evaluación Parcial 2
- **[[Lectures/Sesion_25_Examen_Parcial_2|Sesión 25]]**: **EXAMEN PARCIAL 2** (Evaluación Bloques 3 y 4).

---

### Bloque 5: Partículas Interactuantes, Transiciones de Fase y Modelo de Ising (Sesiones 26 a 30)
- **[[Lectures/Sesion_26_Vibraciones_Red_Solidos_Einstein_Debye|Sesión 26]]**: Vibraciones de red en sólidos (modelos de Einstein y Debye) y sistemas magnéticos.
- **[[Lectures/Sesion_27_Gases_No_Ideales_Particion_Configuracional_Virial|Sesión 27]]**: Gases no ideales: función de partición configuracional y expansión del virial.
- **[[Lectures/Sesion_28_Deduccion_Ecuacion_Van_der_Waals|Sesión 28]]**: Deducción de la ecuación de Van der Waals a partir de interacción intermolecular.
- **[[Lectures/Sesion_29_Ferromagnetismo_Interaccion_Intercambio_Espines|Sesión 29]]**: Ferromagnetismo: interacción de intercambio entre espines y modelo de Ising 1D (Matriz de transferencia).
- **[[Lectures/Sesion_30_Modelo_Ising_2D_Simulacion_Monte_Carlo|Sesión 30]]**: Modelo de Ising en 2D (Teoría de campo medio) y simulación Monte Carlo (Metropolis) en Colab.

### Bloque 6: Fluctuaciones, Procesos Irreversibles y Teoría Cinética (Sesiones 31 a 35)
- **[[Lectures/Sesion_31_Fluctuaciones_Tendencia_Equilibrio_Nyquist|Sesión 31]]**: Fluctuaciones y tendencia al equilibrio; teorema de Nyquist y fluctuación-disipación.
- **[[Lectures/Sesion_32_Movimiento_Browniano_Ecuacion_Langevin|Sesión 32]]**: Movimiento Browniano y ecuación de Langevin.
- **[[Lectures/Sesion_33_Ecuacion_Fokker_Planck_Correlacion_Temporal_Onsager|Sesión 33]]**: Ecuación de Fokker-Planck, correlación temporal y relaciones recíprocas de Onsager.
- **[[Lectures/Sesion_34_Ecuacion_Transporte_Boltzmann_Colision|Sesión 34]]**: Fundamentos de teoría cinética: la ecuación de transporte de Boltzmann y término de colisión.
- **[[Lectures/Sesion_35_Teorema_H_Boltzmann_Irreversibilidad_Navier_Stokes|Sesión 35]]**: Teorema $H$ de Boltzmann, irreversibilidad e introducción a las ecuaciones hidrodinámicas (Navier-Stokes).

---

### 📝 Evaluación Parcial 3
- **[[Lectures/Sesion_36_Examen_Parcial_3|Sesión 36]]**: **EXAMEN PARCIAL 3** (Evaluación Bloques 5 y 6).

---

### Bloque 7 (Temas Especiales): Seminario de Sistemas Cuánticos Ultrafríos y Redes (Sesiones 37 a 39)
> [!NOTE]
> Bloque complementario en formato de seminario y talleres ligeros en Google Colab (no evaluable en examen escrito).
- **[[Lectures/Sesion_37_Gases_Ultrafrios_BEC_Gross_Pitaevskii|Sesión 37]]**: Gases Ultrafríos I: Condensación de Bose-Einstein atrapada y ecuación de Gross-Pitaevskii.
- **[[Lectures/Sesion_38_Mezclas_Fermionicas_Redes_Opticas_Tight_Binding|Sesión 38]]**: Gases Ultrafríos II y Redes: Mezclas fermiónicas, redes ópticas y modelo Tight-Binding en grafos.
- **[[Lectures/Sesion_39_Quantum_Walks_Termalizacion_ETH_MBL|Sesión 39]]**: Dinámica fuera del equilibrio: Caminantes cuánticos (*quantum walks*), termalización cuántica (ETH) y localización (MBL).

---

### 🛠️ Asesoría y Defensas de Proyecto Final (Sesiones 40 a 48)
- **[[Lectures/Sesion_40_Taller_Proyecto_Asesoria_Teorica|Sesión 40]]**: 🛠️ **Taller de Proyecto Final I**: Asesoría y resolución de dudas sobre derivaciones analíticas y modelos teóricos.
- **[[Lectures/Sesion_41_Taller_Proyecto_Asesoria_Computacional|Sesión 41]]**: 🛠️ **Taller de Proyecto Final II**: Asesoría computacional, depuración de simulaciones numéricas en Colab (Python/Julia).
- **[[Lectures/Sesion_42_Taller_Proyecto_Revision_Videos_Entrega|Sesión 42]]**: 🛠️ **Taller de Proyecto Final III**: Revisión de estructura de videos, narrativa y **entrega final de video y reporte**.
- **[[Lectures/Sesion_43_47_Defensas_Orales_Proyectos|Sesiones 43 a 47]]**: 🗣️ **Defensas Orales de Proyectos Finales**: Rondas de exposición y preguntas (15 min por equipo / 10 min individual). El calendario de asignación se publica en la Sesión 39.
- **[[Lectures/Sesion_48_Cierre_Curso_Calificaciones|Sesión 48]]**: 🎓 **Cierre del Curso**: Entrega de calificaciones finales, retroalimentación global y conclusión del curso.

---

## 📖 Bibliografía

### Textos Principales
1. **[[Sources/Books/Reif_1968|Reif, F.]]** (1968). *Fundamentos de física estadística y térmica*. Editorial del Castillo, Madrid, España.
2. **[[Sources/Books/Pathria_Beale_2021|Pathria, R. K., & Beale, P. D.]]** (2021). *Statistical Mechanics* (4th ed.). Academic Press / Elsevier.

### Lecturas Complementarias y Proyectos
- Catálogo completo de artículos científicos clasificados por bloque en **[[Projects/Final_Project_Guide|Guía del Proyecto Final]]**.
- Cuadernos de código interactivos en `Notebooks/Python/` y `Notebooks/Julia/`.
