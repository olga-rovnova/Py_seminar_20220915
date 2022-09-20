# 1.Напишите программу, удаляющую из текста все слова, содержащие "абв". 

# f = open('task1.txt', 'a')
# f.write('\nwriteabc a program deleting all words with "abc"\n')
# f.close

f = open('task1.txt', 'rt')
line = f.readlines()
f.close
print(line)

line1 = str(line)
lst = list(line1.split()) 
print(lst) 
lst = list(filter(lambda x: 'abc' not in x, lst)) 
print(' '.join(lst))
with open('task1_1.txt', 'w') as res:
    res.write(' '.join(lst))
