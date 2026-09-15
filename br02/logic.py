from browser import document as D, html as H
from browser import document as D, html as H
from random import shuffle as sh
D <= H.H1("Aknakereső!")
ml = set()
n = 15
m = 10
asz = 26
T = [1]*asz + [0]*(n * m - asz)
sh(T)
def g(e):
    pos = int(e.target.id)
    if pos not in ml:
        e.target <= "📍"
        e.target.classList.add(f"Z")
        ml.add(pos)
    else:
        e.target.clear()
        ml.remove(pos)
        e.target.classList.remove(f"Z")
    e.preventDefault()
nyitva = set()

def f(e):
    megnyit(e.target)


def megnyit(cella):
    pos = int(cella.id)

    if pos in nyitva:
        return

    nyitva.add(pos)

    if T[pos]:
        cella <= "💣"
        cella.classList.add("Z")
        return

    y = pos // n
    x = pos % n

    asz = 0

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue

            yy = y + dy
            xx = x + dx

            if 0 <= yy < m and 0 <= xx < n:
                asz += T[yy * n + xx]

    cella <= asz
    cella.classList.add(f"X{asz}")

    if asz == 0:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                yy = y + dy
                xx = x + dx

                if 0 <= yy < m and 0 <= xx < n:
                    megnyit(D[str(yy * n + xx)])
D <= H.TABLE([H.TR(
    H.TD("", id=f"{j * n + i}")
        .bind("click", f)
        .bind("contextmenu", g)
        for i in range(n)
) for j in range(m)])