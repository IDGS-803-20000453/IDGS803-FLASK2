
from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField
from wtforms import IntegerField
from wtforms import validators

def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula=StringField('Matricula',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=15,message='No cumple con la longitud para el campo')])
    nombre=StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido')])
    apaterno=StringField('Apaterno',[
        validators.DataRequired(message='El campo es requerido')])
    email=EmailField('Correo',[mi_validacion])
    numero = IntegerField('Número')


class LongiForms(Form):
    username=StringField('usuario',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=15,message='No cumple con la longitud para el campo')])
    password=StringField('password',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=15,message='No cumple con la longitud para el campo')])


class DynamicForm(FlaskForm):
    pass

    