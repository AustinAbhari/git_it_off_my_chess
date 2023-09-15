import { h } from 'preact'
import Square from './square';
import { useState, useEffect } from 'preact/hooks';
import { getValidMoves } from '../api';

const Board = ({ board, youGotToMoveItMoveIt }) => {
    const [activeSquare, setActiveSquare] = useState(null)
    const [validSquares, setValidSqures] = useState([])
    const [captureSqures, setCaptureSquares] = useState([])


    const handleActiveSquare = async (id) => {
        if (id == activeSquare) {
            setActiveSquare(null);
            setValidSqures([])
            setCaptureSquares([])
        } else if (captureSqures.includes(id) || validSquares.includes(id)) {
            await youGotToMoveItMoveIt(activeSquare, id)
            setActiveSquare(null);
            setValidSqures([])
            setCaptureSquares([])
        } else {
            setActiveSquare(id)
        }
    }

    useEffect(() => {
        const validMoves = async () => {
            const result = await getValidMoves(activeSquare)
            const moves = result.moves.map(move => move.join(''))
            const captures = result.captures.map(move => move.join(''))

            setCaptureSquares(captures)
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
                            handleActiveSquare={handleActiveSquare}
                            validSquares={validSquares}
                            captureSqures={captureSqures}
                        />
                    ))}
                </tr>
            ))}
        </table>
    )
}


export default Board;