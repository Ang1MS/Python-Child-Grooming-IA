# Detección de Child Grooming con Inteligencia Artificial

Este proyecto forma parte de un Trabajo de Fin de Máster (TFM) centrado en la detección de **child grooming** a través de técnicas de procesamiento del lenguaje natural (NLP) y aprendizaje automático, incluyendo modelos como Naïve Bayes, SVM, Random Forest y BERT.

---

## Estructura del proyecto

- `DataSets/` 
  Carpeta donde deben colocarse manualmente los datasets PAN12 descargados:
  - `pan12-sexual-predator-identification-training-corpus-2012-05-01.xml`
  - `pan12-sexual-predator-identification-test-corpus-2012-05-17.xml`


- `CargarDataSet.py`   
  Script para convertir los archivos XML en CSV.

- `Modelo_IA.ipynb` 
  Notebook para entrenar los modelos clásicos: Naïve Bayes, SVM y Random Forest.

- `Modelo_IA_BERT.ipynb`  
  Notebook para entrenar el modelo basado en la arquitectura BERT.

- `requirements.txt` 
  Lista de dependencias necesarias para ejecutar el proyecto.

- `README.md` 
  Documentación del proyecto.

---

## Requisitos

- Python 3.8+
- Jupyter Notebook

---

## Instrucciones

### 1. Descargar el Dataset PAN12

- Visita: [https://pan.webis.de/clef12/pan12-web/sexual-predator-identification.html](https://pan.webis.de/clef12/pan12-web/sexual-predator-identification.html)
- Descarga los archivos XML correspondientes al corpus de entrenamiento y prueba.
- Crea una carpeta en la raíz del proyecto llamada `DataSets/` y colócalos dentro.

### 2. Convertir los XML a CSV

Ejecuta el script `CargarDataSet.py` para transformar los archivos XML en CSV:

```bash
python CargarDataSet.py
```

### 3. Entrenar modelos clásicos

Abre el notebook `Modelo_IA.ipynb` y ejecútalo para entrenar los siguientes modelos:

- Naïve Bayes  
- Support Vector Machine (SVM)  
- Random Forest  

---

### 4. Entrenar modelo BERT

Abre el notebook `Modelo_IA_BERT.ipynb` para entrenar el modelo basado en la arquitectura **BERT**. 
(ATENCIÓN: Requiere de haber ejecutado previamente `Modelo_IA.ipynb`)

---

> ⚠️ **Nota importante**  
> Debido a las restricciones de tamaño de archivos en GitHub, **los datasets PAN12 no están incluidos en este repositorio**.  
> Es  necesario descargarlos manualmente y colocarlos en la carpeta `DataSets`.

---

## Créditos
Este proyecto ha sido desarrollado como parte de un **Trabajo de Fin de Máster (TFM)** sobre la detección automatizada de *child grooming* mediante el uso de **inteligencia artificial**.

