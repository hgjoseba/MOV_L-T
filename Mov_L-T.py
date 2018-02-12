#Movimiento Lunar           *
#****************************

#Librerias
from math import sqrt as raiz
from tabulate import tabulate

#Despreciamos posicion_tierra ya que es (0.00,0.00)
def calcular_distancia(posicion_luna):
    return raiz (posicion_luna[0] ** 2 + posicion_luna[1] ** 2)


def calcular_fuerza_gravitatoria(posicion_luna, d, masa_luna, masa_tierra, g_const):
    fuerza_x =  - (g_const * masa_luna * masa_tierra * posicion_luna[0]) / d ** 3
    fuerza_y =  - (g_const * masa_luna * masa_tierra * posicion_luna[1]) / d ** 3

    return (fuerza_x, fuerza_y)


def calcular_aceleracion(fuerza, masa_luna):
    aceleracion_x = fuerza[0] / masa_luna
    aceleracion_y = fuerza[1] / masa_luna

    return (aceleracion_x, aceleracion_y)


def calcular_var_velocidad(ts, a):
    var_vx =  a[0] * ts
    var_vy =  a[1] * ts

    return (var_vx, var_vy)

def calcular_velocidad(var_v, vi):
    vx  = var_v[0] + vi[0]
    vy = var_v[1] + vi[1]

    return (vx,vy)


def calcular_posicion(posicion_luna, v, ts):
    px = posicion_luna[0] + v[0] * ts
    py = posicion_luna[1] + v[1] * ts

    return (px, py)


#Entrada robusta para tiempo simulacion
def leer_opcion_td():
    while True:
        try:
            td = int(input("\nIntroduce el tiempo total de la simulacion (d): "))
            break
        except ValueError:
            print("Error, Prueba otra vez")
    return td

#Entrada robusta para incremento paso tiempo
def leer_opcion_ts():
    while True:
        try:
            ts = float(input("Introduce el incremento en cada paso del tiempo (s): "))
            break
        except ValueError:
            print("Error, Prueba otra vez")
    return ts


#PROGRAMA PRINCIPAL
def main():
    #DATOS "despreciamos posicion_tierra ya que es (0.00,0.00)"
    posicion_luna = (0.0, 384402 * 10 ** 3)
    masa_luna = 7.348 * 10 ** 22
    masa_tierra = 5.9722 * 10 ** 24
    g_const = 6.674 * 10 ** -11
    vi = (1023.055, 0.0)

    #INCREMENTO DE TIEMPO
    td = leer_opcion_td()
    ts = leer_opcion_ts()

    #DATOS INICIALES (partida)
    distancia = calcular_distancia(posicion_luna)
    fuerza = calcular_fuerza_gravitatoria(posicion_luna, distancia, masa_luna, masa_tierra, g_const)

    lista_tabla = []

    fuerza_x = fuerza[0]
    fuerza_y = fuerza[1]
    fuerza_dato = "(%.5e, %.5e)" % (fuerza[0], fuerza[1])
    posicion_x_luna = posicion_luna[0]
    posicion_y_luna = posicion_luna[1]
    posicion_luna_dato = "(%.5e, %.5e)" % (posicion_x_luna, posicion_y_luna)
    distancia = "%.4e" % distancia

    incremento_paso = 0
    dia = 0

    lista_tabla.append((incremento_paso, dia, fuerza_dato, posicion_luna_dato, distancia))#añadimos a la lista los datos a sacar por tabla

    while incremento_paso <= td * 86400:

        distancia = calcular_distancia(posicion_luna)
        fuerza = calcular_fuerza_gravitatoria(posicion_luna, distancia, masa_luna, masa_tierra, g_const)
        aceleracion = calcular_aceleracion(fuerza, masa_luna)
        var_velocidad = calcular_var_velocidad(ts, aceleracion)
        velocidad = calcular_velocidad(var_velocidad, vi)
        posicion_luna = calcular_posicion(posicion_luna, velocidad, ts)#actualizacion posicion, "nueva" posicion_luna
        vi = velocidad #actualizacion velocidad, vi --> Vn+1

        if incremento_paso % 86400 == 0 and incremento_paso != 0:
            dia = incremento_paso / 86400

            fuerza_x = fuerza[0]
            fuerza_y = fuerza[1]
            fuerza_dato = "(%.5e, %.5e)" % (fuerza[0], fuerza[1])#descomposicion tupla para printear con 5 decimales
            posicion_x_luna = posicion_luna[0]
            posicion_y_luna = posicion_luna[1]
            posicion_luna_dato = "(%.5e, %.5e)" % (posicion_x_luna, posicion_y_luna)
            distancia = "%.4e" % distancia

            lista_tabla.append((incremento_paso, dia, fuerza_dato, posicion_luna_dato, distancia))#añadimos a la lista los datos a sacar por tabla

        incremento_paso += 1

    print("\n")
    print(tabulate(lista_tabla, headers=["T(s)", "T(d)", "F(N)", "(x,y)(m)","R(m)"]))


if __name__ == "__main__":
    main()
