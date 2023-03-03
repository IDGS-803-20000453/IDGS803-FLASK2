from flask import Flask,flash, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from collections import Counter
import forms
import math
from flask import make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = "Este es la clave encriptada"
csrf = CSRFProtect(app)


csrf = CSRFProtect(app)
app.config['WTF_CSRF_ENABLED'] = False

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'),404

def bar(error):
        return render_template('error.html'), 404


@app.route("/cookies", methods = ['GET','POST'])
def cookies():
    reg_user = forms.LongiForms(request.form)
    datos = ''
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        passw = reg_user.password.data
        datos = user + '@' + passw
        success_message = 'Bienvenido {}'.format(user)
        flash(success_message)
    
    response = make_response(render_template('cookies.html', form = reg_user))
    if len(datos) > 0 :
        response.set_cookie('datos_user', datos)
    
    return response


    if len(datos)>0:
        response.set_cookie('datos_user',datos)
        return response

@app.route("/saludo")
def saludo():
    valor_cookie = request.cookies.get('datos_user')
    nombres = valor_cookie.split('@')
    return render_template('saludo.html', nom = nombres[0])
valores = {
        "1": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
        "9": 8,
        "10": 9
    }
english_names = {
        "1": "black",
        "2": "brown",
        "3": "red",
        "4": "orange",
        "5": "yellow",
        "6": "green",
        "7": "blue",
        "8": "violet",
        "9": "gray",
        "10": "white",
        "oro": "gold",
        "plata": "silver"
    }
esp_names = {
            "1": "negro",
            "2": "cafe",
            "3": "rojo",
            "4": "naranja",
            "5": "amarillo",
            "6": "verde",
            "7": "azul",
            "8": "violeta",
            "9": "gris",
            "10": "blanco",
            "oro": "oro",
            "plata": "plata"
        }

@app.route("/traductor",methods=['GET','POST'])
def traducir():
    result=""
    
    if request.form.get("palabraEng") or request.form.get("palabraEsp"):
        palabraIngles=request.form.get("palabraEng")
        palabraEspanol=request.form.get("palabraEsp")
        f = open('palabras.txt','a')
        f.write(palabraIngles.lower()+' '+palabraEspanol.lower()+'\n')
        f.close()
    elif request.form.get("palabra"):
        palabra=request.form.get("palabra").lower()

        fichero = open('palabras.txt')
        lineas = fichero.readlines()

        for linea in lineas:
            arraySplit=linea.split()
            if arraySplit[0] == palabra:
                result=arraySplit[1]
            elif arraySplit[1] == palabra:
                result=arraySplit[0]

    return render_template('traductor.html',result=result)

@app.route("/resistencia",methods=['GET','POST'])
def calcularResistencia():
    banda1=request.form.get("banda1")
    banda2=request.form.get("banda2")
    banda3=request.form.get("banda3")
    tolerancia= request.form.get("tolerancia")
    if request.method == 'POST':
        banda1_en = english_names[banda1]
        banda2_en = english_names[banda2]
        banda3_en = english_names[banda3]
        tolerancia_en = english_names[tolerancia]

        valor1 = valores[banda1]
        valor2 = valores[banda2]
        multiplicador = math.pow(10, valores[banda3])
        tolerancia_valor = 0.05 if tolerancia == "oro" else 0.1

        valor = (valor1 * 10 + valor2) * multiplicador
        valor_minimo = valor * (1 - tolerancia_valor)
        valor_maximo = valor * (1 + tolerancia_valor)

        return render_template('calcularRes.html',banda1=esp_names[banda1],banda2=esp_names[banda2],banda3=esp_names[banda3],tolerancia=esp_names[tolerancia], banda1_en=banda1_en,banda2_en=banda2_en,banda3_en=banda3_en,tolerancia_en=tolerancia_en, valor=valor,valor_minimo=valor_minimo,valor_maximo=valor_maximo)
    return render_template('calcularRes.html')

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/Alumnos", methods=['GET', 'POST'])
def Alumnos():
    alum_form = forms.UserForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)
        print(alum_form.apaterno.data)
        print(alum_form.email.data)
    return render_template("Alumnos.html", form=alum_form)

@app.route("/cajas_dinamicas", methods=['GET', 'POST'])
def cajas_dinamicas():
    num_form = forms.UserForm(request.form)
    if request.method == 'POST':
        if num_form.validate():
            num_campos = num_form.numero.data
            return redirect(url_for('nuevo_formulario', num_campos=num_campos, form_data=num_form.data))
    return render_template("cajas_dinamicas.html", form=num_form)

@app.route('/nuevo_formulario/<int:num_campos>', methods=['GET', 'POST'])
def nuevo_formulario(num_campos):
    form_data = request.args.get('form_data')
    form = forms.DynamicForm(request.form)
    form.num_campos = num_campos
    if request.method == 'POST':
        valores = []
        for i in range(num_campos):
            fieldname = 'num{}'.format(i+1)
            value = request.form.get(fieldname, '')
            valores.append(float(value))
        promedio = sum(valores) / num_campos
        maximo = max(valores)
        minimo = min(valores)
        repeticiones = [num for num, count in Counter(valores).items() if count > 1]
        return render_template('formulario_dinamico.html', form=form, promedio=promedio, maximo=maximo, minimo=minimo, repeticiones=repeticiones)
    return render_template('formulario_dinamico.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
