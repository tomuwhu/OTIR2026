from browser import document as D, html as H
from random import randrange as rand
p = 1
oszpsz = [0, 0]
b = 0
j = 19
Z = H.DIV()
def f(e):
    global j, b, p
    sz = int(e.target.id)
    ém = False
    if sz == b:
        b += 1
        ém = True
    if sz == j:
        j -= 1
        ém = True
    if ém:
        oszpsz[p] += int(e.target.innerHTML)
        p = 0 if p else 1
        e.target.clear()
        e.target.classList.add("O")
        Z.clear()
        Z <= [H.DIV(i) for i in oszpsz]
D <= H.H1("Számjáték")
l = [[rand(1,30),j] for i, j in enumerate(range(20))]
D <= H.TABLE(H.TR(H.TD(x[0], id=f"{x[1]}", Class=f"p{x[1] % 2}").bind("click", f) for x in l))
D <= Z