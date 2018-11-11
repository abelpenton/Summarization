# History Summarization

- Manuel Mauricio Martínez Ordoqui
- Jose Carlos Arenas Sanchéz
- Abel Pentón Ibrahim

    C511

## Run
`>python sol.py`

## Test

En la carpeta `examples` tenemos 3 historias a las cuales se les aplicó el algoritmo, si se desea añadir algun otro ejemplo copie a esta carpeta su archivo y dentro de  ``sol.py`` cambiar la linea donde se carga el archivo (107) por el nombre del nuevo documento a analizar.

## How Work

Una de las tantas aplicaciones del algortimo TextRank es la extracción de oraciones para automatizar el proceso de Summarization. Para aplicar el TextRank con el objetivo de hacer Summarization se llevamos a cabo una serie de pasos, primero que todo construimos un grafo asociado al texto, donde los nodos de este representan las oraciones del texto y las aristas del grafo cuentan con un peso que no es más que una función de similaridad entre las oraciones que conecta una arista dada. Esta relación la vamos a establecer a partir del número de tokens entre la representación lexica de ambas oraciones. Formalmenete dado $S_{i}$ y $S_{j}$ 2 oraciones donde $N_{i}$ representa las palabras que aparecen en $S_{i}$ = $w_{1}$, $w_{2}$, ..., $w_{N_{i}}$ la similaridad entre estas 2 oraciones esta dada por:


$S(S_{i}, S_{j})$ = $\frac { | \{w_{k} | w_{k} \in S_{i} \& \ w_{k} \in S_{i}  \}| } {log(|S_{i}|) + log(|S_{j}|)}$


Usando esta función de similaridad una véz construido el grafo vamos a poner como peso a las aristas esta función para todo par de oraciones en el texto. De esta forma tenemos dado un texto un grafo de pesos y a partir de aqui vamos a aplicar el ranking TextRank para establecer un score a las oraciones luego estas seran ordenadas en función de este valor y finalmente se seleccionan una cantidad definida de oraciones del resultado de esta ordenación para representar el resumen.

## Pipeline

1 Tokenizar un texto dado en oraciones aplicando filtros y lemmatization.

2 Construir un grafo a partir del texto, donde los nodos son las oraciones del mismo y el peso en las aristas la función de Similaridad explicada anteriormente.

3 Calcular el score de cada oración usando el algoritmo de TextRank.

4 Ordenar las oraciones por el score y extraer una `x` cantidad definida por el `radio`.

5 Finalmente de las oraciones seleccionadas por el score vamos ordenarlas por el indice de aparición en el texto original con el objetivo de establecer un orden lógico en el resultado final.

## TextRank

Dado un grafo con un conjunto de nodos `V` y un conjunto de aristas `E` donde `G = (V,E)`. Se define como score de un nodo $V_{i}$:

$S(V_{i})$ = $(1-d) + d * \sum_{j \in In(V_{i})}{\frac {1}{|Out(V_{j})|} S(V_{j})}$

donde $In(V_{i})$ es el conjunto de nodos que entran al nodo $V_{i}$ así como $Out(V_{i})$ el conjunto de nodos que salen de $V_{i}$. $d$ es conocido como damping que toma valores entre $[0,1]$ usalmente $0.85$ que representa una probabilidad de un salto aleatorio a otro nodo $[3]$.

El algoritmo original de PageRank asume que los grafos son sin peso en las aristas como se usa en el problema de hacer ranking en las páginas web usando sus links a otras. Sin embargo en el caso del procesamiento del lenguaje natural en textos, las entidades tienen multiples relaciones entre ellas, causa por la cual se representan con grafos de pesos. Teniendo en cuenta esto la formula para calcular el score sufre modificaciones.


$WS(V_{i})$ = $(1-d) + d * \sum_{j \in In(V_{i})}{\frac {w_{ji}}{\sum_{V_{k} \in Out(V_{j})} w_{jk}} WS(V_{j})}$

donde $w_{ij}$ representa la función de similaridad entre las entidades $i$ y $j$.

Con este algoritmo de ranking podemos a cada oracion en nuestro texto asignarle un `score` el cual es el que se utilizará para hacer una selección de las oraciones más importante dentro del texto original. Una de sus principales ventajas es que es un algoritmo completamente no supervisado y los métodos de extracción no necesitan entrenamiento ni conjuntos de datos testeados.

## Referencia

1 TextRank: Bringing Order into Texts. Department of Computer Science University of North Texas.

2 Automatic Text Summarization. University of Turku
Department of Future Technologies. Pauliina Anttila. 2018

3 Sergey Brin and Lawrence Page. The anatomy of a large-scale hypertextual web search engine. Computer networks and ISDN systems, 1998.