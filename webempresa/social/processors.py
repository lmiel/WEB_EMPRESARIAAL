from .models import Link

def ctx_dict(request):
    # Consulta todos los objetos de Link
    links = Link.objects.all()
    
    # Inicializa el contexto con valores iniciales
    ctx = {'test': 'hola'}
    
    # Agrega las claves y URLs al contexto
    for link in links:
        ctx[link.key] = link.url
    
    return ctx
