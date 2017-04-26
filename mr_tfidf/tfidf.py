#!/usr/bin/python

import os
import sys
import gzip

file_input_fd = sys.argv[1]
idf_dict_fd = sys.argv[2]

def get_file_handler(f):
    file_in = open(f, 'r')
    return file_in

idf_map = {}
for line in get_file_handler(idf_dict_fd):
    ss = line.strip().split('\t')
    if len(ss) != 2:
        continue
    word = ss[0].strip()
    idf = ss[1].strip()
    idf_map[word] = float(idf)

for line in get_file_handler(file_input_fd):
    ss = line.strip().split('\t')
    if len(ss) != 2:
        continue

    docid = ss[0].strip()
    context = ss[1].strip()
    tf_map = {}
    for t_word in context.strip().split(' '):
        if t_word not in tf_map:
            tf_map[t_word] = 0
        tf_map[t_word] += 1

    tfidf_map = {}
    for w, tf in tf_map.items():
        if w not in idf_map:
            continue
        idf = idf_map[w]
        tfidf_score = tf * idf
        tfidf_map[w] = tfidf_score

    tmp_list = []
    for key, val in tfidf_map.items():
        tmp_list.append((key, val))
    final_list = sorted(tmp_list, key=lambda x : x[1], reverse=True)[:5]

    word_score_list = []
    for t in final_list:
        word_score_list.append(':'.join([t[0], str(t[1])]))

    print docid + '\t' + ','.join(word_score_list)




