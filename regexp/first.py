 
import re

greedyRegex = re.compile(r'(Ha){3,5}')
match1 = greedyRegex.search('HaHaHaHaHaHaHa')
print(match1.group())

nonGreedyRegex = re.compile(r'(Ha){3,5}?')
match2 = nonGreedyRegex.search('HaHaHaHaHaHaHa')
print(match2.group())
