from operator import truediv
from flask import Flask, render_template, request, redirect
from datetime import date
from conexion import insert_libro

app = Flask(__name__, static_url_path='')

admin_val = [0]

def headers(titulo, hojacss):
    ret = '<!DOCTYPE html>'\
        '<html>'\
        '    <head>'\
        '        <meta charset="utf-8">'\
        '        <meta http-equiv="X-UA-Compatible" content="IE=edge">'\
        '        <meta name="viewport" content="width=device-width, initial-scale=1.0">'\
        '        <title>' + titulo + '</title>'\
        '        <link href="' + hojacss + '" rel="stylesheet">'\
        '        <link rel="shortcut icon" href="/libro.ico" type="image/x-icon">'\
        '    </head>'\
        '   ' #Insertar el '</html>' en cada funcion
    return ret

@app.route("/")
def inicio():
    return redirect('/admin', code=302)

@app.route("/admin")
def admin():
    ret = headers("Log-in", "styles.css")

    ret = ret + '    <body>'\
        '        <div id="top">'\
        '            <form action="validacion" method="post" id="frm">'\
        '                <input type="text" name="user1" id="u1">'\
        '                <input type="password" name="pass1" id="p1">'\
        '                <input type="submit" value="&gt;" id="v1">'\
        '                </select>'\
        '            </form>'\
        '        </div>'\
        '    </body>'\
        '</html>'

    return ret

@app.route("/validacion", methods=["POST"]) #FUNCION / NO PAGINA - - - - - -
def val_admin():
    dato = request.form.to_dict()

    usr = dato['user1']
    pwd = dato['pass1']

    if usr == "admin" and pwd == "123":
        admin_val[0] = 1
        return redirect('/control', code=302)

    #si el usuario y contra andan finos, el value de la key del diccionario se vuelve TRUE
    return redirect('/admin', code=302)
    #si no, redirigir pa tras

#7 INPUTS OBLIGATORIOS | 7 TEXTOS/PLACEHOLDERS | 1 BOTON DE ENVIO + REDIRECCION AL CONTROL
@app.route("/control") #PAGINA - - - - - - - - - - - - - - - -
def control():
    if admin_val[0] == 0:
        return redirect('/admin', code=302)

    ret = headers("Registrar Libro", "styles.css")#Cambiar styles.css por CDN de boostrap

    ret = ret + '    <body>'\
        '        <div id="top">'\
        '            <h1>Insertar Libro</h1>'\
        '            <form action="RegLibro" method="post" id="frm">'\
        '                <input type="text" name="nomL1" id="nombreL1" placeholder="Nombre del libro" required>'\
        '                <input type="text" name="autL1" id="autorL1" placeholder="Autor" required>'\
        '                <input type="text" name="catL1" id="categoríaL1" placeholder="Categoría" required>'\
        '                <input type="number" name="prcL1" id="precioL1" placeholder="Precio" required>'\
        '                <input type="text" name="ediL1" id="editorialL1" placeholder="Editorial" required>'\
        '                <input type="number" name="stkL1" id="stockL1" placeholder="Stock" required>'\
        '                <input type="number" name="vntL1" id="ventasL1" placeholder="Ventas" required>'\
        '                <input type="submit" value="&gt;" id="v1">'\
        '                </select>'\
        '            </form>'\
        '        </div>'\
        '    </body>'\
        '</html>'

    #ret = str(date.today())
    #Si el value del socket es verdadero, adelante. CONVERTIR EN FUNCION REUTILIZABLE
    return(ret)

@app.route("/RegLibro", methods=["POST"]) #FUNCION / NO PAGINA - - - - - - - - RET(/control)
def reg_libro():
    dato = request.form.to_dict()

    nom = dato['nomL1']
    aut = dato['autL1']
    cat = dato['catL1']
    prc = dato['prcL1']
    edi = dato['ediL1']
    stk = dato['stkL1']
    vnt = dato['vntL1']

    print(nom, aut, cat, prc, edi, stk, vnt)

    insert_libro(nom, aut, cat, prc, edi, stk, vnt)

    return redirect('/control', code=302)

@app.route("/VerModLibro") #PAGINA - - - - - - - - - - - - - - - -
def ver_mod_libro():
    ret = headers("Modificar Libro", "styles.css")

    ret = "b"
    return(ret)

@app.route("/ModLibro") #FUNCION / NO PAGINA - - - - - - - - RET(/control)
def mod_libro():
    ret = "b"
    return(ret)

    return redirect('/control', code=302)

@app.route("/BorrarLibro") #FUNCION / NO PAGINA - - - - - - - - RET(/control)
def brr_libro():
    ret= "a"
    return(ret)

    return redirect('/control', code=302)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

@app.route("/Busqueda")
def busqueda():
    ret = "b"
    return(ret)

@app.route("/Libro")
def eleccion():
    ret = "a"
    return(ret)

@app.route("/meterCarrito")
def insertarCarrito():
    ret ="b"
    return(ret)

@app.route("/VerCarrito")
def carrito():
    ret = "a"
    return(ret)

@app.route("/VerHistorial")
def historial():
    ret = "a"
    return(ret)

@app.route("/Signup")
def registrarse():
    ret = "b"
    return(ret)

@app.route("/val_cliente")
def val_cliente():
    ret = "a"
    return(ret)

#crear espacios y botones necesarios para inserciones de libros

#luego para modificaciones

#luego para eliminar


#ruta de pagina principal que pone libros mas vendidos

#deberia poner libros de categoria relacionada (default:famosos)


#click al libro devuelva mas datos

#la categoria de este debe cargar de otras


#añadir al carro y ver 

#consultar el carro para ver que si aparezcan los datos alla

#if['SOCKETID'].clave == TRUE: permitir acceso al mismo SOCKETID solicitante

app.run(debug=True)