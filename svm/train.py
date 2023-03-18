import pickle
def read_csv(filename):
    with open(filename) as f:
        return f.read().splitlines()

oasis_input_list=read_csv('data/oasis+_dev_99.csv')
print(oasis_input_list[0])
def num(s):
    if s=='':
        return -9
    try:
        return int(s)
    except ValueError:
        return float(s)
data=[o[0:-2].split(',') for o in oasis_input_list]
labels=[o[-1] for o in oasis_input_list]
converted_data=[]
for d in data:
    num_arrray=[]
    for each_num in d:
        n=num(each_num)
        num_arrray.append(n)
    converted_data.append(num_arrray)
print(converted_data[0])
print(labels[0])
from sklearn import svm
X = converted_data
y = labels
clf = svm.SVC()
clf.fit(X, y)
def save_model(model, filename):
    with open(filename, 'wb') as f:
        pickle.dump(model, f)
save_model(clf,'svm/svm_model_99.pkl')