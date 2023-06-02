from django.shortcuts import render

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.core.serializers.json import DjangoJSONEncoder

# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    response.set_cookie("us", "username")
    return response

# получение куки
def get(request):
    # получаем куки с ключом username
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")

def index(request):
    bob = Person("Bobby", 416)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)
 
class Person:
  
    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = age        # возраст человека
 
class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
            # return obj.__dict__
        return super().default(obj)


# def index(request):
#      return JsonResponse({"name": "Tom", "age": 38})
 
def about(request):
    return HttpResponse("About")
 
def contact(request):
    return HttpResponseRedirect("/about")
 
def details(request):
    return HttpResponsePermanentRedirect("/")

# def index(request):
#     host = request.META["HTTP_HOST"]
#     user_agent = request.META["HTTP_USER_AGENT"]
#     sh = request.scheme
#     body = request.body
#     m = request.method
#     e = request.encoding
#     ct = request.content_type
#     G = request.GET
#     P = request.POST
#     C = request.COOKIES
#     F = request.FILES
#     h = request.headers
#     fp = request.get_full_path()
#     gh = request.get_host()
#     gp = request.get_port()

#     return HttpResponse(f"""
#                         <p>    host = {request.META["HTTP_HOST"]} </br>
#     user_agent = {request.META["HTTP_USER_AGENT"]} </br>
#     sh = {request.scheme}</br>
#     body = {request.body}</br>
#     m = {request.method}</br>
#     e = {request.encoding}</br>
#     ct = {request.content_type}</br>
#     G = {request.GET}</br>
#     P = {request.POST}</br>
#     C = {request.COOKIES}</br>
#     F = {request.FILES}</br>
#         fp = {request.get_full_path()}</br>
#     gh = {request.get_host()}</br>
#     gp = {request.get_port()}
#     </p>
#                         """)

# def about(request, name, age):
#     return HttpResponse(f"""
#                         <h2>About SQL!!!</h2>
#                         <p>Name: {name}</p>
#                         <p>Age:{age}</p>
                        
                        
#     """)

# def contact(request):
#     return HttpResponse('Contact SQL!!!',status=400, reason="Incorrect data")

# def user(request):
#         age = request.GET.get('age', 0)
#         name = request.GET.get('name', 'unknown')
#         return HttpResponse(f"""
#                         <h2>About user:</h2>
#                         <p>Name: {name}</p>
#                         <p>Age:{age}</p>

                        
                        

#     """)


# def old_cat(request, id):
#      return HttpResponse(f'old_cats {id}')

# def new_cat(request, id):
#      return HttpResponse(f'new_cats {id}')

# def cat(request, id):
#      return HttpResponse(f'all_cats {id}')