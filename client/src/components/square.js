import { h } from 'preact';

const Square = ({ color, piece, activeSquare, id, handleActiveSquare, validSquares, captureSqures }) => {
    const squareColor = captureSqures.includes(id) ? 'Violet'
        : validSquares.includes(id) ? 'teal'
            : id == activeSquare ? 'gold' : color

    return (
        <div
            onClick={() => handleActiveSquare(id)}
            style={`background: ${squareColor};  
            color: red;
            height: 80px;
            width: 80px; 
            display: flex;
            justify-content: center;
            align-items: center;
            border: 1px solid black;
            cursor: grab;
            font-size: 4em;`}>
            {piece?.piece_abbreviation || null}
        </div>
    )
}


export default Square;