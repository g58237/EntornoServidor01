from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registro(request):
    
    contexto = {
        'nombre': '',
        'curso': '',
        'email': '',
        'enviado': False,
    }
    if request.method == 'POST':
        contexto['nombre'] = request.POST.get('nombre', '')
        contexto['curso'] = request.POST.get('curso', '')
        contexto['email'] = request.POST.get('email', '')
        contexto['enviado'] = True

    return render (request, 'registro.html', contexto)

def tecnologias(request):
    lista = {
        'Python': 'Lenguaje de programación de alto nivel y es de tipo dinámico.',
        'Django': 'Framework web de Python.',
        'HTML': 'Lenguaje de marcado para estructurar el contenido de una página web.',
        'CSS': 'Hojas de estilo en cascada. Sirve para dar diseño a una estructura hecha con HTML.',
        'VS Code': 'Es un IDE de código abierto usado para hacer aplicaciones con muchos lenguajes de programación (Python, JavaScript, etc.).'
    }
    return render(request, 'tecnologias.html', {'lista': lista})

def calculadora(request):
    resultado = None
    if request.method == 'POST':
        a = int(request.POST.get('a', 0))
        b = int(request.POST.get('b', 0))
        op = request.POST.get('op')
        if op == 'suma':
            resultado = a + b
        elif op == 'resta':
            resultado = a - b
        elif op == 'multi':
            resultado = a * b
        elif op == 'div' and b != 0:
            resultado = a / b
    return render(request, 'calculadora.html', {'resultado': resultado})            
