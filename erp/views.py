from django.shortcuts import render, redirect

def home(request):
    return render(request, 'html/home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Autenticar al usuario utilizando el correo electrónico y la contraseña
        # ...

        return redirect('erp:menu')

    return render(request, 'html/login.html')

def menu_view(request):
    return render(request, 'html/menu.html')

def procesar_formulario(request):
    return redirect('erp:menu')
