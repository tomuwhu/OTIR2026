from browser import document as D, html as H
from random import shuffle as sh
D <= H.H1("Lottó nyerőszámok")
l = list(range(1, 91))
sh(l)
D <= H.TABLE(H.TR(H.TD(i) for i in sorted(l[0:5])))
