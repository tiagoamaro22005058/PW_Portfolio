def is_gestor(request):
    return {
        'is_gestor': request.user.is_authenticated and request.user.groups.filter(name='gestor-portfolio').exists()
    }
