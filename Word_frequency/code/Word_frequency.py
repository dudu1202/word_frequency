#!/usr/bin/env.python
# -*- coding: utf-8 -*-
import string
import operator
import matplotlib.pyplot as plt


def get_word_list(file_name):
    # 打开文件，切分得到词汇列表
    res = []
    file = open(file_name, 'r').readlines()
    for line in file:
        file2 = line.strip().split(' ')
        for item in file2:
            item2 = item.strip(string.punctuation)
            if len(item2) >= 1:
                res.append(item)
    return res


def cut_word(k, word_list):
    # 对词汇列表进行词汇计数
    result = {}
    for i in word_list:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    word = sorted(result.items(), key=operator.itemgetter(1), reverse=True)  # 降序排序
    result = word[:k]
    return result


def draw_photo(result):
    # 画出前k个频率最高的词汇
    num = []
    word = []
    for x, y in result:
        num.append(x)
        word.append(y)
    plt.bar(num, height=word, alpha=0.8, color=['r', 'g', 'b', 'y', 'm', 'c', 'g'])
    # y轴数值序列就是词出现的次数，透明度为0.8
    plt.title('Word frequency')
    plt.show()


def main():
    k = int(input('请输入要查看排名在前多少位的词汇:'))
    file_name = 'test.txt'
    word_list = get_word_list(file_name)
    result = cut_word(k, word_list)
    draw_photo(result)


main()
