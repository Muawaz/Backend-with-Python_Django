from django.http import HttpResponse
from django.template import loader
from .models import Users

def user_view(request):
    user_view_list = Users.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'user_list': user_view_list,
    }

    return HttpResponse(template.render(context, request))

def user_details(request, id):
    user_detail_list = Users.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'detail_list': user_detail_list,
    }

    return HttpResponse(template.render(context, request))
