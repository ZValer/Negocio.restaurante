
"""
Programa para restaurantes

El programa despliega un menu para seleccionar las opciones
Posteriormente hace los cálculos para generar la cuenta,
agregar propina y crear un ticket. 

"""
   
def calcularCuentaTotal(matrizPedido, cuentaTotal,ventas):
    #función para calcular la cuenta total
    #suma los elementos de precios de cada platillo de la matriz creada de platillos y precios
    #la matriz creada tiene platillos en la columna 1 y precios en la columna 2
    #(uso de operadores, funciones, listas, matrices, condicionales, ciclos y ciclos anidados)
    
    for i in range (len(matrizPedido)):
        columna=1
        for j in range (len(matrizPedido[i])):
            if (j==columna):
                cuentaTotal+=matrizPedido[i][j]
    print ("\n Su cuenta total es de: $", cuentaTotal)
    
    #Agrega la propina, llama a otra función para hacer el cálculo
    propina=float(input("\n¿Qué porcentaje de propina desea agregar?: "))
    propinaCalc(propina, cuentaTotal, ventas)
    return cuentaTotal
    
def propinaCalc(porcentaje, cuentaTotal, ventas):
    #función para calcular el porcentaje de propina
    #(uso de operadores, cálculos, funciones)
    print ("Con propina de: ", porcentaje, "%")
    #agrega la propina a la cuenta
    cuentaTotal=cuentaTotal*(1+(porcentaje/100))
    cuentaTotal=(round(cuentaTotal, 2))
    print ("Su cuenta Total es: $", cuentaTotal)
    ventas.append(cuentaTotal)
    return cuentaTotal

def imprime_matriz(matrizPedido):
    #Imprime el platillo y el precio de forma ordenada dada la matriz creada
    #(uso de operadores, funciones, listas, matrices, ciclos)
    for i in range (len(matrizPedido)):
        for j in range (len(matrizPedido[i])):
            print (matrizPedido[i][j], end="\t\t")
        print() #crea un salto de línea para cada renglon
        
    
def desplegarPedido (pedido, ventas):
    #Va llamando las funciones para desplegar el pedido
    #(uso de operadores, funciones, listas, matrices, ciclos)
    
     #crea una matriz de la lista de platillos y precios dada para generar el ticket
    matrizPedido=[[]]
    renglones=int(len(pedido)/2)
    columnas=2
    num=0
    cuentaTotal=0
    for i in range(renglones):
        lista=[]
        for j in range (columnas):
            lista.append(pedido[num])
            num+=1
        matrizPedido.insert(i, lista)
        
     #para desplegar el ticket
    print("\n\n\tTicket \n\nPlatillo\t\tPrecio($)\n")
    imprime_matriz(matrizPedido)
    
     #para calcular e indicar la cuenta
    calcularCuentaTotal(matrizPedido, cuentaTotal, ventas)
    
def imprimeArchivo(nombre):
    #Despliega el contenido de un archivo de texto
    #(Uso de funciones y archivos)
    file=open(nombre, "r")
    file.seek(0)
    contenido=file.read()
    print(contenido)
    file.close
    
def generarReporteVentas(ventas):
    #Escribe los elementos de una lista en un archivo
    #(uso de ciclos, funciones, archivos)
    file=open("archivo_ventas.txt","w+")
    for i in ventas:
        file.write("%s \n"%i)
        #Llama a la función para imprimir el archivo de ventas
    imprimeArchivo("archivo_ventas.txt")
    file.close
    
def sumaCuentas(ventas):
    #suma cada cuenta total
    #(uso de ciclos, uso de listas)
    sumaVentas=0
    for i in range (len(ventas)):
        sumaVentas+=ventas[i]
    print("Total ventas: $", sumaVentas)
    
