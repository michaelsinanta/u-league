from example_app.utils import get_user_role
from django.shortcuts import redirect, render

def dashboard(request):
    if request.method == 'GET':
        username = request.COOKIES['username']

        role = get_user_role(username)
        context = {
            'user': {
                'role': f'{role}',
            }
        }

        return render(request, 'dashboard_manajer.html', context)
    
    
