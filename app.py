from flask import Flask,flash, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from collections import Counter
import forms
from flask import make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = "Este es la clave encriptada"

csrf = CSRFProtect(app)
app.config['WTF_CSRF_ENABLED'] = False

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'),404

def bar(error):
        return render_template('error.html'), 404


@app.route("/cookies")
def cookies():
    reg_user=forms.LongiForms(request.form)
    datos=''
    if request.method=='POST' and reg_user.validate():
        user=reg_user.username.data
        passw= reg_user.password.data
        datos= user + '@'+ passw
        succes_message='Bienvenido {}'.format(user)
        flash(succes_message)
    response=make_response(render_template('cookies.html',form=reg_user))


    if len(datos)>0:
        response.set_cookie('datos_user',datos)
        return response

@app.route("/saludo")
def saludo():
    valor_cookie= request.cookie.get('datos_user')
    nombres= valor_cookie.split('@')
    return render_template('saludo.html',nom=nombres(0))
    
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
