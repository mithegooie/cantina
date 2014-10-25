from django.shortcuts import render, render_to_response
from payments.models import User

# Create your views here.

def index(request):
    uid = request.session.get('user')
    if uid is None:
        return render_to_response('main/index.html')
    else:
        return render_to_response(
            'main/user.html',
            {'user': User.get_by_id(uid)}
        )