def main ():
    #función main para iniciar con el programa
    ventas=[]
    continuarPedido="1"
    
    while continuarPedido!="2":  
        #Llama a la función que imprime archivos que imprima menú
        #Despliega platillos y precios desde un archivo de texto
        imprimeArchivo("menu.txt")
        
        x=""
        pedido=[]
                
        #ciclo para seleccionar y seguir agregando platillos
        #(uso de operadores, listas, condicionales, ciclos y ciclos anidados)
        
        while x!="no":
            x=str(input("\n¿Desea agregar un platillo? (si/no): "))
            
            if x=="si":
                num=int(input("Introduce el número de platillo: "))
                #Calcula el precio
                if num==1:
                    pedido.append("Pizza\t")
                    pedido.append(300)
                elif num==2:
                    pedido.append("Pasta\t")
                    pedido.append(200)
                elif num==3:
                    pedido.append("Ensalada")
                    pedido.append(100)
                elif num==4:
                    pedido.append("Ravioles")
                    pedido.append(250)
                    
            elif x!="si" and x!="no":
                print ("Opción no válida, vuelva a intentarlo")
                            
        #(uso de ciclo)
        for contador in range (25):
            print ("_", end="")
        #Llama a la función para desplegar el pedido
        desplegarPedido (pedido,ventas)
        
        seguir=int(input("\nIngresa 1 para continuar: "))
        if seguir==1:
            print ("\n\n1.Hacer pedido \n2.Generar reporte de ventas")
            continuarPedido=str(input("Introduce una opción (1/2): "))
        else:
            continuarPedido=2
       
        
    if continuarPedido=="2":
        #Llama a la función para generar Reporte de Ventas y luego la función para imprimirlo
        generarReporteVentas(ventas)
        print("\nVentas:")
        #Llama a la función para realizar la suma de las cuentas totales
        imprimeArchivo("archivo_ventas.txt")
        sumaCuentas(ventas)
        
        
def pruebas():
    #entrada:Pizza,Pasta
    #salida: Cuenta total=500
    
    #función main para iniciar con el programa
    ventas=[]
    continuarPedido="1"
    
    while continuarPedido!="2":
        
        #Llama a la función que imprime archivos que imprima menú
        #Despliega platillos y precios desde un archivo de texto
        imprimeArchivo("menu.txt")
        
        x=""
        pedido=[]
                
        #ciclo para seleccionar y seguir agregando platillos
        #(uso de operadores, listas, condicionales, ciclos y ciclos anidados)
        
        x="no"
        while x!="no":
            x=str("\n¿Desea agregar un platillo? (si/no): ")
            
            if x=="si":
                num=int("Introduce el número de platillo: ")
                #Calcula el precio
                if num==1:
                    pedido.append("Pizza\t")
                    pedido.append(300)
                elif num==2:
                    pedido.append("Pasta\t")
                    pedido.append(200)
                elif num==3:
                    pedido.append("Ensalada")
                    pedido.append(100)
                elif num==4:
                    pedido.append("Ravioles")
                    pedido.append(250)
                    
            #elif x!="si" and x!="no":
                #print ("Opción no válida, vuelva a intentarlo")
                            
        #(uso de ciclo)
        for contador in range (25):
            print ("_", end="")
        #Llama a la función para desplegar el pedido
        
        pedido=['Pizza\t', 300, 'Pasta\t', 200]
        print(pedido)
        desplegarPedido (pedido,ventas)
        
        seguir=int(input("\nIngresa 1 para continuar: "))
        if seguir==1:
            print ("\n\n1.Hacer pedido \n2.Generar reporte de ventas")
            continuarPedido=str(input("Introduce una opción (1/2): "))
        else:
            continuarPedido=2
       
        
    if continuarPedido=="2":
        #Llama a la función para generar Reporte de Ventas y luego la función para imprimirlo
        generarReporteVentas(ventas)
        print("\nVentas:")
        #Llama a la función para realizar la suma de las cuentas totales
        imprimeArchivo("archivo_ventas.txt")
        sumaCuentas(ventas)
        
   
main()
#pruebas()
    