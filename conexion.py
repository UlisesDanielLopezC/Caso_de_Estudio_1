from os import name
import mysql.connector

DB = mysql.connector.connect(
    user='root', password='', database='tiendalibros'
)

cursor = DB.cursor()

#ADMIN: insertar libros
#7 INPUTS OBLIGATORIOS | 7 TEXTOS | 1 BOTON DE ENVIO + LIMPIADO AL ENVIAR
def insert_libro(nom, aut, cat, prc, edi, stk, vnt):
    reg = "INSERT INTO libros(nombre, autor, categoria, precio, editorial, stock, ventas) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(reg, (nom, aut, cat, prc, edi, stk, vnt))
    DB.commit()

#ADMIN: modificar libros
#1 subrayado en la palabra MODIFICAR inicia esto
#6 INPUTS CON VALUE | 6 TEXTOS | 1 BOTON DE ENVIO + SER RECARGAR PAGINA o REENVIAR A LA PAGINA DEL LIBRO
def update_libro(id, nom, aut, cat, prc, edi, stk):
    #Los inputs deben tener sus valores originales. Consultar y ponerlos ahi
    upd = "UPDATE libros SET nombre = %s WHERE id = %s"
    cursor.execute(upd, (nom, id))
    upd = "UPDATE libros SET autor = %s WHERE id = %s"
    cursor.execute(upd, (aut, id))
    upd = "UPDATE libros SET categoria = %s WHERE id = %s"
    cursor.execute(upd, (cat, id))
    upd = "UPDATE libros SET precio = %s WHERE id = %s"
    cursor.execute(upd, (prc, id))
    upd = "UPDATE libros SET editorial = %s WHERE id = %s"
    cursor.execute(upd, (edi, id))
    upd = "UPDATE libros SET stock = %s WHERE id = %s"
    cursor.execute(upd, (stk, id))
    DB.commit()

#ADMIN: borrar libros
#1 subrayado en la palabra ELIMINAR envia la id
def delete_libro(id):
    dlt = "DELETE FROM libros WHERE id = %s"
    cursor.execute(dlt, (id,))
    DB.commit()

#CLIENTE: buscar libros
#1 ENTRADA para escribir | 1 BOTON para enviar
def select_libros(nom):
    cons = f"SELECT id, nombre, autor, precio, editorial FROM libros WHERE nombre LIKE \"%{nom}%\""
    cursor.execute(cons)
    
    libros = []
    for row in cursor.fetchall():
        l = {
            'id': row[0],
            'nombre': row[1],
            'autor': row[2],
            'precio': row[3],
            'editorial': row[4]
        }
        libros.append(l)
    return libros

#ADD: ver libro + ver relacionados
#1 SUBRAYADO para entrar al libro
def select_libro(id):
    cons = "SELECT * FROM libros WHERE id = %s"
    cursor.execute(cons, (id,))

    l_r = []
    row = cursor.fetchall()
    l = {
        'id': row[0],
        'nombre': row[1],
        'autor': row[2],
        'categoria': row[3],
        'precio': row[4],
        'editorial': row[5],
        'stock': row[6],
        'ventas': row[7]
    }
    l_r.append(l)

    cat = l['categoria']

    rels = "SELECT id, nombre, autor FROM libros WHERE categoria = %s LIMIT 5"
    cursor.execute(rels, (cat,))

    for row in cursor.fetchall():
        r = {
            'id': row[0],
            'nombre': row[1],
            'autor': row[2]
        }
        l_r.append(r)

    return l_r

