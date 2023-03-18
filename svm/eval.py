import pickle
from sklearn import svm
def load_model(filename):
    with open(filename, 'rb') as f:
        model = pickle.load(f)
    return model
clf=load_model('svm/svm_model_999.pkl')
print(clf.predict([[19,0,15,176,49,30.5,39.28,5535,1,0]]))