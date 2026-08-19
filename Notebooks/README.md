# 💻 Laboratorios Computacionales y Notebooks

Esta carpeta contiene los materiales y simulaciones en **Python** y **Julia** para las prácticas numéricas del curso de **Física Estadística (2027-1)**.

Están diseñados para ejecutarse tanto en la nube mediante **Google Colab** (con un solo clic) como en entornos locales (JupyterLab / Notebooks / VS Code).

---

## 🚀 Cuadernos Disponibles y Acceso Directo

| # | Cuaderno / Tema | Descripción | Google Colab |
| :-: | :--- | :--- | :---: |
| **01** | `01_Statistical_Physics_Basics.ipynb` | Introducción a distribuciones continuas (Maxwell-Boltzmann) y simulaciones Monte Carlo básicas. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/razamoraz/FIsicaESTAdistica_2027_1/blob/main/Notebooks/Python/01_Statistical_Physics_Basics.ipynb) |
| **02** | `02_Camino_Aleatorio_1D_Reif.ipynb` | **Camino Aleatorio 1D, Momentos y Límite Gaussiano**: Deducción combinatoria exacta, simulación vectorial de ensamble, truco de diferenciación de Reif y aproximación continua para $N \gg 1$ (*Reif Cap. 1, Secs. 1.2–1.5*). | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/razamoraz/FIsicaESTAdistica_2027_1/blob/main/Notebooks/Python/02_Camino_Aleatorio_1D_Reif.ipynb) |

---

## 🛠️ Configuración y Ejecución en Local (usando `make`)

Para reproducir y ejecutar los cuadernos en tu computadora con todas las dependencias científicas (`numpy`, `scipy`, `matplotlib`, `jupyter`), sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone https://github.com/razamoraz/FIsicaESTAdistica_2027_1.git
cd FIsicaESTAdistica_2027_1
```

### 2. Configurar el entorno virtual con `make setup`
Ejecuta el siguiente comando en la terminal:
```bash
make setup
```
Este comando automáticamente:
- Crea un entorno virtual aislado en `.venv`.
- Actualiza `pip` e instala todas las dependencias científicas requeridas especificadas en `requirements.txt`.
- Inicializa el archivo `.env` de configuración si no existe.

### 3. Iniciar Jupyter
Para abrir la interfaz interactiva en tu navegador:
```bash
# Para iniciar Jupyter Notebook clásico:
make jupyter

# O para iniciar JupyterLab:
make lab
```

### 4. Validar la ejecución de todos los cuadernos
Puedes verificar que todos los cuadernos de Python se ejecuten correctamente sin errores con:
```bash
make test-notebooks
```

### 5. Uso manual alternativo (sin `make`)
Si prefieres activar el entorno virtual directamente:
```bash
source .venv/bin/activate
jupyter notebook Notebooks/
```
Para desactivar el entorno al terminar:
```bash
deactivate
```
