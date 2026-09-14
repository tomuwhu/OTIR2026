from browser import document as D, html as H
D <= H.H1("Hello World!")
D <= H.TABLE(H.TR(H.TD(f"{i*j}") for i in range(10)) for j in range(5))