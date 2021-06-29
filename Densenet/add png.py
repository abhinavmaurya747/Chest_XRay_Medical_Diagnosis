import pandas as pd

tr = pd.read_csv('csv/train.csv')
for ind,i in enumerate(tr['Image']):
    if i[:-9] == 'Viral Pneumonia':
        print(i[:-9]+' ('+i[-8:-4]+')'+i[-4:])
        tr.loc[ind,'Image'] = i[:-9]+' ('+i[-8:-4]+')'+i[-4:]
    if i[:-8] == 'Viral Pneumonia':
        print(i[:-8]+' ('+i[-7:-4]+')'+i[-4:])
        tr.loc[ind,'Image'] = i[:-8]+' ('+i[-7:-4]+')'+i[-4:]
    if i[:-7] == 'Viral Pneumonia':
        print(i[:-7]+' ('+i[-6:-4]+')'+i[-4:])
        tr.loc[ind,'Image'] = i[:-7]+' ('+i[-6:-4]+')'+i[-4:]
    if i[:-6] == 'Viral Pneumonia':
        print(i[:-6]+' ('+i[-5:-4]+')'+i[-4:])
        tr.loc[ind,'Image'] = i[:-6]+' ('+i[-5:-4]+')'+i[-4:]
    if i[:-9] == 'NORMAL':
        print(i[:-9]+' ('+i[-8:-4]+')'+i[-4:])
        tr.loc[ind,'Image'] = i[:-9]+' ('+i[-8:-4]+')'+i[-4:]
    if i[:-8] == 'NORMAL':
        print(i[:-8]+' ('+i[-7:-4]+')'+i[-4:])
        tr.loc[ind,'Image'] = i[:-8]+' ('+i[-7:-4]+')'+i[-4:]
    if i[:-7] == 'NORMAL':
        print(i[:-7]+' ('+i[-6:-4]+')'+i[-4:])
        tr.loc[ind,'Image'] = i[:-7]+' ('+i[-6:-4]+')'+i[-4:]
    if i[:-6] == 'NORMAL':
        print(i[:-6]+' ('+i[-5:-4]+')'+i[-4:])
        tr.loc[ind,'Image'] = i[:-6]+' ('+i[-5:-4]+')'+i[-4:]
tr.to_csv('train.csv')


te = pd.read_csv('csv/test.csv')
for ind,i in enumerate(te['Image']):
    if i[:-9] == 'Viral Pneumonia':
        print(i[:-9]+' ('+i[-8:-4]+')'+i[-4:])
        te.loc[ind,'Image'] = i[:-9]+' ('+i[-8:-4]+')'+i[-4:]
    if i[:-8] == 'Viral Pneumonia':
        print(i[:-8]+' ('+i[-7:-4]+')'+i[-4:])
        te.loc[ind,'Image'] = i[:-8]+' ('+i[-7:-4]+')'+i[-4:]
    if i[:-7] == 'Viral Pneumonia':
        print(i[:-7]+' ('+i[-6:-4]+')'+i[-4:])
        te.loc[ind,'Image'] = i[:-7]+' ('+i[-6:-4]+')'+i[-4:]
    if i[:-6] == 'Viral Pneumonia':
        print(i[:-6]+' ('+i[-5:-4]+')'+i[-4:])
        te.loc[ind,'Image'] = i[:-6]+' ('+i[-5:-4]+')'+i[-4:]
    if i[:-9] == 'NORMAL':
        print(i[:-9]+' ('+i[-8:-4]+')'+i[-4:])
        te.loc[ind,'Image'] = i[:-9]+' ('+i[-8:-4]+')'+i[-4:]
    if i[:-8] == 'NORMAL':
        print(i[:-8]+' ('+i[-7:-4]+')'+i[-4:])
        te.loc[ind,'Image'] = i[:-8]+' ('+i[-7:-4]+')'+i[-4:]
    if i[:-7] == 'NORMAL':
        print(i[:-7]+' ('+i[-6:-4]+')'+i[-4:])
        te.loc[ind,'Image'] = i[:-7]+' ('+i[-6:-4]+')'+i[-4:]
    if i[:-6] == 'NORMAL':
        print(i[:-6]+' ('+i[-5:-4]+')'+i[-4:])
        te.loc[ind,'Image'] = i[:-6]+' ('+i[-5:-4]+')'+i[-4:]
te.to_csv('test.csv')

val = pd.read_csv('csv/validation.csv')
for ind,i in enumerate(val['Image']):
    if i[:-9] == 'Viral Pneumonia':
        print(i[:-9]+' ('+i[-8:-4]+')'+i[-4:])
        val.loc[ind,'Image'] = i[:-9]+' ('+i[-8:-4]+')'+i[-4:]
    if i[:-8] == 'Viral Pneumonia':
        print(i[:-8]+' ('+i[-7:-4]+')'+i[-4:])
        val.loc[ind,'Image'] = i[:-8]+' ('+i[-7:-4]+')'+i[-4:]
    if i[:-7] == 'Viral Pneumonia':
        print(i[:-7]+' ('+i[-6:-4]+')'+i[-4:])
        val.loc[ind,'Image'] = i[:-7]+' ('+i[-6:-4]+')'+i[-4:]
    if i[:-6] == 'Viral Pneumonia':
        print(i[:-6]+' ('+i[-5:-4]+')'+i[-4:])
        val.loc[ind,'Image'] = i[:-6]+' ('+i[-5:-4]+')'+i[-4:]
    if i[:-9] == 'NORMAL':
        print(i[:-9]+' ('+i[-8:-4]+')'+i[-4:])
        val.loc[ind,'Image'] = i[:-9]+' ('+i[-8:-4]+')'+i[-4:]
    if i[:-8] == 'NORMAL':
        print(i[:-8]+' ('+i[-7:-4]+')'+i[-4:])
        val.loc[ind,'Image'] = i[:-8]+' ('+i[-7:-4]+')'+i[-4:]
    if i[:-7] == 'NORMAL':
        print(i[:-7]+' ('+i[-6:-4]+')'+i[-4:])
        val.loc[ind,'Image'] = i[:-7]+' ('+i[-6:-4]+')'+i[-4:]
    if i[:-6] == 'NORMAL':
        print(i[:-6]+' ('+i[-5:-4]+')'+i[-4:])
        val.loc[ind,'Image'] = i[:-6]+' ('+i[-5:-4]+')'+i[-4:]
val.to_csv('validation.csv')
