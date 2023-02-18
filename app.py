from flask import Flask, render_template, request, redirect, url_for
from flask import request


import forms

app=Flask(__name__)

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


@app.route("/Alumnos",methods=['GET','POST'])
def Alumnos():
    alum_form = forms.UserForm(request.form)
    if request.method =='POST':
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)
    return render_template("Alumnos.html", form=alum_form)


@app.route("/cajas_dinamicas", methods=['GET', 'POST'])
def cajas_dinamicas():
    num_form = forms.UserForm(request.form)
    if request.method == 'POST':
        if num_form.validate():
            num_campos = num_form.numero.data
            return redirect(url_for('nuevo_formulario', num_campos=num_campos))
    return render_template("cajas_dinamicas.html", form=num_form)


@app.route('/nuevo_formulario/<int:num_campos>', methods=['GET', 'POST'])
def nuevo_formulario(num_campos):
    form = forms.DynamicForm(request.form)
    if request.method == 'POST':
        for i in range(num_campos):
            fieldname = 'num{}'.format(i+1)
            value = request.form.get(fieldname, '')
            print('Valor de {}: {}'.format(fieldname, value))
    return render_template('nuevo_formulario.html', form=form, num_campos=num_campos)



if __name__=="__main__":
    app.run(debug=True)
