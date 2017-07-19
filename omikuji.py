#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import numpy as np

def puts(i):
	print (i)
	return i

def chunked(iterable, n):
    return [iterable[x:x + n] for x in range(0, len(iterable), n)]

def omikuji():
	t = ["t1","t2","t3","t4"]
	m2 = ["m2_1","m2_2","m2_3","m2_4","m2_5","m2_6","m2_7","m2_8","m2_9"]
	m1 = ["m1_1","m1_2","m1_3","m1_4","m1_5","m1_6","m1_7","m1_8","m1_9"]
	b4 = ["b4_1","b4_2","b4_3","b4_4","b4_5","b4_6","b4_7","b4_8","b4_9"]
	g = [[0 for i in range(10)] for j in range(4)]
	m2_n = len(m2)/len(t)
	m1_n = len(m1)/len(t)
	b4_n = len(b4)/len(t)
	
	random.shuffle(m2)
	m2 = chunked(m2,m2_n)
	random.shuffle(m1)
	m1 = chunked(m1,m1_n)
	random.shuffle(b4)
	b4 = chunked(b4,b4_n)
	#print (m2)
	#print (m1)
	#print (b4)
	
	for i in range(0, len(t)):
		g[i] = [t[i]] + m2[i] + m1[i] + b4[i]
		# print(g[i])

	a = len(t)
	amari = m2[a]+m1[a]+b4[a]
	i1=0
	for i in amari:
		g[i1].append(i)
		i1=i1+1
		i1 = i1%len(t)
	for i in range(len(t)):
		puts(g[i])

omikuji()