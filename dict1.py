def read_file(filename):
	count = 0
	data =[]
	with open(filename, 'r') as file:
		for line in file:
			data.append(line.strip())
			count += 1
			if count % 50000 == 0:
				print('loading:', count)
	return data


def data_dict(file):
	dict1 ={}
	for line1 in file:
		data_split = line1.split(' ')
		for line2 in data_split:
			if line2 in dict1:
				dict1[line2] += 1
			else:
				dict1[line2] = 1
	return dict1
			

data = read_file('original.txt')
print('增加字典中...')
dict1 = data_dict(data)
while True:
	word = input('想搜尋的字母:')
	if word == 'q':
		break
	else:
		if word in dict1:
			print(dict1[word], '個')
		else:
			print('沒有這個字')