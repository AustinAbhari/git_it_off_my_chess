export const getValidMoves = async (square) => {
    if (!square) return []
    square.split('')
    const result = await fetch(`http://0.0.0.0:5000/moves/${square[0]}-${square[1]}`);
    const data = await result.text()

    return JSON.parse(data)
}

export const movePiece = async (from, to) => {
    const result = await fetch(`http://0.0.0.0:5000/move`,
        {
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ from: from.split(''), to: to.split('') })
        })

    const data = await result.text()
    return JSON.parse(data)
}

