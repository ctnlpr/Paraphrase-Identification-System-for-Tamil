

def get_data(text_file, label_file):
    read_file = open(text_file, 'r+')
    pair_1 = []
    pair_2 = []
    i = 0
    for line in read_file:
        line = line.replace('\n','')
        while '  ' in line:
            line = line.replace('  ', ' ')
        if i%2 == 0:
            pair_1.append(line)
        else:
            pair_2.append(line)
        i += 1
    read_file.close()
    labels = []
    read_file = open(label_file, 'r+')
    for line in read_file:
        line = line.replace('\n','')
        labels.append(int(line))
    read_file.close()
    return pair_1, pair_2, labels
