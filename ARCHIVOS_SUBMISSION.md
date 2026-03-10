# Análisis de Archivos para Submisión de Tarea

## 📋 Estado Actual del Repositorio

### Archivos Existentes

| Archivo/Carpeta | Tamaño | Estado Git | ¿Incluir? | Razón |
|----------------|--------|-----------|-----------|-------|
| `notebooks_TareaModelo.ipynb` | - | Modificado | ✅ **SÍ** | **REQUERIDO** - Notebook principal con todo el análisis |
| `TareaModelo.html` | - | No rastreado | ✅ **SÍ** | **REQUERIDO** - Versión HTML exportada del notebook |
| `INSTRUCCIONES_CCMC.md` | - | No rastreado | ✅ **SÍ** | Documentación útil para referencia |
| `JUSTIFICACION_EVENTO_MARZO_2012.md` | - | No rastreado | ✅ **SÍ** | Justificación detallada de selección del evento |
| `hapienv/` | 12 MB | No rastreado | ❌ **NO** | Entorno virtual - se regenera con pip install |
| `.venv/` | 448 MB | No rastreado | ❌ **NO** | Entorno virtual - se regenera con pip install |
| `hapicache/` | 848 KB | No rastreado | ⚠️ **OPCIONAL** | Caché de datos HAPI - puede regenerarse |
| `.ipynb_checkpoints/` | - | Ignorado | ❌ **NO** | Archivos temporales de Jupyter |
| `.DS_Store` | - | Ignorado | ❌ **NO** | Archivo del sistema macOS |
| `.git/` | - | Sistema | ✅ **SÍ** | Directorio de control de versiones Git |
| `.gitignore` | - | Rastreado | ✅ **SÍ** | Configuración de Git |

---

## ❗ ARCHIVOS FALTANTES (CRÍTICOS)

Según los requisitos, **FALTAN** los siguientes archivos de modelos CCMC:

### 1. Resultados del Modelo CORHEL-CME
**Fecha del modelo**: 7 marzo 2012, 00:24:06 UTC

- [ ] `CORHEL_CME_20120307_config.txt` - Configuración del run
- [ ] `CORHEL_CME_20120307_propagation.png` - Gráfico de propagación
- [ ] `CORHEL_CME_20120307_arrival.png` - Predicción de llegada
- [ ] `CORHEL_CME_20120307_results.dat` - Datos numéricos (opcional)

### 2. Resultados del Modelo Tsyganenko TS05
**Fecha del modelo**: 10 marzo 2012

- [ ] `TS05_magnetosphere_20120310_config.txt` - Configuración
- [ ] `TS05_magnetosphere_20120310_fieldlines.png` - Líneas de campo
- [ ] `TS05_magnetosphere_20120310_overview.png` - Vista general
- [ ] `TS05_magnetosphere_20120310_parameters.txt` - Parámetros de entrada

### 3. Resultados del Modelo IRI-2020
**Fecha del modelo**: 10 marzo 2012

- [ ] `IRI2020_ionosphere_20120310_config.txt` - Configuración
- [ ] `IRI2020_ionosphere_20120310_profiles.png` - Perfiles de densidad
- [ ] `IRI2020_ionosphere_20120310_TEC.png` - Contenido total de electrones
- [ ] `IRI2020_ionosphere_20120310_data.dat` - Datos numéricos (opcional)

### 4. Resultados de Trayectorias de Rayos Cósmicos
**Fecha del modelo**: 10 marzo 2012

- [ ] `cosmic_ray_20120310_config.txt` - Configuración T05+IGRF
- [ ] `cosmic_ray_20120310_trajectories.png` - Gráficos de trayectorias
- [ ] `cosmic_ray_20120310_cutoff.png` - Rigidez de corte
- [ ] `cosmic_ray_20120310_data.dat` - Datos numéricos (opcional)

---

## 🎯 PLAN DE ACCIÓN PARA COMPLETAR LA TAREA

### Paso 1: Solicitar Modelos en CCMC

1. **CORHEL-CME**: https://ccmc.gsfc.nasa.gov/models/CORHEL-CME~1/
   - Fecha: 2012-03-07, Hora: 00:24:06 UTC
   - Velocidad: 2684 km/s o 2379 km/s
   - PA: 57°, Ancho: 360°

2. **Tsyganenko TS05**: https://ccmc.gsfc.nasa.gov/models/Tsyganenko%20Magnetic%20Field~TS05/
   - Fecha: 2012-03-10
   - Los parámetros se obtienen automáticamente de OMNI

3. **IRI-2020**: https://ccmc.gsfc.nasa.gov/models/IRI~2020/
   - Fecha: 2012-03-10
   - Seleccionar ubicación de interés

4. **Rayos Cósmicos**: https://cor.crmodels.org/geo-mag/
   - Fecha: 2012-03-10
   - Modelo: T05 + IGRF

### Paso 2: Descargar Resultados

Cuando reciba los emails con los resultados:
- Descargar TODOS los archivos (gráficos, datos, configuración)
- Guardarlos en la raíz del proyecto con nombres descriptivos

### Paso 3: Actualizar .gitignore

```bash
# Actualizar .gitignore para excluir archivos grandes innecesarios
echo "hapienv/" >> .gitignore
echo ".venv/" >> .gitignore
echo "hapicache/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
```

### Paso 4: Actualizar el Notebook

En la sección "Resultados de Modelos CCMC", descomente y actualice:

