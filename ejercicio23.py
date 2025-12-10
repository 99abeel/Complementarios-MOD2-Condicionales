print("Introduce el año de nacimiento de las tres personas:")

anio_pedro = int(input("Año de Pedro: "))
anio_alicia = int(input("Año de Alicia: "))
anio_carla = int(input("Año de Carla: "))

if anio_pedro == anio_alicia and anio_alicia == anio_carla:
    print("Todos son de la misma quinta.")
elif anio_pedro == anio_alicia:
    print("Pedro y Alicia son de la misma quinta.")
elif anio_pedro == anio_carla:
    print("Pedro y Carla son de la misma quinta.")
elif anio_alicia == anio_carla:
    print("Alicia y Carla son de la misma quinta.")
else:
    print("Ninguno es de la misma quinta.")