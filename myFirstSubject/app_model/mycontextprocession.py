from .models import MyUser

def myuser(request):
    myuser = request.session.get('username','null')
    if myuser != 'null':
        return {'username':myuser}
    else:
        return {'username':'未登录'}