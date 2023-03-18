def read_csv(filename):
    with open(filename) as f:
        return f.read().splitlines()

test_input=read_csv('Oasis+Dev.csv')
features=test_input[0].split(',')
for i in range(len(features)):
    print(i,features[i])

    
def prep_data(data):
    # remove the header
    data = data[1:]
    # split the data
    data = [row.split(',') for row in data]
    # convert the data to a list of dictionaries
    return data
labels=[]
data=[]
for d in prep_data(test_input):
    labels.append(d[35])
    datum=d[5]+','+d[7]+','+d[9]+','+d[11]+','+d[13]+','+d[15]+','+d[17]+','+d[19]+','+d[21]+','+d[23]
    data.append(datum)

def account_label(labels):
    # count the number of each label
    label_counts = {}
    for label in labels:
        if label not in label_counts:
            label_counts[label] = 0
        label_counts[label] += 1
    return label_counts

label_counts=account_label(labels)
print(label_counts)

def write_data(data, labels,filename):
    with open(filename, 'w') as f:
        for i in range(len(data)):
            print(data[i],labels[i])
            f.write(data[i]+','+labels[i]+'\n')

write_data(data,labels,'oasis+_dev.csv')