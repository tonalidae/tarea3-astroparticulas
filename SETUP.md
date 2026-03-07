# Requisitos del Proyecto - Tarea Clima Espacial

## Paquetes de Python Necesarios

Para recrear el entorno virtual, use:

```bash
# Crear entorno virtual
python -m venv .venv

# Activar (macOS/Linux)
source .venv/bin/activate

# Activar (Windows)
.venv\Scripts\Activate

# Instalar paquetes
pip install --upgrade pip
pip install --upgrade hapiclient hapiplot
pip install --upgrade pytz
pip install --upgrade enlilviz
pip install --upgrade jupyterlab
pip install --upgrade pandas
pip install --upgrade matplotlib
pip install --upgrade numpy
```

## O usando requirements.txt

```bash
pip install -r requirements.txt
```

## Versiones Recomendadas

- Python: 3.8+
- hapiclient: última versión
- hapiplot: última versión
- jupyterlab: 3.x o 4.x
- pandas: última versión
- matplotlib: última versión
- numpy: última versión
- enlilviz: última versión
- pytz: última versión

## Notas

- Los entornos virtuales (hapienv/, .venv/) NO deben incluirse en el repositorio
- Use este archivo para recrear el entorno en cualquier máquina
- La carpeta hapicache/ contiene datos descargados y se regenera automáticamente
