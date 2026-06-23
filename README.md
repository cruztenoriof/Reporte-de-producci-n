# Automatización de Reportes de Producción

## Descripción

Este proyecto fue desarrollado en Python para automatizar el análisis de datos de producción a partir de archivos Excel.

La aplicación permite leer información de producción, calcular indicadores clave (KPIs), generar reportes automáticos y crear visualizaciones para apoyar la toma de decisiones en entornos de manufactura.

---

## Objetivo

Reducir el tiempo dedicado a la elaboración manual de reportes de producción mediante la automatización del procesamiento y análisis de datos.

---

## Funcionalidades

- Lectura de archivos Excel.
- Cálculo de producción total.
- Cálculo de scrap total.
- Cálculo de porcentaje de scrap.
- Análisis de producción por máquina.
- Generación automática de reportes en Excel.
- Creación automática de gráficas de producción.

---

## Tecnologías Utilizadas

- Python
- Pandas
- OpenPyXL
- Matplotlib
- Excel

---

## Estructura del Proyecto

```text
Reporte_produccion_automatizado

├── data
│   └── datos_produccion.xlsx

├── reports
│   └── reporte_produccion.xlsx

├── images
│   └── produccion_por_maquina.png

├── src
│   └── main.py

└── README.md
```

---

## Indicadores Generados

El programa calcula automáticamente:

- Producción Total
- Scrap Total
- Porcentaje de Scrap
- Producción por Máquina

---

## Resultados Obtenidos

### Resumen General

| Indicador | Valor |
|------------|---------:|
| Producción Total | 178,956 |
| Scrap Total | 4,023 |
| Porcentaje de Scrap | 2.25% |

### Producción por Máquina

| Máquina | Producción |
|----------|-----------:|
| M01 | 45,449 |
| M05 | 36,823 |
| M02 | 36,235 |
| M04 | 31,659 |
| M03 | 28,790 |

---

## Visualización

El sistema genera automáticamente una gráfica de barras para comparar la producción acumulada por máquina.

---

## Posibles Mejoras Futuras

- Tendencia de producción mensual.
- Análisis de scrap por máquina.
- Dashboard interactivo con Power BI.
- Generación automática de PDF.
- Envío automático de reportes por correo electrónico.
- Integración con bases de datos SQL.

---

## Aprendizajes del Proyecto

Durante el desarrollo de este proyecto se aplicaron conocimientos de:

- Manipulación de datos con Pandas.
- Lectura y escritura de archivos Excel.
- Automatización de procesos.
- Generación de gráficos con Matplotlib.
- Análisis de indicadores de producción.
- Programación en Python.

---

## Autor

**Francisco Antonio Cruz Tenorio**

Analista de Datos | Python | SQL | Power BI | Excel Avanzado