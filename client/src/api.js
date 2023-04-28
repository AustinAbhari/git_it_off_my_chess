export const getValidMoves = async (square) => {
    if (!square) return []

    console.log(square)
    square.split('')
    const result = await fetch(`http://0.0.0.0:5000/moves/${square[0]}-${square[1]}`);
    const data = await result.text()

    return JSON.parse(data)
}

export const movePiece = (gridPosition, piece) => {

}