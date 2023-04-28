import { h } from 'preact'
import Square from './square';
import { useState, useEffect } from 'preact/hooks';
import { getValidMoves } from '../api';

const Board = ({ board }) => {
    const [activeSquare, setActiveSquare] = useState(null)
    const [validSquares, setValidSqures] = useState([])

    useEffect(() => {
        const validMoves = async () => {
            const result = await getValidMoves(activeSquare)
            const moves = result.moves.map(move => move.join(''))

            setValidSqures(moves)
        }

        if (activeSquare) validMoves()
    }, [activeSquare]);

    return (
        <table style="border-collapse: collapse;
              table-layout: fixed;">
            {board.grid.map((row, x) => (
                <tr style="display: flex;">
                    {row.map((square, y) => (
                        <Square
                            id={`${x}${y}`}
                            color={square._color}
                            piece={square?._piece || null}
                            activeSquare={activeSquare}
                            setActiveSquare={setActiveSquare}
                            validSquares={validSquares}
                        />
                    ))}
                </tr>
            ))}
        </table>
    )
}


export default Board;