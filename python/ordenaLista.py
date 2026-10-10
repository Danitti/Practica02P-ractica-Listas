def ordena(lista):
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
        


lista = list(map(int, input().split()))
lista = ordena(lista)

print(*lista)