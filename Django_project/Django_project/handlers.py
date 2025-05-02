from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.http import require_http_methods
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

import json
import bcrypt

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

@require_http_methods(["POST"])
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

@require_http_methods(["GET"])
def get_products(request):
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
    
    products = [{"name" : "", "description" : ""},{"name" : "", "description" : ""},{"name" : "", "description" : ""},{"name" : "", "description" : ""}] # тут тип берем продукты из бд
    return JsonResponse(products, safe= False)

@require_http_methods(["GET"])
def get_category_page(request):
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

    input_data = request.GET
    print(input_data)
    category_id = input_data["cat_id"] if "cat_id" in input_data else None
    if category_id is None:
        return JsonResponse({"ERROR" : "no category specified"})
    cat_page_data = {"id" : category_id, "name" : "", "description" : ""} # тут тип берем профиль из бд
    
    return JsonResponse(cat_page_data)

@require_http_methods(["GET"])
def search(request):
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

    input_data = request.GET
    print(input_data)
    quiery = input_data["q"] if "q" in input_data else None
    if quiery is None:
        return JsonResponse({"ERROR" : "no quiery specified"})
    quiery = quiery.lower()
    # сам поиск
    found_users = []
    found_products = []
    with connection.cursor() as cursor:
        # 1. по пользователям
        cursor.execute(f"SELECT * FROM users WHERE LOWER(username) LIKE '%{quiery}%' OR LOWER(name_first) LIKE '%{quiery}%' OR LOWER(name_last) LIKE '%{quiery}%';")
        rows = cursor.fetchall()
        found_users += [{'id' : elm[0], 'uname' : elm[1], 'first_name' : elm[4], 'last_name' : elm[5]} for elm in rows]
        # 2. по продуктам
        cursor.execute(f"SELECT * FROM products WHERE LOWER(name) LIKE '%{quiery}%';")
        rows = cursor.fetchall()
        found_products += [{'id' : elm[0], 'name' : elm[1], 'price' : elm[2], 'amount' : elm[3]} for elm in rows]

    result_data = {"users" : found_users, "products" : found_products} # тут тип берем профиль из бд
    return JsonResponse(result_data)

@require_http_methods(["GET"])
def get_all(request):
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

    # сам поиск
    all_users = []
    all_products = []
    all_baskets = []
    with connection.cursor() as cursor:
        # 1. по пользователям
        cursor.execute(f"SELECT * FROM users;")
        rows = cursor.fetchall()
        all_users += [{'id' : elm[0], 'uname' : elm[1], 'first_name' : elm[4], 'last_name' : elm[5]} for elm in rows]
        # 2. по продуктам
        cursor.execute(f"SELECT * FROM products;")
        rows = cursor.fetchall()
        all_products += [{'id' : elm[0], 'name' : elm[1], 'price' : elm[2], 'amount' : elm[3]} for elm in rows]
        # 2. по корзинам
        cursor.execute(f"SELECT * FROM baskets;")
        rows = cursor.fetchall()
        all_baskets += [{'id' : elm[0], 'owner_id' : elm[1], 'opened' : elm[2], 'closed' : elm[3]} for elm in rows]

    result_data = {"users" : all_users, "products" : all_products, 'baskets' : all_baskets} # тут тип берем профиль из бд
    return JsonResponse(result_data)

@csrf_exempt
@require_http_methods(["POST"])
def add_entitiy(request):
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
    
    input_data = json.loads(request.body)
    print(input_data)
    e_type = input_data["e_type"] if "e_type" in input_data else None
    if e_type == "user":
        user_name = input_data["user_name"] if "user_name" in input_data else None
        user_password = input_data["user_password"] if "user_password" in input_data else None
        name_first = input_data["name_first"] if "name_first" in input_data else None
        name_last = input_data["name_last"] if "name_last" in input_data else None

        with connection.cursor() as cursor:
            # проверка, не занято ли имя
            cursor.execute(f"SELECT id FROM users WHERE username= '{user_name}';")
            if len(cursor.fetchall()) != 0:
                return JsonResponse("ERROR", "user name unavailable")
            # запись
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(user_password.encode('utf-8'), salt).decode('utf-8')
            cursor.execute(f"INSERT INTO users (username, pword_hash, pword_salt, name_first, name_last)\
                                VALUES {user_name, password_hash, salt.decode('utf-8'), name_first, name_last};")
            connection.commit()
            cursor.execute("SELECT id FROM users ORDER BY id desc limit 1")
            uid = cursor.fetchall()[0][0]

            result = {"RESULT" : "OK", "new_id" : uid}
    elif e_type == "product":
        product_name = input_data["product_name"] if "product_name" in input_data else None
        product_price = input_data["product_price"] if "product_price" in input_data else None
        product_amount = input_data["product_amount"] if "product_amount" in input_data else None

        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO products (name, price, amount)\
                                VALUES {product_name, product_price, product_amount};")
            connection.commit()
            cursor.execute("SELECT id FROM products ORDER BY id desc limit 1")
            pid = cursor.fetchall()[0][0]

            result = {"RESULT" : "OK", "new_id" : pid}
    else:
        result = {"RESULT" : "WRONG ETYPE"}
    return JsonResponse(result)