# Cómo programar en JavaScript, Python y PHP
Este grupo de lenguajes han mantenido su popularidad con el tiempo, algunos por el impacto que generan en los procesos de aprendizaje, otros porque han sido implementados por grandes exponentes de la industria de la tecnología.

En esta lectura aprenderás cómo implementar en cada uno de estos lenguajes los elementos básicos que utilizarás en tu día a día como desarrolladora de software.

## Variables
En todos los lenguajes, las variables almacenan temporalmente un valor y pueden presentarse de diferentes tipos, sin embargo, su alcance y definición cambian entre un lenguaje y otro enfocándose en la necesidad de tu aplicación y la lógica que estés deseando implementar.

En JavaScript encontrarás que var, let y const serán la manera en la cual puedes definir variables y van a permitirte almacenar algo, pero su uso difiere y se verá extendido o limitado de acuerdo a la que uses, por ejemplo:

Si defines una variable usando “var” tendrás un alcance global, esto quiere decir que el valor de esa variable podrá ser accedido, alterado o bloqueado por procesos dentro del documento donde lo hayas definido.

“let” tiene un alcance más corto y solo estará disponible dentro del bloque de código donde fue definido, de esta manera puedes tener otra variable fuera de ese alcance incluso con el mismo nombre y valor pero no se cruzarán ni generarán conflicto alguno.

Con el uso de “const” hay un punto interesante porque estamos haciendo referencia a un valor que será de sólo lectura, es decir, que esta variable no podrá ser reasignada. Por lo tanto, debemos hacer un uso adecuado correspondiente a su naturaleza.

Para el caso de PHP, se define una variable usando el signo $ seguido del nombre que le des. Además, no es obligatorio definir variables antes de inicializarlas para poder usarlas (aunque ésta sea una buena práctica), por ejemplo:

En lugar de escribir:
````
$saludo;

$saludo = “Hola, soy un saludo”;
````


Puedes escribir:
````
$saludo = “Hola, soy un saludo”;

$numero = 8;

$nombre = “Juanito”;
````


La definición de variables en Python es igualmente muy simple y útil pues no es requerido indicar el tipo de variable o algún símbolo antes de definirla, simplemente tienes que indicar el nombre y en seguida asignarle un valor si así lo deseas, por ejemplo:
````
saludo = “Hola, yo también soy un saludo en Python”

nombre = “Mi nombre es Juanito”
````

## Funciones
Para definir funciones hay una similitud muy marcada entre JavaScript y PHP porque su estructura base es simplemente escribir la palabra reservada “function” seguido por el nombre de la función y paréntesis que bien pueden estar vacíos si no recibe ningún valor o incluir los parámetros separados por comas.

Sin embargo, en PHP puedes definir el alcance de la función; si será pública, privada o estática, pero si no se lo indicas explícitamente, de manera automática se creará pública.

Con Python esta definición es distinta, pues solo utiliza “def”, seguido por el nombre de la función y los parámetros que recibe, al igual que los lenguajes anteriormente mencionados. Adicionalmente, un bloque de código no empieza por las típicas llaves, sino por dos puntos ( : ) que indican que debajo empiezan sus instrucciones a ejecutar.

## Estructuras de control
Cómo ya has visto, cada lenguaje tiene su propia forma de escribir las cosas. No obstante, las estructuras de control son un punto en común. A pesar de que las instrucciones empiecen con llaves, con dos puntos o que las líneas de código terminen en punto y coma o no, la forma del contenido en las estructuras de control no cambia su lógica, suceden de la misma forma y ofrecen el mismo servicio en los tres lenguajes.

El condicional “if” en todos los casos evalúa una condición basada en operadores lógicos de comparación. Los ciclos también siguen con este mismo patrón porque incluso su definición cumple con la misma estructura y respetan la forma en la cual funciona. Es esta la magia de saber programación primero que un lenguaje específico.

## El proceso de debugging
El muy conocido debugging o depuración es una actividad que realizamos cuando estamos probando un código en un punto muy específico del cual necesitamos ver un resultado o una salida en consola para conocer específicamente qué puede estar pasando en un punto crítico de nuestra aplicación.

Para realizar esta inspección, utilizamos normalmente alguna instrucción que nos muestre algo que definamos y dependiendo del lenguaje que utilicemos contamos diferentes herramientas.

En JavaScript existe el muy popular console.log() que dentro de sus paréntesis recibe el valor que va a mostrar justo cuando la ejecución de la aplicación llegue a donde está ubicado y mostrará este valor en consola. Sin embargo, no es el único método pues también se puede utilizar debugger para detener la ejecución de la aplicación justo en el punto donde lo hayamos ubicado.

````
console.log(“Quiero ver esto en consola”)
````


Con PHP hay varias formas y la que utilices dependerá del contexto en el cual quieres ver este mensaje o valor de referencia para la depuración además del tipo de dato que devolverá.

Se puede hacer uso de “echo” que es la forma más clásica de mostrar cadenas de texto en PHP. Sin embargo, no será útil si deseas mostrar valores de tipo objeto o algo más complejo, en este caso puedes usar var_dump para conocer el tipo de dato que devuelves o print_r para imprimir lo que sea que traiga.

````
echo “Quiero ver esto cuando el código pase por aquí”;

var_dump($soyunavariable);

print_r([“Hola”]);
````


Python, por supuesto, también ofrece herramientas para hacer esta actividad de depuración, como es el uso de la librería pdb, con la cual se pueden crear breakpoints sobre los cuales hacer pausas en la ejecución y probar esas fracciones de manera fácil y controlada.

Puedes igualmente usar el clásico “retorno de mensajes”, pero también tienes una herramienta que lo puede hacer por ti.

## Métodos de arrays
Con todo lo que has aprendido, ya puedes entender que la programación es la base y los lenguajes solo son caminos sintácticos que pueden ayudarte en ciertos proyectos o necesidades muy específicas.

Los arrays son secuencias de valores contenidas en un mismo espacio y además comparten su mismo tipo, pero, además de ello, pueden ordenarse, medirse, accederse y realizar muchas acciones más.

En todos los lenguajes lo puedes hacer pero variará la sintaxis que debas usar para lograrlo, algunos métodos de arrays que encontrarás:

Upper para pasar a mayúsculas uno o varios valores de un array.

Lower para pasar a minúsculas uno o varios valores de un array.

Sort para ordenar los valores.

Length para conocer la cantidad de posiciones del array.

Ejemplo de UpperCase en JavaScript para pasar a mayúsculas toda una oración:

````
const cadenaMinuscula = 'espero que tengas un gran dia';

cadenaMinuscula.toUpperCase() //ESPERO QUE TENGAS UN GRAN DIA
````

Ejemplo de tolower en C para pasar a minúsculas toda una palabra:

````
cadena = 'MARIA';

resultado = tolower(cadena); // maria
````


Ejemplo de sort en PHP:

````
$frutas = array("limón", "piña", "naranja", "fresa");

sort($frutas); // fresa, limón, naranja, piña
````


Ejemplo de length en Python:

````
frase = “Quiero saber cuántos caracteres tengo”

len(frase) //37
````


Además, podrás encontrar muchas más en la documentación oficial del lenguaje que uses además de su implementación y sintaxis adecuada.

