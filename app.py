from flask import Flask, render_template,abort
import os
import json
with open("books.json") as fichero:
    datos=json.load(fichero)
app = Flask(__name__)	

@app.route('/')
def inicio():
    libros=[]
    for i in datos:
        dic={"titulo":i.get("title"),"isbn":i.get("isbn")}
        libros.append(dic)
    return render_template("inicio.html",libros=libros)
@app.route('/libro/<num1>')
def detalle(num1):
    ind=0
    for i in datos:
        if i.get("isbn") == num1:
            tit=i.get("title")
            img=i.get("thumbnailUrl")
            autores=i.get("authors")
            descripcion=i.get("longDescription")
            categorias=i.get("categories")
            status=i.get("status")
            numpag=i.get("pageCount")
            ind=1
    if ind == 0:
        abort(404)
    return render_template("libro.html",tit=tit,img=img,autores=autores,descripcion=descripcion,categorias=categorias,status=status,numpag=numpag)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=True)
