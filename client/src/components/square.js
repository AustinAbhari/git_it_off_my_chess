const Square = ({ color, piece }) => (
    <div style={`background: ${color}; 
				border: 2px black solid; 
                height: 80px;
                width: 80px; 
                display: flex;
                justify-content: center;
                align-items: center;`}>
        {piece?.piece_abbreviation || null} </div>
)

export default Square;