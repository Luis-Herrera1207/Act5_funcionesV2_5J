print("--Funciones version 2--")
print("Luis Herrera")
## zona de listas tuplas sets y diccionario
Vehiculos=["Golf gti (2017)","altima (2019)","charger (2015)"]

## Conjuntos
Canciones={"Amor","Stay","Starboy"}
print(Canciones)
for herrera in Canciones:
    print (herrera)
    
## Tuplas
Deportes=("Futbol","Tenis","Boxeo")
print(Deportes)
y = list(Deportes)
print(y)
y[1] = "Boxeo"
x = tuple(y)
print(x)
for herrera in Deportes:
    print(herrera)
    
## Diccionario
Celulares = {"Compañia: Iphone": "","Trabajo Industrial": "","Año: 1959": 1959}
print(Celulares)

## Zona de funciones
def verlista(Vehiculos):
    for unvehiculo in Vehiculos:
        print(unvehiculo)
        

def verlista(Canciones):
    for unacancion in Canciones:
        print(unacancion)
        
def verlista(Deportes):
    for undeporte in Deportes:
        print(undeporte)
        
def verlista(Celulares):
    for uncelular in Celulares:
        print(uncelular)

## Llamadas a funciones 
print("--Vehiculos--")
verlista(Vehiculos)
print("--Canciones--")
verlista(Canciones)
print("--Deportes--")
verlista(Deportes)
print("--Celulares--")
verlista(Celulares)
