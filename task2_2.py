# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

value = int(input("Введите количество конфет на столе: "))
set_max = int(input("Введите максимальное количество конфет, которое можно взять за один ход : "))
res = set_max + 1
step_one = value % res
print(f"Чтобы выиграть, первый игрок в первый ход должен взять: {step_one} конфет")