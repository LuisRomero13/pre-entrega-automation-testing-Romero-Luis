import pandas as pd

data = {
    'Nombre': ['Ana', 'Juan', 'María', 'Carlos'],
    'Edad': [25, 30, 28, 35],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
}
df = pd.DataFrame(data)

print(df)

# formas de acceder a valores
# Acceder al valor en la fila 1, columna 2
valor = df.iloc[1, 2]
print(f"Valor en fila 1, columna 2: {valor}")  # Output: Barcelona
# Acceder al valor en la fila 0, columna 1
valor = df.iloc[0, 1]
print(f"Valor en fila 0, columna 1: {valor}")  # Output: 25

# Acceder al valor en la fila 2, columna 'Ciudad'
valor = df.loc[2, 'Ciudad']
print(f"Valor en fila 2, columna 'Ciudad': {valor}")  # Output: Sevilla
# Acceder al valor en la fila 0, columna 'Nombre'
valor = df.loc[0, 'Nombre']
print(f"Valor en fila 0, columna 'Nombre': {valor}")  # Output: Ana

# Acceder al valor en la fila 3 de la columna 'Edad'
valor = df['Edad'][3]
print(f"Valor en fila 3 de la columna 'Edad': {valor}")  # Output: 35

# Acceder al valor en la fila 1, columna 'Nombre'
valor = df.at[1, 'Nombre']
print(f"Valor en fila 1, columna 'Nombre': {valor}")  # Output: Juan

# Acceder al valor en la fila 2, columna 1
valor = df.iat[2, 1]
print(f"Valor en fila 2, columna 1: {valor}")  # Output: 28

# Usa iloc cuando quieras acceder por posición numérica.
# Usa loc cuando quieras acceder por etiquetas de fila y nombre de columna.
# at y iat son más rápidos para acceder a un solo valor, pero solo funcionan para un valor a la vez.
# El método de acceso directo (df['columna'][índice]) es intuitivo pero puede ser menos eficiente para operaciones grandes.

# asegúrate de tener instalada la librería openpyxl. Pandas la usa para escribir archivos Excel.
# df.to_excel('mi_archivo.xlsx', sheet_name='Hoja1', index=False, freeze_panes=(1,0))
# sheet_name='Hoja1' nombra la hoja de Excel.
# freeze_panes=(1,0) congela la primera fila (útil para encabezados).

# Si tu DataFrame es muy grande, podrías querer usar el motor 'xlsxwriter' para mejor rendimiento:

# df.to_excel('mi_archivo_grande.xlsx', engine='xlsxwriter')
# Nota: Para usar 'xlsxwriter', primero debes instalarlo con pip install xlsxwriter.

# Si quieres guardar múltiples DataFrames en diferentes hojas del mismo archivo Excel:

# with pd.ExcelWriter('archivo_multiple.xlsx') as writer:
#     df1.to_excel(writer, sheet_name='Hoja1', index=False)
#     df2.to_excel(writer, sheet_name='Hoja2', index=False)
#     df3.to_excel(writer, sheet_name='Hoja3', index=False)