from django.utils.deprecation import MiddlewareMixin

class MyExpression(MiddlewareMixin):
    def process_request(self,request):
        print('process_request')
        return None

    def process_view(self,request,callback,callback_args,callback_kwargs):
        print('process_view')
        return None
    #
    def process_template_response(self,request,response):
        print('process_template_response')
        return None
    #
    def process_response(self,request,reponse):
        print('process_response')
        return reponse
    #
    def process_exception(self,request,excetion):
        print('process_exception')
        return excetion

class UserMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        username = request.session.get('username','null')
        print('request')
        if username:
            setattr(request,'username',username)
        response = self.get_response(request)
        print('response')
        return response