# 📚 Física Estadística (2027-1) — Facultad de Ciencias, UNAM

**Profesor:** Dr. Roberto Antonio Zamora Zamora  
**Contacto:** `roberto.a.zamorazamora@gmail.com`  
**Duración:** 48 sesiones efectivas (2.0 horas por sesión: Lunes, Miércoles y Viernes)

Repositorio oficial y bóveda de conocimiento digital del curso de **Física Estadística (FE)** en la Facultad de Ciencias de la UNAM. El material combina rigor analítico en física teórica con simulaciones computacionales en **Python** y **Julia**, además de un énfasis especial en **gases cuánticos ultrafríos** y **dinámica en redes**.

---

## 🎯 Esquema de Evaluación

| Elemento | Ponderación | Detalles |
| :--- | :---: | :--- |
| **3 Exámenes Parciales** | **50%** | • **Parcial 1 (Sesión 16)**: Bloques 1 y 2.<br>• **Parcial 2 (Sesión 25)**: Bloques 3 y 4.<br>• **Parcial 3 (Sesión 39)**: Bloques 5 y 6.<br>*Bonificación (+1 pt)*: Al entregar 1 cuartilla manuscrita de síntesis. |
| **Proyecto Final** | **40%** | Análisis de un artículo científico en equipo o individual.<br>• **Semana 8–9**: Propuesta de 1 página (10%).<br>• **Cierre**: Video dinámico de 7–15 min (40%).<br>• **Sesión 48**: Defensa oral de 15 min (50%). |
| **Google Forms** | **10%** | Participación y retroalimentación semanal (>90% completados). |

---

## 🗓️ Calendario Sintético del Curso

```
┌────────────────────────────────────────────────────────────────────────┐
│                      CALENDARIO SINTÉTICO FE                           │
├───────────────────────┬──────────┬─────────────────────────────────────┤
│ Bloque / Actividad    │ Sesiones │ Temas Principales                   │
├───────────────────────┼──────────┼─────────────────────────────────────┤
│ Bloque 1              │ 1 - 6    │ Probabilidad, Camino Aleatorio      │
│ Bloque 2              │ 7 - 15   │ Ensambles de Gibbs (Micro/Can/Gran) │
│ Examen Parcial 1      │ 16       │ Evaluación Bloques 1 y 2            │
│ Bloque 3              │ 17 - 22  │ Estadística Cuántica (Bose/Fermi)   │
│ Bloque 4              │ 23 - 24  │ Radiación de Cuerpo Negro           │
│ Examen Parcial 2      │ 25       │ Evaluación Bloques 3 y 4            │
│ Bloque 5              │ 26 - 33  │ Gases No Ideales e Ising            │
│ Bloque 6              │ 34 - 38  │ Fluctuaciones y Fokker-Planck       │
│ Examen Parcial 3      │ 39       │ Evaluación Bloques 5 y 6            │
│ Bloque 7              │ 40 - 42  │ Teoría Cinética y Boltzmann         │
│ Bloque 8 (Especial)   │ 43 - 47  │ Ultrafríos y Redes (NO EVALUABLE)   │
│ Cierre Proyectos      │ 48       │ Evaluación Oral de Proyectos        │
└───────────────────────┴──────────┴─────────────────────────────────────┘
```

---

## 📖 Bibliografía

1. **Reif, F.** (1968). *Fundamentos de física estadística y térmica*. Editorial del Castillo, Madrid, España.
2. **Pathria, R. K., & Beale, P. D.** (2021). *Statistical Mechanics* (4th ed.). Academic Press / Elsevier.
3. Catálogo de 20 artículos científicos en `Projects/Final_Project_Guide.md` y `Sources/Papers/`.

---

## 🚀 Inicio Rápido

### Vista Previa Local (Quartz)
Requiere Node.js 22+:

```bash
# Instalar dependencias de Node
npm install

# Iniciar servidor local en http://localhost:8080
make site-dev

# Compilar sitio estático en public/
make site-build
```

---

## 📂 Estructura de la Bóveda

```
.
├── Concepts/             # Conceptos atómicos interconectados (Ensambles, Entropía, etc.)
├── Lectures/             # Bitácora cronológica de las 48 sesiones (Sesion_01 a Sesion_48)
├── MoC/                  # Map of Content (Mapa temático del curso)
├── Notebooks/            # Cuadernos interactivos de Google Colab (Python / Julia)
├── Projects/             # Guía del Proyecto Final (40%) y catálogo de artículos
├── Sources/
│   ├── Books/            # Fichas bibliográficas de libros de texto base
│   └── Papers/           # Fichas de los 20 artículos científicos recomendados
├── Syllabus.md           # Programa oficial completo del curso
└── index.md              # Página principal del sitio web
```
