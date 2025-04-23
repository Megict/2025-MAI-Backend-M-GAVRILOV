import random
 
def app(environ, start_response):
	data = ""
	# задаем начальные множества
	alphabet = "qwertyuiopasdfghjklzxcvbnm"
	numbers = "1234567890"
	symbols = "#.,!@&^%"
	# задаем множества для выбора
	datavar = {}
	datavar["let"] = list(alphabet)
	datavar["LET"] = list(alphabet.upper())
	datavar["num"] = list(numbers)
	datavar["sym"] = list(symbols)
	# случайно выбираем длину
	datalen = random.randrange(8,17)
	# случайно строим карту пароля
	variation = []
	att_ind = 0
	while len(set(variation)) != 4: # если не присутствуют элементы каждого множества, то переделываем
		att_ind += 1
		variation = random.choices(["let","LET","num","sym"], k = datalen)
	# генерируем сам пароль
	for i in range(datalen):
		data += random.choice(datavar[variation[i]])
	print("--------------")
	print(f"password: {data}")
	print(f"variation: {variation}")
	print(f"len: {datalen}")
	print(f"took {att_ind} attempts")
	print("--------------")
	data = str.encode(data)

	start_response("200 OK", [
		("Content-Type", "text/plain"),
		("Content-Length", str(len(data)))
	])

	return iter([data])
