# Datos
cursos = [8, 2.5, 4]
print(dir(cursos))
cursos.sort()
print(cursos)
miCurso = 1.5

# Punto A
porc1 = miCurso * 100 / cursos[0]
dif1 = 100 - porc1
print(
    f"La diferencia en porcentaje entre este curso y el mas rapido de los otros cursos es {dif1}%")

porc2 = miCurso * 100 / cursos[1]
dif2 = 100 - porc2
print(
    f"La diferencia en porcentaje entre este curso y el promedio de los otros cursos es {dif2}%")

porc3 = miCurso * 100 / cursos[2]
dif3 = 100 - porc3
print(
    f"La diferencia en porcentaje entre este curso y el promedio de los otros cursos es {dif3}%")

# Punto B
crudo = [3.5, 5]
porc4 = cursos[1] * 100 / crudo[1]
dif4 = 100 - porc4
print(
    f"El porcentaje de material inservible entre el promedio de los cursos y y el crudo es {dif4}%")
porc2
porc5 = miCurso * 100 / crudo[0]
dif5 = 100 - porc5
print(
    f"El porcentaje de material inservible entre el el curso actual y y el crudo es {dif5}%")
print(
    f"El porcentaje de material inservible entre el el curso actual y y el crudo es {int(dif5)}%")

# Punto C
# Si:
# 1,5hs     4hs
# 10hs      ?
equi1 = 10 * cursos[1] / miCurso
print(f"Ver 10 horas de este curso equivale a {equi1}hs de otros cursos")
print(f"Ver 10 horas de este curso equivale a {int(equi1)}hs de otros cursos")
# Y al reves:
# 1,5hs     4hs
# ?         10hs
equi2 = 10 * miCurso / cursos[1]
print(f"Ver 10 horas de otros cursos equivale a {equi2}hs de este curso")

