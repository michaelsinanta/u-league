from example_app.utils import get_user_role
from django.shortcuts import redirect, render

def dashboard(request):
    username = request.COOKIES.get('username', None)

    if username is None:
        return render(request, 'landing_page.html', {}) 

    role = get_user_role(username)
    context = {
        'user': {
            'role': f'{role}',
        }
    }

    if role == "Manajer":
        return render(request, 'dashboard_manajer.html', context)
    elif role == "Panitia":
        return render(request, 'dashboard_panitia.html', context)
    elif role == "Penonton":
        return render(request, 'dashboard_penonton.html', context)
    else :
        return render(request, 'landing_page.html')
    
    
