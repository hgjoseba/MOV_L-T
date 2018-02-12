# MOV_L-T
Movimiento Luna-Tierra

El funcionamiento general del programa es el siguiente:

• Se calcula la fuerza gravitatoria total a la que se encuentra sometido el cuerpo, en este caso la Luna, debido al resto de cuerpos conocidos por el programa. En este momento únicamente se va a realizar el cálculo con la Tierra, pero el programa se generalizará más adelante para calcular la fuerza total que sobre un determinado cuerpo producen otros N cuerpos.

• Para calcular la fuerza sobre un cuerpo necesitamos saber la posición del mismo (X, Y), así como la del resto de cuerpos que le afectan (en este ejemplo solamente uno, la Tierra) y sus masas. A partir de las posiciones en cada paso de tiempo calculamos las distancias entre un par de cuerpos y podemos obtener la fuerza que le afecta a dicho cuerpo. En el ejemplo actual no es necesario calcular la fuerza sobre la Tierra, únicamente la fuerza que esta última ejerce sobre la Luna en cada instante.

• Cuando sabemos la fuerza que en la posición actual está ejerciendo la Tierra sobre la Luna, procedemos a calcular la nueva posición que tendrá la Luna al estar sometida a esa fuerza. Para ello suponemos que la fuerza no cambia durante el intervalo considerado (por ejemplo, un intervalo de un segundo), a pesar de que en la realidad en cada instante infinitesimal la Luna se mueve y se ve afectada por una fuerza ligeramente distinta que en el instante anterior. Sin embargo, el cálculo que vamos a realizar nosotros utiliza una fuerza constante para mover el cuerpo durante el incremento de tiempo determinado.

◦ Calculada la fuerza sobre la Luna debida a otros cuerpos (uno en este caso), podemos calcular la aceleración a la que está sometida (m es la masa de la Luna y F la fuerza a la que está sometida en la posición actual): ⃗a = ⃗F m

◦ A partir de la aceleración en el intervalo considerado, calculamos el cambio de velocidad que la fuerza anterior produce sobre la luna. En este caso t es el tiempo que transcurre en el intervalo considerado (por ejemplo un segundo): Δ v⃗ = a⃗ ⋅ t

◦ Con el cambio de velocidad calculado podemos saber la nueva velocidad de la Luna ⃗v i + 1 = v⃗ i + Δ v⃗

◦ Una vez obtenida la velocidad de la Luna, calculamos su nueva posición al finalizar el intervalo de tiempo actual. s i + 1 = s i + ⃗v i + i ⋅ t

• Este proceso se repite paso a paso hasta el número de pasos determinado. A partir de la descripción anterior, de la investigación realizada por cada grupo, y de las consultas que se realicen al profesor, cada grupo debe implementar un programa que calcule e imprima en cada instante la fuerza a la que se encuentra sometida la Luna así como su posición. El programa debe pedir al usuario los siguientes datos:

• Número de días a simular. El programa internamente trabaja en segundos, por lo que habrá que convertir el dato introducido por el usuario.

• Incremento de tiempo producido en cada paso. En el ejemplo se utiliza un segundo de incremento entre cada paso. Aunque este tiempo puede hacerse mayor para reducir el número de cálculos, el resultado será menos preciso, y las órbitas se irán separando de las reales en mayor medida.

Para evitar que la lista impresa sea muy grande, el programa únicamente imprime los datos de la órbita de la Luna una vez por día (cada 86400 s), aunque internamente sigue haciendo cálculos teniendo en cuenta el incremento de tiempo considerado (un segundo en el caso del ejemplo).

La salida del programa debe ir escribiendo una tabla similar al ejemplo que al final de este documento. Hay que tener en cuenta que tanto la fuerza, como la velocidad y la posición son vectores. La última columna de la tabla debe imprimir la distancia de la Luna a la tierra en el paso de tiempo considerado.

Al introducir los datos del ejemplo se puede comprobar que la Luna vuelve a su posición inicial aproximadamente entre los días 27-28, lo que se corresponde con la realidad a pesar del error cometido en la aproximación.

Los datos utilizados en la simulación para la Tierra y la Luna son: • Tierra: m=5.9722e24Kg;(X,Y)=(0.0,0.0)m;(Vx,Vy)=(0.0,0.0)m/s • Luna: m=7.348e22Kg;(X,Y)=(0.0,384402e3)m;(Vx,Vy)=(1023.055,0.0)m/s
