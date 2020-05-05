# Python Init

## Hola!

Bienvenido a Python Init, un repositorio para practicar ejercicios básicos de Python 🐍🖤.

## Introducción

Los __objetivos__ de Python Init son:

- Proveer una serie de ejercicios que vayan incrementando gradualmente su complejidad

- Crear un marco de trabajo similar al que ocurre en una empresa o en un proyecto open source

- Generar un espacio para que la gente que está comenzando a programar pueda recibir feedback de programadores/as con más experiencia

Python Init __no__ es:

- Un lugar para aprender a programar desde cero, para eso existen excelentes cursos como ser el de Chuck Severance [Python for Everybody](https://www.youtube.com/watch?v=8DvywoWv6fI)

## Requerimientos

Antes de comenzar, nuestra computadora debería contar con:

- python 3 (es importante que __no__ sea python 2) - [como instalarlo](https://realpython.com/installing-python/)

- git - [como instalarlo](https://www.digitalocean.com/community/tutorials/how-to-contribute-to-open-source-getting-started-with-git)

Y nosotros deberíamos contar con conocimientos básicos de como usar git y github. Hay un excelente video introductorio de [Brian Yu](https://www.youtube.com/watch?v=MJUJ4wbFm_A)

## Comenzando

### Revisando las herramientas

Antes que nada deberíamos chequear que tenemos todo lo necesario para empezar a resolver los ejercicios. Para verificar que nuestra instalación de python es correcta podemos correr en una terminal:

```bash
python -V
Python 3.8.2
```

Y debería devolvernos la versión de python que tenemos (yo estoy usando `3.8.2` en este momento pero cualquier versión que comience con 3 está bien).

Luego chequeamos que `git` esté instalado:

```bash
git --version
git version 2.21.0 (Apple Git-122)
```

La versión de git no es demasiado importante. Cualquier instalación relativamente moderna nos va a permitir trabajar con Python Init.

### Forkear el repositorio

Lo primero que tenemos que hacer es forkear este repositorio (copiarlo) para que quede bajo nuestro usuario de github, si no tenemos una cuenta, [acá hay un tutorial de cómo crearla](https://help.github.com/es/github/getting-started-with-github/signing-up-for-a-new-github-account) (no es necesario pagar, con la versión gratis es más que suficiente).

Para más información de como forkear el repositorio [ver este documento](https://help.github.com/es/github/getting-started-with-github/fork-a-repo)

### Clonar el repositorio en nuestra máquina

El paso siguiente es clonar el repositorio en nuestra PC. Para tal fin corremos:

```bash
git clone https://github.com/<nombre_de_usuario>/python_init
```

En una carpeta de nuestra compu. Reemplazar `<nombre_de_usuario>` por nuestro nombre de usuario de github.


### Instalar dependencias

Una vez clonado el repositorio procedemos a instalar las dependencias necesarias con pip.

__Importante:__ pip debería apuntar a nuestra instalación de python 3 (nunca de python 2), para confirmar esto podemos correr `pip -V`. En caso de apuntar a una distribución de python 2, probar con `pip3 -V`.

En adelante asumiremos que el comando `pip` apunta a una instalación de python 3, reemplazar por `pip3` de ser necesario.

```bash
pip install -r requirements.txt
```

Esto instalará las dependencias.

__Usuarios avanzados:__ para los usuarios que conozcan un poco más de python y sepan de entornos virtuales, notar que también existe un `pyproject.toml` que puede ser utilizado con [poetry](https://python-poetry.org/)


## Probando las dependencias

Para probar que tenemos todo instalado podemos intentar correr los tests con `pytest`:

```bash
pytest -v .
```

El resultado debería ser similar a este:

```bash
============================= test session starts ==============================
platform darwin -- Python 3.8.2, pytest-5.4.1, py-1.8.1, pluggy-0.13.1 -- /Users/pablo/Library/Caches/pypoetry/virtualenvs/python-init-BmScUBFz-py3.8/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/Users/pablo/projects/playground/python_init/.hypothesis/examples')
rootdir: /Users/pablo/projects/playground/python_init
plugins: hypothesis-5.10.3
collecting ... collected 9 items

numbers/number_test.py::test_sum_two_numbers SKIPPED                     [ 11%]
numbers/number_test.py::test_is_even SKIPPED                             [ 22%]
numbers/number_test.py::test_is_odd SKIPPED                              [ 33%]
numbers/number_test.py::test_is_prime SKIPPED                            [ 44%]
numbers/number_test.py::test_sum_all_array SKIPPED                       [ 55%]
numbers/number_test.py::test_sum_all_array_varags SKIPPED                [ 66%]
triangles/triangle_h_test.py::test_triangle_characters SKIPPED           [ 77%]
triangles/triangle_test.py::test_triangle_draw_large SKIPPED             [ 88%]
triangles/triangle_test.py::test_triangle_draw_small SKIPPED             [100%]

============================== 9 skipped in 0.03s ==============================
```

Como vemos, hay una gran cantidad de tests y todos están como _skipped_, o sea, que __no__ se ejecutaron. 

Sin embargo nuestra instalación de python es correcta y tenemos las dependencias necesarias! 🌝


## Implementando nuestra primera función

Una vez que podemos correr los tests, implementaremos nuestra primera función.

En la carpeta `numbers`, dentro del archivo `numbers.py` encontramos la función `add`:

```python
def add(a, b):
    pass
```

Como podemos ver, tanto `add` como el resto de las funciones están vacías. Procedemos a implementarla:

```python
def add(a, b):
    return a + b
```

Guardamos el archivo y vamos a `numbers_test.py` en la misma carpeta, para buscar el test que prueba la funcionalidad de `add`:

```python
@pytest.mark.skip()
def test_sum_two_numbers():
    assert number.add(1, 2) == 3
```

Como vemos el test tiene el [decorator](https://realpython.com/primer-on-python-decorators/) `@pytest.mark.skip`. Lo quitamos borrando la línea y guardamos el archivo.


## Corriendo los tests nuevamente

Si volvemos a correr `pytest -v .` veremos un output similar al siguiente:

```
============================= test session starts ==============================
platform darwin -- Python 3.8.2, pytest-5.4.1, py-1.8.1, pluggy-0.13.1 -- /Users/pablo/Library/Caches/pypoetry/virtualenvs/python-init-BmScUBFz-py3.8/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/Users/pablo/projects/playground/python_init/.hypothesis/examples')
rootdir: /Users/pablo/projects/playground/python_init
plugins: hypothesis-5.10.3
collecting ... collected 9 items

numbers/number_test.py::test_sum_two_numbers PASSED                      [ 11%]
numbers/number_test.py::test_is_even SKIPPED                             [ 22%]
numbers/number_test.py::test_is_odd SKIPPED                              [ 33%]
numbers/number_test.py::test_is_prime SKIPPED                            [ 44%]
numbers/number_test.py::test_sum_all_array SKIPPED                       [ 55%]
numbers/number_test.py::test_sum_all_array_varags SKIPPED                [ 66%]
triangles/triangle_h_test.py::test_triangle_characters SKIPPED           [ 77%]
triangles/triangle_test.py::test_triangle_draw_large SKIPPED             [ 88%]
triangles/triangle_test.py::test_triangle_draw_small SKIPPED             [100%]

========================= 1 passed, 8 skipped in 0.03s =========================
```

Notar que la función `test_sum_two_numbers` no dice más _skipped_ sino que dice _passed_. Esto significa que nuestra implementación es correcta! 😊

Opcionalmente podemos probar de implementar mal la función `add` (por ejemplo, restando en vez de sumar) y ver cómo el test falla. También podemos agregar otros tests más complejos (números negativos, sumarle cero a un número, etc)

## Subiendo Nuestro Código

Deberíamos a esta altura tener modificaciones en el archivo `numbers.py` y `numbers_test.py`. Comiteamos los cambios y los pusheamos a nuestro repositorio.


## Generando un Pull Request

Una vez que tenemos los cambios pusheados a nuestro repositorio, mandamos un pull request al repositorio original. Más detalles sobre este proceso [en el siguiente artículo](https://help.github.com/es/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork).

## Esperar Feedback

En esta etapa, un/a programador/a con más experiencia revisará tu código y te dará feedback de qué cosas mejorar en el caso de que las haya.

Esto es una simulación muy fiel de lo que pasa en un equipo de trabajo real, los pull requests son el medio en el cuál los programadores discuten ideas, implementaciones, etc.

## Cerrar y Repetir

Una vez aprobado el pull request, debemos cerrarlo. En un trabajo _real_ nuestro código sería _mergeado_ con el repositorio original, sin embargo, si lo hacemos ahora, otras personas que se bajen el mismo código para practicar tendrán nuestra solución en vez de la función vacía. Por ese motivo lo cerramos.

Y ahora a buscar otra función que sea más difícil (y más divertida 😃) que `add`. Adelante!