```python
from IPython.display import Image, display

# CORHEL-CME
display(Image(filename='CORHEL_CME_20120307_propagation.png'))

# TS05
display(Image(filename='TS05_magnetosphere_20120310_fieldlines.png'))

# IRI-2020
display(Image(filename='IRI2020_ionosphere_20120310_profiles.png'))

# Rayos Cósmicos
display(Image(filename='cosmic_ray_20120310_trajectories.png'))
```

### Paso 5: Verificar TareaModelo.html

El archivo HTML ya existe, pero debe ser **regenerado** después de:
1. Ejecutar todas las celdas del notebook
2. Incluir las imágenes de CCMC
3. Completar las interpretaciones

Para regenerar:
- En Jupyter Lab: File → Export Notebook As → HTML
- O desde terminal: `jupyter nbconvert --to html notebooks_TareaModelo.ipynb --output TareaModelo.html`

### Paso 6: Commit y Push

```bash
# Actualizar .gitignore
git add .gitignore

# Agregar archivos del notebook
git add notebooks_TareaModelo.ipynb
git add TareaModelo.html

# Agregar documentación
git add INSTRUCCIONES_CCMC.md
git add JUSTIFICACION_EVENTO_MARZO_2012.md
git add ARCHIVOS_SUBMISSION.md

# Agregar resultados de CCMC (cuando estén disponibles)
git add CORHEL_*.png CORHEL_*.txt
git add TS05_*.png TS05_*.txt
git add IRI2020_*.png IRI2020_*.txt
git add cosmic_ray_*.png cosmic_ray_*.txt

# Commit
git commit -m "Tarea completa: Análisis clima espacial marzo 2012 con resultados CCMC"

# Push
git push origin main
```

---

## ✅ CHECKLIST FINAL ANTES DE SUBMISIÓN

### Archivos Obligatorios
- [ ] `notebooks_TareaModelo.ipynb` - Notebook completo y ejecutado
- [ ] `TareaModelo.html` - Exportado después de ejecutar todo

### Resultados de Modelos (CRÍTICO)
- [ ] Archivos de CORHEL-CME (al menos 1 imagen + config)
- [ ] Archivos de Tsyganenko TS05 (al menos 1 imagen + config)
- [ ] Archivos de IRI-2020 (al menos 1 imagen + config)
- [ ] Archivos de Rayos Cósmicos (al menos 1 imagen + config)

### Documentación (Recomendada)
- [ ] `JUSTIFICACION_EVENTO_MARZO_2012.md` - Justificación de selección
- [ ] `INSTRUCCIONES_CCMC.md` - Guía de uso
- [ ] `.gitignore` actualizado

### Contenido del Notebook
- [ ] Metodología completa con tabla de CMEs
- [ ] Todas las celdas ejecutadas sin errores
- [ ] Gráficos de datos HAPI generados
- [ ] Imágenes de CCMC incluidas
- [ ] Sección de Resultados con interpretaciones
- [ ] Sección de Conclusiones completada
- [ ] Referencias a los modelos CCMC

### Verificación Final
- [ ] El notebook se ejecuta completamente sin errores
- [ ] Todas las imágenes se visualizan correctamente
- [ ] El archivo HTML muestra todo el contenido
- [ ] El repositorio está sincronizado con GitLab
- [ ] No se incluyeron entornos virtuales (hapienv/, .venv/)

---

## 🚫 ARCHIVOS QUE NO DEBEN INCLUIRSE

| Archivo/Carpeta | Razón para Excluir |
|----------------|-------------------|
| `hapienv/` | Entorno virtual (12 MB) - se regenera con requirements.txt |
| `.venv/` | Entorno virtual (448 MB) - se regenera con requirements.txt |
| `hapicache/` | Caché temporal (848 KB) - se regenera al ejecutar el notebook |
| `.ipynb_checkpoints/` | Archivos temporales de Jupyter |
| `.DS_Store` | Archivo del sistema macOS |
| `__pycache__/` | Caché de Python |
| `*.pyc` | Archivos compilados de Python |

---

## 📊 RESUMEN

### Estado Actual: ⚠️ INCOMPLETO

**Archivos presentes**: 3/7 requeridos (43%)
- ✅ Notebook (modificado, no committeado)
- ✅ HTML (debe regenerarse)
- ❌ Resultados CCMC (0/4 modelos)

### Próximos Pasos Inmediatos:

1. **URGENTE**: Solicitar los 4 modelos en CCMC
2. Actualizar `.gitignore` para excluir entornos virtuales
3. Esperar resultados de CCMC (pueden tardar horas/días)
4. Agregar imágenes al notebook
5. Ejecutar todo el notebook
6. Exportar nuevo HTML
7. Commit y push todo al repositorio

### Estimación de Tiempo:
- Solicitudes CCMC: 30-60 minutos
- Espera de resultados: 1-48 horas (depende de la carga del servidor)
- Integración al notebook: 30-60 minutos
- Revisión final: 30 minutos

**Total**: 2-3 horas de trabajo activo + tiempo de espera de CCMC

---

## 💡 RECOMENDACIÓN

**No submita la tarea hasta tener los resultados de CCMC**, ya que son un requisito explícito según las instrucciones:

> "Además del notebook, deberá subir al GitLab los resultados de los 'Run-on-request' o 'Instant Run' de los siguientes modelos..."

Sin estos archivos, la tarea está **incompleta**.
