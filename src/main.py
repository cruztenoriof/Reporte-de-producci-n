import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("../data/datos_produccion.xlsx")

print("\nDATOS DE PRODUCCIÓN")
print(df)

# Calcular indicadores

produccion_total = df["Producción"].sum()
scrap_total = df["Scrap"].sum()

porcentaje_scrap = (scrap_total / produccion_total) * 100

print("\nRESUMEN")
print(f"Producción Total: {produccion_total}")
print(f"Scrap Total: {scrap_total}")
print(f"Porcentaje Scrap: {porcentaje_scrap:.2f}%")

# ==========================
# CREAR REPORTE EN EXCEL
# ==========================

resumen = pd.DataFrame({
    "Indicador": [
        "Producción Total",
        "Scrap Total",
        "Porcentaje Scrap"
    ],
    "Valor": [
        produccion_total,
        scrap_total,
        round(porcentaje_scrap, 2)
    ]
})

resumen.to_excel(
    "../reportes/reporte_produccion.xlsx",
    index=False
)

print("\nReporte generado correctamente.")
produccion_por_maquina = (
    df.groupby("Máquina")["Producción"]
    .sum()
    .reset_index()
    .sort_values("Producción", ascending=False)
)

print("\nPRODUCCIÓN POR MÁQUINA")
print(produccion_por_maquina)
# Crear carpeta images si no existe
import os
os.makedirs("../images", exist_ok=True)

# Crear gráfica
plt.figure(figsize=(8,5))

plt.bar(
    produccion_por_maquina["Máquina"],
    produccion_por_maquina["Producción"]
)

plt.title("Producción por Máquina")
plt.xlabel("Máquina")
plt.ylabel("Producción")

plt.tight_layout()

# Guardar imagen
plt.savefig("../images/produccion_por_maquina.png")

print("\nGráfica generada correctamente.")