
  
       
      

      
   
mapa=(
[-3,-3,2,-3,3,-2,-2,1 ,2 ,0, 2,0,1],
[2, 3,'I',-1,-1,3,2,0,-3,-3, 2,2,1],
[1,-3,-3,2, 3,1,3,3,2, 1,-2,-2,2,3],
[0,0, 3,0,3,-3,-2,-3,0, 2, 2, 1, 1],
[2,-1,-1,-3 ,3, 3,0,-3, 1,-2,2,0,1],
[0,3,-1,1,-1,-2,-2,-2,2,-1,-2,-3,0],
[0,3,2 ,0, 1, 1,2,3,-1,-3, 0, 0,-2],
[3,3,-3,-2,3,-3,-1,-3,3,-2,2,-2,-1],
[-2,-2,1,0,-1,0,3 ,0, 0,-2,2,-3,-1],
[-3, 3,0,-1,-3,1 ,2,-3,2,-3,0,2,-2],
[-3,-3,-3,3,-2,0,-2,-3,1,0,1,-1,-2],
[-1,0,1,2,1 ,0,'F',0,-3,3,-2,-2,-1],
[1,-3,1, 0, 1, 2,3,1,-2, 3,3, 0, 3]




)

def buscar (mapa):
    inicio=[]
    final=[]
    inicio=mapa[11][6]
    final= mapa[1][2]
    ruta=[]
    print(type(inicio))
    for fila in mapa:
        print(fila)

buscar(mapa);


