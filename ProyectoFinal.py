import sys

usu=["fio","Ale"]#Lista de los usuarios
password=["1234","Ale"]#Listas de los password

inventario_data=[
    {"codigo":"01","nombre":"Camisa","cantidad":10},
    {"codigo":"02","nombre":"Blusa","cantidad":25}
]#Lista de los productos del inventario, y se realizaron como diccionarios

def verificar():#Funcion que permite verificar el ingreso de usuario y contrasena
    usuario = input("Ingrese un usuario")
    passw = input("Ingrese un password")
    if usuario in usu and passw in password:# verifica si el usuario y passw esta en la lista de usu y password para pasar al menu principal y si no retorna en falso
        if usu.index(usuario) == password.index(passw):
            return True
    else:
        return False

def usuarios():#Funcion que maneja el submenu de los usuarios
    while True:
        print("Menu del usuario")

        print("1.Anadir usuario\n"
              "2.Eliminar usuario\n"
              "3.Modificar usuario\n"
              "4.Mostrar todos los usuarios\n"
              "5.Salir\n")

        opc=int(input("Seleccione una opcion del menu: "))

        if opc==1:
            nuevo_usu=input("Ingrese el nuevo usuario")
            nuevo_pass=input("Ingrese nuevo password")
            if nuevo_usu not in usu and nuevo_pass not in password:#verifica que el nuevo usuario y password no esten en las listas y si no le manda un mensaje de que ya existe
                usu.append(nuevo_usu)
                password.append(nuevo_pass)
                print("Usuario anadido correctamente")
            else:
                 print("Ese usuario existe")
        elif opc == 2:
            #el usuario ingresa el usu y pass el que desea eliminar
            print(f"La lista de los usuarios y password son los siguientes: Los usuarios son:{usu} y los passwords son:{password}")
            eliminar_usu = input("Ingrese el usuario que desea eliminar")
            eliminar_pass = input("Ingrese el password que desea eliminar")
            if eliminar_usu in usu and eliminar_pass in password:#si esta lo elimina
                index1 = usu.index(eliminar_usu)
                index2 = password.index(eliminar_pass)
                usu.pop(index1)
                password.pop(index2)
                print("El usuario y password fueron eliminados correctamente")
            else:# si no es que lo no existe en la lista
                print("Ese usuario no existe")
        elif opc == 3:
            print("Opcion en contruccion")
        elif opc == 4:
            #imprime todos los usuarios que estan en las listas
            print(f"La lista de los usuarios y password son los siguientes: Los usuarios son:{usu} y los passwords son:{password}")
        elif opc == 4:
            break#lo manda al menu principal
        else:
            print("Opcion invalida")

def inventario():#Funcion que maneja el submenu de inventario
    while True:
        print("Menu del inventario")

        print("1.Ingrese un nuevo producto\n"
              "2.Mostrar el inventario\n"
              "3.Eliminar algun elemento del inventario\n"
              "4.Alguien compro algun producto\n"
              "5.Salir")

        opc=int(input("Ingrese alguna opcion"))

        if opc==1:
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            if any(producto["codigo"]==codigo for producto in inventario_data):#verifica que si el producto existe en la lista
                print("Ese codigo ya existe en el inventario")#ya existe
            else:
                inventario_data.append({"codigo": codigo, "nombre": nombre, "cantidad": cantidad})#No existe y lo ingresa
                print("Producto agregado correctamente.")
        elif opc==2:
            if not inventario_data:#verifica si el inventario esta vacio
                print("El inventario esta vacio")
            else:
                print("El inventario disponible es:\n")
                for producto in inventario_data:#Imprime cada producto de la lista
                    print(f"Codigo: {producto['codigo']},Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")#imprime el codigo,el nombre y cantidad
        elif opc==3:
            codigo = input("Ingrese el código del producto a eliminar: ")
            for producto in inventario_data:
                if producto["codigo"] == codigo:#Con el codigo ingresado del usuario se verifica que exista en la lista
                    inventario_data.remove(producto)#Si se encontro se elimina
                    print("Producto fue eliminado correctamente")
                    break
            else:
                print("Lo siento ese producto no existe")
        elif opc==4:
            print("Opcion en contruccion")
        elif opc==5:
            break#manda al menu principal
        else:
            print("Opcion invalida")


#Verifica si las credenciales son correctas pasa al menu principal
if verificar():
    while True:
        print("Menu Principal del sistema de inventario\n"
              "1.Inventario\n"
              "2.Usuario\n"
              "3.Salir\n")

        opc=int(input("Escoga una opcion: "))

        if opc==1:
            inventario()
        elif opc==2:
            usuarios()
        elif opc==3:
            sys.exit()
        else:
            print("Lo siento esa opcion no existe")
else:
    print("Lo siento ese usuario no existe o el usuario o password son incorrectos")


