from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from app.models import Artigos, Comissao, Edicoes, Normas, Textos, Areas
from .forms import Form


def inicio(request):
    anais = Artigos.objects.all()
    form = Form()
    context = {
        "tabela": anais,
        "form": form,
    }
    return render(request, "admin/admin.html", context)


def comissao(request):
    comissao = Comissao.objects.all()
    context = {"tabela": comissao}
    return render(request, "admin/comissao-admin.html", context)


def edicoes(request):
    edicoes = Edicoes.objects.all()
    context = {"tabela": edicoes}
    return render(request, "admin/edicoes-admin.html", context)


def normas(request):
    normas = Normas.objects.all()
    context = {"tabela": normas}
    return render(request, "admin/normas-admin.html", context)


def textos(request):
    textos = Textos.objects.all()
    context = {"tabela": textos}
    return render(request, "admin/textos-admin.html", context)


def eixos(request):
    eixos = Areas.objects.all()
    context = {"tabela": eixos}
    return render(request, "admin/eixos-admin.html", context)


def Add(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("areadmin")
    context = {
        "form": form,
    }
    return redirect("admin.html", context)


def Update(request, id):
    alt = get_object_or_404(Artigos, id=id)

    if request.method == "GET":
        context = {"formulario": Form(instance=alt), "id": id}
        return render(request, "admin.html", context)

    elif request.method == "POST":
        form = Form(request.POST, instance=alt)
        if form.is_valid():
            form.save()
            return redirect("areadmin")
    else:
        messages.error(request, "Por favor faça os passos.")
        return render(request, "admin.html", {"formulario": form})
    return redirect(request, "admin.html", context)


def Delete(request, id):
    anais = Artigos.objects.filter(id=id)
    anais.delete()
    return redirect("areadmin")
