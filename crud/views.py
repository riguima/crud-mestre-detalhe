import json

from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render

from .forms import CompanyForm, ContactForm
from .models import Company, Contact


def index(request):
    for contact_model in Contact.objects.filter(empresa=None):
        contact_model.delete()
    return render(
        request, 'crud/index.html', {'companies': Company.objects.all()}
    )


def add_company(request):
    return render(
        request,
        'crud/add_company.html',
        {
            'company_form': CompanyForm(),
            'contact_form': ContactForm(),
        },
    )


def edit_company(request, company_id):
    company_model = Company.objects.get(pk=company_id)
    company_form = CompanyForm({
        'razao_social': company_model.razao_social,
        'cnpj': company_model.cnpj,
        'estado': company_model.estado,
        'cidade': company_model.cidade,
        'bairro': company_model.bairro,
        'endereco': company_model.endereco,
        'cep': company_model.cep,
        'numero': str(company_model.numero),
        'complemento': company_model.complemento,
    })
    return render(
        request,
        'crud/edit_company.html',
        {
            'company_form': company_form,
            'contact_form': ContactForm(),
            'company': company_model,
        },
    )


def add_company_action(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        company_model = Company(
            razao_social=data['razao_social'],
            endereco=data['endereco'],
            bairro=data['bairro'],
            cidade=data['cidade'],
            cnpj=data['cnpj'],
            numero=int(data['numero']),
            complemento=data['complemento'],
            estado=data['estado'],
            cep=data['cep'],
        )
        company_model.save()
        for contact_id in data['contatos_ids']:
            contact_model = Contact.objects.get(pk=contact_id)
            contact_model.empresa = company_model
            contact_model.save()
        return JsonResponse({
            'id': company_model.id,
            'razao_social': company_model.razao_social,
            'endereco': company_model.endereco,
            'bairro': company_model.bairro,
            'cidade': company_model.cidade,
            'cnpj': company_model.cnpj,
            'numero': company_model.numero,
            'complemento': company_model.complemento,
            'estado': company_model.estado,
            'cep': company_model.cep,
        })
    return HttpResponseNotFound()


def add_contact_action(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        contact_model = Contact(
            nome=data['nome'],
            telefone=data['telefone'],
            celular=data['celular'],
            email=data['email'],
            cargo=data['cargo'],
            departamento=data['departamento'],
            observacao=data['observacao'],
            recebe_email=data['recebe_email'],
        )
        contact_model.save()
        return JsonResponse({
            'id': contact_model.id,
            'nome': contact_model.nome,
            'telefone': contact_model.telefone,
            'celular': contact_model.celular,
            'email': contact_model.email,
            'cargo': contact_model.cargo,
            'departamento': contact_model.departamento,
            'observacao': contact_model.observacao,
            'recebe_email': contact_model.recebe_email,
        })
    return HttpResponseNotFound()


def edit_company_action(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        company_model = Company.objects.get(pk=data['empresa_id'])
        company_model.razao_social = data['razao_social']
        company_model.endereco = data['endereco']
        company_model.bairro = data['bairro']
        company_model.cidade = data['cidade']
        company_model.cnpj = data['cnpj']
        company_model.numero = int(data['numero'])
        company_model.complemento = data['complemento']
        company_model.estado = data['estado']
        company_model.cep = data['cep']
        company_model.save()
        contacts_ids = [c.id for c in company_model.contact_set.all()]
        for contact_id in data['contatos_ids']:
            if contact_id not in contacts_ids:
                contact_model = Contact.objects.get(pk=contact_id)
                contact_model.empresa = company_model
                contact_model.save()
        for contact_id in contacts_ids:
            if contact_id not in data['contatos_ids']:
                contact_model = Contact.objects.get(pk=contact_id)
                contact_model.delete()
        return JsonResponse({
            'id': company_model.id,
            'razao_social': company_model.razao_social,
            'endereco': company_model.endereco,
            'bairro': company_model.bairro,
            'cidade': company_model.cidade,
            'cnpj': company_model.cnpj,
            'numero': company_model.numero,
            'complemento': company_model.complemento,
            'estado': company_model.estado,
            'cep': company_model.cep,
        })
    return HttpResponseNotFound()


def edit_contact_action(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        contact_model = Contact.objects.get(pk=data['contato_id'])
        contact_model.nome = data['nome']
        contact_model.telefone = data['telefone']
        contact_model.celular = data['celular']
        contact_model.email = data['email']
        contact_model.cargo = data['cargo']
        contact_model.departamento = data['departamento']
        contact_model.observacao = data['observacao']
        contact_model.recebe_email = data['recebe_email']
        contact_model.save()
        return JsonResponse({
            'id': contact_model.id,
            'nome': contact_model.nome,
            'telefone': contact_model.telefone,
            'celular': contact_model.celular,
            'email': contact_model.email,
            'cargo': contact_model.cargo,
            'departamento': contact_model.departamento,
            'observacao': contact_model.observacao,
            'recebe_email': contact_model.recebe_email,
        })
    return HttpResponseNotFound()


def delete_company_action(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        company_model = Company.objects.get(pk=data['empresa_id'])
        company_model.delete()
        return JsonResponse({
            'id': data['empresa_id'],
        })
    return HttpResponseNotFound()


def delete_contact_action(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        contact_model = Contact.objects.get(pk=data['contato_id'])
        contact_model.delete()
        return JsonResponse({
            'id': data['contato_id'],
        })
    return HttpResponseNotFound()
