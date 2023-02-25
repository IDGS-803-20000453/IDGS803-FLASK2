
from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField
from wtforms import IntegerField


class UserForm(Form):
    matricula=StringField('Matricula')
    nombre=StringField('Nombre')
    apaterno=StringField('Apaterno')
    email=EmailField('Correo')
    numero = IntegerField('Número')

class DynamicForm(FlaskForm):
    pass

    