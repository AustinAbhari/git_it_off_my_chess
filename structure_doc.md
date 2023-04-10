- Game class
	- Ownership of:
		- turn
		- checks (checkmate and shit)
	- Function:
		- `show_valid_moves(piece)`
			- highlighting all valid moves
- Board
	- `move_piece_to_location(piece_source_location, piece_destination)`
		- Move piece from X to Y (e.g. move pawn from b2 to b3)
		-
		  ```python
		  # if this were inside of "board"
		  move_piece_to_location(piece_source_location, piece_destination):
		    piece = find_piece(piece_source_location)
		    destination_square = find_peace(piece_destination)
		    update_destination(piece, destination_square) # handle the capturing
		    # update the board with the new location
		  ```
	- `validate_moves(piece, destination)`
		- make sure that the move is valid
- Square class
	- Properties:
		- `array_location`(e.g. [1,1])
		- `grid_location` (e.g. 'a1')
		- `piece`: Piece
- Piece