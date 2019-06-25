Text = []
print("Введите элементы списка: ")
while True:
    k = input()
    if (k == ""):
        break
    else:
        Text.append(k)
Text.reverse()
Text1 = Text
t = [] + Text
dlina = len(Text)
while (dlina > 0):
    Text1.pop()
    dlina = dlina-1
    t = t + Text1
print(t)









