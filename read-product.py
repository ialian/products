#讀取檔案

products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #繼續,跳到下一迴()
		name, price = line.strip().split(',') # split(',')就是遇到','就切一刀下去變成兩個欄位
		products.append([name, price])
print(products)

# continue 跟break一樣 只能寫在迴圈裡
# continue 就是跳到下一迴的意思(下一輪)