"""
Práctica 2: Listas en Python — Código base
AED I · Bloque I

Completa las tres funciones. Reglas:
  - Trabaja únicamente con list de Python.
  - No uses sort(), sorted(), reverse() ni set.
  - Al terminar cada ejercicio, escribe en el comentario su complejidad temporal.

Para comprobar tu solución, ejecuta este fichero:
    python enunciado_base.py
(o, si tienes pytest instalado:  pytest enunciado_base.py)
"""


# ---------------------------------------------------------------------------
# Ejercicio 1 - Ordenación por inserción (in-place)
# ---------------------------------------------------------------------------
def insertion_sort(lista):
    """Ordena 'lista' de menor a mayor modificándola in-place. No devuelve nada."""
    if lista == []:
        return []

    if len(lista) == 1:
        return lista
    
    for i, elemento in enumerate(lista):
        valor_auxiliar_1 = elemento
        for j in range(i-1, -1, -1):
            if elemento < lista[j]:
                lista[j+1] = lista[j]
                lista[j] = valor_auxiliar_1
            
            if elemento > lista[j]:
                break            
            
            
                
    return lista
    

# Complejidad -> mejor caso: O(1)   peor caso: O(n^2)


# ---------------------------------------------------------------------------
# Ejercicio 2 - Fusionar dos listas ordenadas en una sola pasada
# ---------------------------------------------------------------------------
def fusionar(a, b):
    """Devuelve una lista NUEVA y ordenada con los elementos de a y b (ya ordenadas)."""
    if (a == [] and b == []):
        return []
    
    if (a == []):
        return b
    
    if (b == []):
        return a
    
    lista_nueva = []
    
    i = 0
    j = 0
    
    while (i < len(a) and j < len(b)):
        valor_a = a[i]
        valor_b = b[j]
        if valor_a < valor_b:
            lista_nueva.append(valor_a)
            i += 1
        
        elif valor_b < valor_a:
            lista_nueva.append(valor_b)
            j += 1
        
        else: # valor_b = valor_a
            lista_nueva.append(valor_a)
            lista_nueva.append(valor_b)
            i += 1
            j += 1
    
    if i < len(a):
        while (i < len(a)):
            lista_nueva.append(a[i])
            i += 1
    
    if j < len(b):
        while (j < len(b)):
            lista_nueva.append(b[j])
            j += 1
                
    
    return lista_nueva
    
    
    
    
    

# Complejidad -> O(n)


# ---------------------------------------------------------------------------
# Ejercicio 3 - Eliminar duplicados conservando el orden
# ---------------------------------------------------------------------------
def sin_duplicados(lista):
    """Devuelve una lista NUEVA con la primera aparición de cada valor. Sin set."""
    if lista == []:
        return []
    
    lista_nueva = []
    
    for elemento in lista:
        existe_ya = False
        if lista_nueva == []:
            lista_nueva.append(elemento)
            continue
        
        for elemento_nuevos in lista_nueva:
            if elemento == elemento_nuevos:
                existe_ya = True
                break
        
        if not existe_ya:
            lista_nueva.append(elemento)
    
    return lista_nueva
            
        
            

# Complejidad -> peor caso: O(n^2)   ¿por qué? Porque resulta que el primer y último elemento se repiten, por lo que hay que iterar hasta el final para llegar a descartarlo


# ---------------------------------------------------------------------------
# Pruebas (no hace falta modificarlas)
# ---------------------------------------------------------------------------
def test_ejercicio1():
    datos = [7, 3, 5, 2, 9, 1]
    insertion_sort(datos)
    assert datos == [1, 2, 3, 5, 7, 9]
    vacia = []
    insertion_sort(vacia)
    assert vacia == []
    uno = [42]
    insertion_sort(uno)
    assert uno == [42]
    repetidos = [2, 2, 1, 2]
    insertion_sort(repetidos)
    assert repetidos == [1, 2, 2, 2]
    inversa = [4, 3, 2, 1]
    insertion_sort(inversa)
    assert inversa == [1, 2, 3, 4]


def test_ejercicio2():
    assert fusionar([1, 4, 7], [2, 3, 9]) == [1, 2, 3, 4, 7, 9]
    assert fusionar([], [2, 5]) == [2, 5]
    assert fusionar([2, 5], []) == [2, 5]
    assert fusionar([], []) == []
    assert fusionar([1, 1, 3], [1, 2]) == [1, 1, 1, 2, 3]


def test_ejercicio3():
    assert sin_duplicados([3, 1, 3, 2, 1, 4]) == [3, 1, 2, 4]
    assert sin_duplicados([]) == []
    assert sin_duplicados([5, 5, 5]) == [5]
    original = [3, 1, 3]
    sin_duplicados(original)
    assert original == [3, 1, 3], "No modifiques la lista de entrada"


if __name__ == "__main__":
    for prueba in (test_ejercicio1, test_ejercicio2, test_ejercicio3):
        try:
            prueba()
            print(f"OK    {prueba.__name__}")
        except AssertionError as e:
            print(f"FALLA {prueba.__name__} {e}")
