from chess import polyglot
import chess
board = chess.Board()
while not board.is_game_over():
    with chess.polyglot.open_reader("book.bin") as reader:
        moves=[]
        weight=[]
        for entry in reader.find_all(board):
            moves.append(entry.move)
            weight.append(entry.weight)
    if len(weight)==0:
        break
    else:
        board.push(moves[weight.index(max(weight))])
print(board)
