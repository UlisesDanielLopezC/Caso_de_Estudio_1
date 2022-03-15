from operator import truediv
from flask import Flask, redirect
from datetime import date

app = Flask(__name__)

admin_val = [False]

@app.route("/admin")
def admin():
    ret = '<!DOCTYPE html>'\
        '<html>'\
        '    <head>'\
        '        <meta charset="utf-8">'\
        '        <meta http-equiv="X-UA-Compatible" content="IE=edge">'\
        '        <meta name="viewport" content="width=device-width, initial-scale=1.0">'\
        '        <title>Administracion</title>'\
        '        <link href="QWERTY.css" rel="stylesheet">'\
        '        <link rel="shortcut icon" href="QWERTY.ico" type="image/x-icon">'\
        '    </head>'\
        '   '\
        '    <body>'\
        '        <div id="top">'\
        '            <form action="validacion" method="post" id="frm">'\
        '                <input type="password" value="test" name="user1" id="u1">'\
        '                <input type="password" name="pass1" id="p1">'\
        '                <input type="submit" value="&gt;" id="v1">'\
        '                </select>'\
        '            </form>'\
        '        </div>'\
        '    </body>'\
        '</html>'

    return ret

@app.route("/validacion")
def val_admin():
    print("a")
    #si el usuario y contra andan finos, el value de la key del diccionario se vuelve TRUE
    return redirect('/control', code=302)
    #si no, redirigir pa tras

@app.route("/control")
def control():
    ret = str(date.today())
    ls = ['a', 'bc', 0, 5]
    print(ls)
    #Si el value del socket es verdadero, adelante. CONVERTIR EN FUNCION REUTILIZABLE
    return(ret)

@app.route("/RegLibro")
def reg_libro():
    ret = "a"
    return(ret)

@app.route("/ModLibro")
def mod_libro():
    ret = "b"
    return(ret)

@app.route("/BorrarLibro")
def brr_libro():
    ret= "a"
    return(ret)

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