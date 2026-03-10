# Instrucciones para Completar la Tarea Modelo

## Evento Seleccionado: 5-8 Marzo 2012

### Datos del Evento Principal
- **Fecha de la CME**: 7 de marzo de 2012, 00:24:06 UTC
- **Velocidad lineal**: 2684 km/s
- **Velocidad final**: 2379 km/s
- **Energía cinética**: 5.0×10³² erg
- **Tipo**: Halo completo (360°)
- **Ángulo de posición**: 57°

---

## Pasos a Seguir

### 1. Solicitar Modelos en CCMC

#### A. Modelo CORHEL-CME
- **URL**: https://ccmc.gsfc.nasa.gov/models/CORHEL-CME~1/
- **Fecha**: 2012-03-07
- **Hora**: 00:24:06 UTC
- **Parámetros sugeridos**:
  - Velocidad inicial: 2684 km/s o 2379 km/s (velocidad final)
  - Ángulo de posición: 57°
  - Ancho angular: 360° (halo)

#### B. Modelo Tsyganenko TS05
- **URL**: https://ccmc.gsfc.nasa.gov/models/Tsyganenko%20Magnetic%20Field~TS05/
- **Fecha**: 2012-03-10 (3 días después de la CME)
- **Hora**: Seleccionar el momento de mínimo Dst (consultar gráfico en el notebook)
- **Parámetros**: Se obtienen automáticamente de bases de datos (OMNI)

#### C. Modelo IRI-2020
- **URL**: https://ccmc.gsfc.nasa.gov/models/IRI~2020/
- **Fecha**: 2012-03-10
- **Hora**: Mismo que TS05
- **Ubicación**: Seleccionar coordenadas de interés (ej: observatorio local)

#### D. Trayectorias de Rayos Cósmicos
- **URL**: https://cor.crmodels.org/geo-mag/
- **Modelo magnético**: Tsyganenko T05 + IGRF
- **Fecha**: 2012-03-10
- **Parámetros**: Partículas de diferentes energías/rigideces

---

### 2. Descargar Resultados

Cuando reciba los resultados por correo:
1. Descargue todos los archivos (gráficos, datos, configuración)
2. Guárdelos en la carpeta del proyecto con nombres descriptivos:
   - `CORHEL_CME_20120307_*.png`
   - `TS05_magnetosphere_20120310_*.png`
   - `IRI2020_ionosphere_20120310_*.png`
   - `cosmic_ray_trajectories_20120310_*.png`

---

### 3. Actualizar el Notebook

1. Abra el notebook
2. Localice la sección "Resultados de Modelos CCMC"
3. Descomente y actualice las líneas de código para cargar imágenes:
   ```python
   from IPython.display import Image, display
   display(Image(filename='CORHEL_CME_20120307_results.png'))
   display(Image(filename='TS05_magnetosphere_20120310_results.png'))
   display(Image(filename='IRI2020_ionosphere_20120310_results.png'))
   display(Image(filename='cosmic_ray_trajectories_20120310_results.png'))
   ```

---

### 4. Completar el Análisis

1. Ejecute todas las celdas del notebook
2. Revise los gráficos generados y complete la interpretación en la sección "Análisis de Resultados"
3. Actualice la sección de "Conclusiones" con sus observaciones específicas:
   - Valor mínimo de Dst alcanzado
   - Clasificación de la tormenta
   - Tiempo de llegada observado
   - Efectos en magnetómetros e ionosfera

---

### 5. Exportar y Subir

1. **Exportar a HTML**:
   - En Jupyter: File → Export Notebook As → HTML
   - Guardar como `TareaModelo.html`

2. **Subir a GitLab**:
   ```bash
   git add notebooks_TareaModelo.ipynb
   git add TareaModelo.html
   git add CORHEL_*.png
   git add TS05_*.png
   git add IRI2020_*.png
   git add cosmic_ray_*.png
   git add *.txt  # archivos de configuración
   git commit -m "Tarea completa: Análisis evento clima espacial marzo 2012"
   git push origin main
   ```

---

## Recursos Adicionales

### Datos del Evento
- **CDAW CME Catalog**: https://cdaw.gsfc.nasa.gov/CME_list/halo/halo.html
- **Índices Kp**: https://solen.info/solar/old_reports/
- **NOAA Space Weather Archive**: https://www.swpc.noaa.gov/products/solar-and-geophysical-activity-summary

### Documentación
- **HAPI Client**: https://github.com/hapi-server/client-python
- **CCMC Models**: https://ccmc.gsfc.nasa.gov/models/modelinfo.php

---

## Soporte

Si encuentra problemas con:
- **Solicitudes CCMC**: Consulte la documentación de ayuda en cada página del modelo
- **HAPI Client**: Revise los ejemplos en https://github.com/hapi-server/client-python/tree/master/examples
- **Análisis de datos**: Consulte la literatura sobre el evento de marzo 2012 (fue un evento mayor ampliamente estudiado)

---

**¡Buena suerte con su análisis! 🌟**
