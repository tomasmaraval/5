from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserModel, UserChangeForm

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class EntregablesFormulario(forms.Form):
    nombre = forms.CharField()
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()

class UserCreationFormCustom(UserCreationForm):
    username = forms.CharField(label='Usuario', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k: '' for k in fields}

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Ingrese su email:')
    first_name = forms.CharField(label='Ingrese su nombre:')
    last_name = forms.CharField(label='Ingrese su apellido:')
    imagen = forms.ImageField(label='Ingrese su foto de perfil:', required=False)

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'imagen')
        help_texts = {k: '' for k in fields}