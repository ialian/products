import os # operating system

products = []
if os.path.isfile('products.csv'): # 檢查檔案在不在
	print('找到目標檔案')

	# 讀取檔案
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續,跳到下一迴()
			name, price = line.strip().split(',') # split(',')就是遇到','就切一刀下去變成兩個欄位
			products.append([name, price])
	print(products)

else:
	print('找不到檔案.....')

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':      #quit
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	# p = []
	# p.append(name)
	# p.append(price)
	p = [name, price]
	products.append(p)
	# products.append([name, price]) 更簡潔
print(products)
# products[0][0]

# 印出購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')   # csv檔可以用,來區隔欄位