#CLIENTE: añadir libro al carrito
#3 ELECCIONES | paqueteria | modo de envio | metodo de pago | 1 BOTON para enviar
def insert_carro(stk, idl, idc, mtp, num, dtp, idm, mdm, precio_l, costo_env):
    #DEFINIR CON EL STOCK ALGO basado en num>stk
    #MTP debe recibir una cadena especifica segun lo que se haya elegido "TARJETA" / "CHEQUE"
    #IDM debe recibir una ^^^ de la paqueteria elegida (LISTA DE ELECCION SUBMIT) 
    #MODO DE ENV "NORMAL"100 / "RAPIDO"150 / "EXPRESS"200 altera el COSTO de ENV (procesado en el main.py)

    #ADD: fraccion de envio en caso de limite

    imp = precio_l + costo_env

    reg = "INSERT INTO carrito VALUES (%s, %s, \"PROCESANDO\", %s, %s, %s, %s, %s, %s)"
    cursor.execute(reg, (idl, idc, mtp, num, dtp, imp, idm, mdm))
    DB.commit()

#CLIENTE: ver su carrito
#1 BOTON para acceder al carro
def select_carro(id):
    cons = "SELECT * FROM carrito WHERE id_cliente = %s"
    cursor.execute(cons, (id,))

    pedidos = []
    for row in cursor.fetchall():
        p = {
            'idl': row[0],
            'idc': row[1],
            'estatus': row[2],
            'met_pago': row[3],
            'cantidad': row[4],
            'fecha_ped': row[5],
            'importe_t': row[6],
            'idm': row[7],
            'modo_mensj': row[8]
        }
        pedidos.append(p)

    libros = []
    for pedido in pedidos:
        idl = pedido[0]
        cons = "SELECT id, nombre, autor, precio, stock FROM libros WHERE id = %s"
        cursor.execute(cons, (idl,))

        row = cursor.fetchall()
        l = {
            'id': row[0],
            'nombre': row[1],
            'autor': row[2],
            'precio': row[3],
        }
        libros.append(l)

    return pedidos, libros

#CLIENTE: ver etapas de un envio

#Debe ir alterando el valor de carrito.estatus


#AMBOS: ver historial de un cliente
#despues de que el estatus sea "completado" recibir el la fila para historial
def insert_historial(idl, idc, dtp, dtr, cst):
    reg = "INSERT INTO historial VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(reg, (idl, idc, dtp, dtr, cst))
    DB.commit()
    #sumar uno a ventas de ese libro

#al entrar a un perfil de un cliente ver su historial
#1 BOTON para acceder al historial
def select_historial(id):
    cons = "SELECT * FROM historial WHERE id_cliente = %s"
    cursor.execute(cons, (id,))

    historial = []
    for row in cursor.fetchall():
        h = {
            'idl': row[0],
            'idc': row[1],
            'f_ped': row[2],
            'f_rec': row[3],
            'costo': row[4]
        }
        historial.append(h)
    #poder ir al libro a partir del id regresado al el HTML
    return historial

#ADD: actualizacion constante de la pagina


#AMBOS: ver estadisticas de libros mas vendidos
#1 BOTON para acceder a los datos
def mas_vendidos():
    cons = "SELECT id, nombre, autor, precio, editorial FROM libros ORDER BY ventas DESC LIMIT 5"
    cursor.execute(cons)
    
    libros = []
    for row in cursor.fetchall():
        l = {
            'id': row[0],
            'nombre': row[1],
            'autor': row[2],
            'precio': row[3],
            'editorial': row[4]
        }
        libros.append(l)
    return libros

#CLIENTE: darse de alta
#7 INPUTS OBLIGATORIOS | 2 BUTTON aceptar y cancelar
def insert_cliente(nom, apl, trj, crr, psw, num, dir):
    reg = "INSERT INTO clientes(nombres, apellidos, tarjeta, correo, contra, numtel, direccion) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(reg, (nom, apl, trj, crr, psw, num, dir))
    DB.commit()

#CLIENTE: autenticar sesion
#2 INPUTS | 1 BOTON
def select_cliente(crr, psw):
    cons = "SELECT COUNT(*) FROM clientes WHERE correo = %s AND contra = %s"
    cursor.execute(cons, (crr, psw))
    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False