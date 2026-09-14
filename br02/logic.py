from browser import document as D, html as H
from random import shuffle as sh
D <= H.H1("Aknakereső!")
n = 15
m = 10
asz = 26
T = [1]*asz + [0]*(n * m - asz)
sh(T)
def g(e):
    e.target <= "Z"
    e.preventDefault()
    e.target.classList.add("Z")
def f(e):
    e.target.clear()
    pos = int(e.target.id)

    if T[pos]:
        e.target <= "B"
    else:
        x = pos % n
        y = pos // n

        asz = 0

        for dx, dy in [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1),           (0, 1),
                       (1, -1),  (1, 0),  (1, 1)]:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m:
                asz += T[ny * n + nx]

        e.target <= asz
        e.target.classList.add(f"X{asz}")

D <= H.TABLE([H.TR(
    H.TD("", id=f"{j * n + i}")
        .bind("click", f)
        .bind("contextmenu", g)
        for i in range(n)
) for j in range(m)])