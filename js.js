var t
let next = "X"
let go
setTimeout(() => f(), 100)
function f() {
    go = false
    t = Array(10).fill(0).map(() => Array(15).fill(0))
    document.getElementById("x1").innerHTML = `
        <table>
        ${t.map((v, j) => `
            <tr>
                ${v.map((x, i) => `<td 
                    id="${j}-${i}"
                    onclick="g(${i},${j})"></td>`).join("")}
            </tr>`).join("")}
        </table>
    `
}
function g(x, y) {
    let player = next
    let clickedcell = document.getElementById(`${y}-${x}`)
    if (clickedcell.innerHTML == "" &&!go) {
        t[y][x] = next
        clickedcell.innerHTML = next
        clickedcell.classList.add(next);
        [[0, 1], [1, 0], [1, 1], [1, -1]].forEach(v => {
            let n = 0
            var [xp, yp] = [x, y]
            var [xi, yi] = v
            xp += xi
            yp += yi
            while (
                yp >= 0 && yp < 10 &&
                xp >= 0 && xp < 15 &&
                t[yp][xp] == player
            ) {
                n++
                xp += xi
                yp += yi
            }
            [xp, yp] = [x, y]
            xp -= xi
            yp -= yi
            while (
                yp >= 0 && yp < 10 &&
                xp >= 0 && xp < 15 &&
                t[yp][xp] == player
            ) {
                n++
                xp -= xi
                yp -= yi
            }
            if (n >= 4) {
                setTimeout(() => alert(player + " nyert!"), 100)
                go = true
            }
        })
        next = next == "X" ? "O" : "X"
    }
}