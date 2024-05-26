from django import forms


class CompanyForm(forms.Form):
    razao_social = forms.CharField(
        label='Razão Social',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Razão Social'}
        ),
    )
    cnpj = forms.IntegerField(
        label='CNPJ',
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'CNPJ'}
        ),
    )
    estado = forms.CharField(
        label='Estado',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Estado'}
        ),
    )
    cidade = forms.CharField(
        label='Cidade',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Cidade'}
        ),
    )
    bairro = forms.CharField(
        label='Bairro',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Bairro'}
        ),
    )
    endereco = forms.CharField(
        label='Endereço',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Endereço'}
        ),
    )
    cep = forms.IntegerField(
        label='CEP',
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'CEP'}
        ),
    )
    numero = forms.IntegerField(
        label='Número',
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Número'}
        ),
    )
    complemento = forms.CharField(
        label='Complemento',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Complemento'}
        ),
    )


class ContactForm(forms.Form):
    nome = forms.CharField(
        label='Nome',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nome'}
        ),
    )
    telefone = forms.CharField(
        label='Telefone',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Telefone'}
        ),
    )
    celular = forms.CharField(
        label='Celular',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Celular'}
        ),
    )
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}
        ),
    )
    cargo = forms.CharField(
        label='Cargo',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Cargo'}
        ),
    )
    departamento = forms.CharField(
        label='Departamento',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Departamento'}
        ),
    )
    observacao = forms.CharField(
        label='Observação',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Observação'}
        ),
    )
    recebe_email = forms.BooleanField(
        label='Recebe Email?',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
