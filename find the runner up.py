if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    lista = list(arr)
    
 
    lista1 = sorted(lista)
    
    set1 = set(lista1)
    
   
    lista2 = list(set1)
    

    print(lista2[-2])