#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt			# 导入模块

years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
turnovers = [0.5, 9.36, 52, 191, 350, 571, 912, 1027, 1682, 2135, 2684]
plt.figure()
plt.scatter(years, turnovers, c='red', s=100, label='legend')
plt.xticks(range(2008, 2020, 3))
plt.yticks(range(0, 3200, 800))
plt.xlabel("Year", fontdict={'size': 16})
plt.ylabel("number", fontdict={'size': 16})
plt.title("Title", fontdict={'size': 20})
plt.legend(loc='best')
plt.show()