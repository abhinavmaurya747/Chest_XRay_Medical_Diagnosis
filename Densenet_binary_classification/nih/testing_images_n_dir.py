import pandas as pd 
import os

files = os.listdir('images')

test = pd.read_csv('test.csv')
test = list(test['Image'])
#print(test)

for i in test:
	if i in files:
		pass
	else:
		print('error : ',i)

test = pd.read_csv('train.csv')
test = list(test['Image'])
#print(test)

for i in test:
	if i in files:
		pass
	else:
		print('error : ',i)


test = pd.read_csv('validation.csv')
test = list(test['Image'])
#print(test)

for i in test:
	if i in files:
		pass
	else:
		print('error : ', i)

