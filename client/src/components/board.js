import { h } from 'preact'
import Square from './square'

const Board = ({ board }) => (
    <table style="border-collapse: collapse;
              table-layout: fixed;">
        {board.grid.map(row => (
            <tr style="display: flex;">
                {row.map(square => (
                    <Square color={square._color} piece={square?._piece || null} />
                ))}
            </tr>
        ))}
    </table>
)


export default Board;