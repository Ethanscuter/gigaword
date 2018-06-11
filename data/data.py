"""
This is a preprocessed code on raw Gigaword Dataset.

Parameters:
    Datafile path: ./datafiles

Returns:
    The same format of CNN/DM, which use the code of https://github.com/abisee/pointer-generator
"""

import os

'''
func: use extraction to filter the noise data and split the file into valid set and test set respect.
'''
def extraction(filename1, filename2):
    with open(filename1) as file_object:
        lines_title = file_object.readlines()

    with open(filename2) as file_object:
        lines_article = file_object.readlines()

    title = []
    article = []

    for line in lines_title:
        line = line.split()
        title.append(line)

    for line in lines_article:
        line = line.split()
        article.append(line)

    data_title = []
    data_article = []

    for i in range(len(title)):
        if len(title[i]) > 12:
            data_title.append(title[i])
            data_article.append(article[i])

    filename_test = './datafiles/test.article.txt'
    filename_valid = './datafiles/valid.article.txt'

    data_article_test = data_article[0:2000]
    data_article_valid = data_article[2000:]

    with open(filename_test, 'w') as file_object:
        for i in range(len(data_article_test)):
            line = ''
            for j in range(len(data_article_test[i])):
                line = line + ' ' + data_article_test[i][j]
                line = line.strip()
            file_object.write(line + '\n')

    with open(filename_valid, 'w') as file_object:
        for i in range(len(data_article_valid)):
            line = ''
            for j in range(len(data_article_valid[i])):
                line = line + ' ' + data_article_valid[i][j]
                line = line.strip()
            file_object.write(line + '\n')

    filename_test = './datafiles/test.title.txt'
    filename_valid = './datafiles/valid.title.txt'

    data_title_test = data_title[0:2000]
    data_title_valid = data_title[2000:]

    with open(filename_test, 'w') as file_object:
        for i in range(len(data_title_test)):
            line = ''
            for j in range(len(data_title_test[i])):
                line = line + ' ' + data_title_test[i][j]
                line = line.strip()
            file_object.write(line + '\n')

    with open(filename_valid, 'w') as file_object:
        for i in range(len(data_title_valid)):
            line = ''
            for j in range(len(data_title_valid[i])):
                line = line + ' ' + data_title_valid[i][j]
                line = line.strip()
            file_object.write(line + '\n')

'''
func: use process function to reformat the train/valid/test files to the format abisee code can process.
'''
def process(filename1, filename2, mode):
    with open(filename1) as file_object:
        lines_title = file_object.readlines()

    with open(filename2) as file_object:
        lines_article = file_object.readlines()

    data_title = []
    data_article = []

    for line in lines_title:
        line = line.strip()
        data_title.append(line)

    for line in lines_article:
        line = line.strip()
        data_article.append(line)

    idx = 0
    file_idx = []
    if mode == 'train':
        if not os.path.exists('./train'): os.makedirs('./train')
        for idc in range(len(lines_title)):
            filename = './train/' + str(idx) + '.train' + '.story'
            filename_idx = str(idx) + '.train' + '.story'
            file_idx.append(filename_idx)
            with open(filename, 'w') as file_object:
                file_object.write(data_article[idx] + '\n')
                file_object.write('\n')
                file_object.write('@highlight' + '\n')
                file_object.write('\n')
                file_object.write(data_title[idx] + '\n')
                idx += 1
            if idc % 5000 == 0:
                print('Writing the %d file.' % idc)

        with open('./lists/all_train.txt', 'w') as file_object:
            for file_ in file_idx:
                file_object.write(file_ + '\n')

    elif mode == 'valid':
        if not os.path.exists('./valid'): os.makedirs('./valid')
        for idc in range(len(lines_title)):
            filename = './valid/' + str(idx) + '.valid' + '.story'
            filename_idx = str(idx) + '.valid' + '.story'
            file_idx.append(filename_idx)
            with open(filename, 'w') as file_object:
                file_object.write(data_article[idx] + '\n')
                file_object.write('\n')
                file_object.write('@highlight' + '\n')
                file_object.write('\n')
                file_object.write(data_title[idx] + '\n')
                idx += 1
            if idc % 5000 == 0:
                print('Writing the %d file.' % idc)

        with open('./lists/all_valid.txt', 'w') as file_object:
            for file_ in file_idx:
                file_object.write(file_ + '\n')
    else:
        if not os.path.exists('./test'): os.makedirs('./test')
        for idc in range(len(lines_title)):
            filename = './test/' + str(idx) + '.test' + '.story'
            filename_idx = str(idx) + '.test' + '.story'
            file_idx.append(filename_idx)
            with open(filename, 'w') as file_object:
                file_object.write(data_article[idx] + '\n')
                file_object.write('\n')
                file_object.write('@highlight' + '\n')
                file_object.write('\n')
                file_object.write(data_title[idx] + '\n')
                idx += 1
            if idc % 5000 == 0:
                print('Writing the %d file.' % idc)

        with open('./lists/all_test.txt', 'w') as file_object:
            for file_ in file_idx:
                file_object.write(file_ + '\n')



if __name__ == '__main__':
    # Split the filter files into validation set and test set
    filename_title = './datafiles/title.filter.txt'
    filename_article = './datafiles/article.filter.txt'
    extraction(filename_title, filename_article)
    # Process the training set
    filename1 = './datafiles/train.title.txt'
    filename2 = './datafiles/train.article.txt'
    mode = 'train'
    print('Start processing the training data.')
    process(filename1, filename2, mode)
    # Process the validation set
    filename1 = './datafiles/valid.title.txt'
    filename2 = './datafiles/valid.article.txt'
    mode = 'valid'
    print('Start processing the validation data.')
    process(filename1, filename2, mode)
    # Process the test set
    filename1 = './datafiles/test.title.txt'
    filename2 = './datafiles/test.article.txt'
    mode = 'test'
    print('Start processing the test data.')
    process(filename1, filename2, mode)
    print('Processing finished.')
