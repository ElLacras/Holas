#Productos={Modelo:[Marca, Pantalla, Ram, Disco, GB de DD,Procesador, Targeta de Video],}

productos = {
    '8475HD':['HP',15.6,'8GB RAM','DD','1T','Intel Core i5','Nvidia GTX 1050'],
    '2175HD':['Lenovo', 14,'4GB RAM','SSD','512GB','Intel Core i5', 'Nvidia GTX 1050'],
    'JjfFHD':['Asus',14,'16GB RAM','SSD','256GB','Intel Core i7','Nvidia RTX 2080Ti'],
    'fgdxFHD':['HP',15.6,'8GB RAM','DD','1T','Intel Core i3','Intedrada'],
    'GF75HD':['Asus',15.6,'8GB RAM','DD','1T','Intel Core i7', 'Nvidia GTX 1050'],
    '123FHD':['Lenovo',14,'6GB RAM','DD','1T','AMD Ryzen 5','Integrada'],
    '342FHD':['Lenovo',15.6,'8GB RAM','DD','1T','AMD Ryzen 7','Nvidia GTX 1050'],
    'UWU131HD':['Dell',15.6,'8GB RAM','DD','1T','AMD Ryzen 3','Nvidia GTX 1050'],
     
     
}

stock = {
    '8475HD':[387990,10],
    '2175HD':[327990,4],
    'JjfFHD':[424990,1],
    'fgdxFHD':[664990,21],
    'GF75HD':[749990,2],
    '123fhd':[290890,32],
    '342FHD':[444990,1],
    'UWU131HD':[349990,1],
    'FS1230HD':[249990,0],

}

def stock_marca(marca):
    marca = marca.lower()
    total_de_stock = 0
    for producto_id, datos in productos.items():
        producto_marca = datos[2].lower()
        if producto_marca == marca:
            ventas = stock[producto_id][1]
            total_de_stock += ventas
    print(f"Modelo total en stock '{marca}': {total_de_stock}")

def busqueda_por_precio(precio_min, precio_max):
    resultado = []
    for producto_id, datos in productos.items():
        precio = datos[3]
        ventas = stock[producto_id][1]
        if precio_min <= precio <= precio_max and ventas > 0:
            marca_modelo = f"{datos[0]}--{datos[1]}"
            resultado.append(marca_modelo)
    if resultado:
        resultado.sort()
        print("Modelos Encontrado: ")
        for item in resultado:
            print(item)
    else:
        print("No hay existen Modelos")

def actualizar_precio(producto_id, nuevo_precio):
    if producto_id in stock:
        stock[producto_id][1] = nuevo_precio
        return True
    else:
        return False
    
def menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1.- Stock Marca")
        print("2.- Busqueda por Precio")
        print("3.- Actualizar Precio")
        print("4.- Salir.")

        seleccion = input("Seleccione una Opcion: ")

        if seleccion == "1":
            marca = input("Ingrese Marca a Consultar: ")
            stock_marca(marca)

        elif seleccion == "2":
            while True:
                try:
                    precio_min = int(input("Ingrese Precio minimo: "))
                    precio_max = int(input("Ingrese Precio maximo: "))
                    break
                except ValueError:
                    print("!!!Debe ingresar valores enteros!!!")
            busqueda_por_precio(precio_min, precio_max)

        elif seleccion == "3":
            while True:
                producto_id = input("Ingrese Modelo a Actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese Precio Nuevo: "))
                except ValueError:
                    print("Debe ingresar un numero entero para la cantidad")
                    continue
                actualizado = actualizar_precio(producto_id, nuevo_precio)
                if actualizado:
                    print("!!Precio Actualizado!!")
                else:
                    print("!!El Modelo no Existe!!")
                otro = input("Desea actualizar otro Precio? (si/no): ").lower()
                if otro != "si":
                    break

        elif seleccion == "4":
            print("Programa Finalizado.")
            break

        else:
            print("Debe seleccionar una Opcion Valida!!")

menu()