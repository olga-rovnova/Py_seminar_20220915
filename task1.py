# 1.Напишите программу, удаляющую из текста все слова, содержащие "абв". 

# f = open('task1.txt', 'a')
# f.writelines('writeabc a program deleting all words with "abc"')
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