from django.http import JsonResponse
from datetime import datetime

def verify_password(user_id, password_hash):
    # заглушка для проверки пароля
    verification_token = 0
    return verification_token

def verify_user(user_id, verification_token):
    # заглушка для проверки токена
    return verification_token == 0

def test(request):
    method = request.method
    host = request.META["HTTP_HOST"] # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
    path = request.path     # получаем запрошенный путь
    print("======================")
    print(datetime.now())
    print(method)
    print(host)
    print(user_agent)
    print(path)
    print("======================")
    if request.method == "POST":
        return JsonResponse({"ERROR" : "wrong method"})
    print(request.GET)
    return JsonResponse("this is test url", safe = False)

def get_user_profile(request):
    # заглушка для получения профиля
    method = request.method
    host = request.META["HTTP_HOST"] # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
    path = request.path     # получаем запрошенный путь
    print("======================")
    print(datetime.now())
    print(method)
    print(host)
    print(user_agent)
    print(path)
    print("======================")
    if request.method == "GET":
        return JsonResponse({"ERROR" : "wrong method"})
    input_data = request.POST
    print(input_data)
    user_id = input_data["user_id"] if "user_id" in input_data else None
    verification_token = input_data["token"] if "token" in input_data else -1
    if user_id == None:
        return JsonResponse({"ERROR" : "no user id provided"})
    verified = verify_user(user_id, verification_token)
    if not verified:
        return JsonResponse({"ERROR" : "verification error"})
    profile = {"name" : "", "description" : ""} # тут тип берем профиль из бд
    return JsonResponse(profile)
