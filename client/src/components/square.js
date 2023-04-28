import { h } from 'preact';

const Square = ({ color, piece, activeSquare, id, setActiveSquare, validSquares }) => (
    <div
        onClick={() => setActiveSquare(id)}
        style={`background: ${validSquares.includes(id) ? 'yellow'
            : id == activeSquare ? 'hotpink' : color};  
                height: 80px;
                width: 80px; 
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 4em;`}>
        {piece?.piece_abbreviation || null} </div>
)


export default Square;