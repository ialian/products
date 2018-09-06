
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':      #quit
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price)
	# 也可以寫 p = [name, price]
	products.append(p)
	# products.append([name, price]) 更簡潔
print(products)
# products[0][0]

for p in products:
	print(p[0], '的價格是', p[1])
