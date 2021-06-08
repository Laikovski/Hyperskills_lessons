# Stage 1/5: Setting Up the Game
import random

class DominoGame:
    stock_pieces = [[2, 5], [1, 2], [3, 6], [0, 0], [0, 2], [5, 6], [3, 5], [2, 4], [3, 4], [1, 5], [0, 4], [2, 6], [3, 3], [1, 1], [1, 4], [1, 3], [2, 3], [4, 5], [2, 2], [0, 3], [0, 6], [5, 5], [4, 4], [4, 6], [0, 1], [0, 5], [1, 6],[6, 6]]
    player = []
    computer = []
    move = ''
    display = []
    def shufle_domino(self):
        random.shuffle(self.stock_pieces)
        return self.stock_pieces

    def set_domino(self):
        for _ in range(7):
            self.player.append(self.stock_pieces.pop())
            self.computer.append(self.stock_pieces.pop())
            self.player = sorted(self.player, reverse=True)
            self.computer = sorted(self.computer, reverse=True)
        temp_player = [[item[0], item[1]] for item in self.player if item[0] == item[1]]
        temp_comp = [[item[0], item[1]] for item in self.computer if item[0] == item[1]]


        if len(temp_player) == 0 and len(temp_comp) >= 1:
            self.move = 'player'
            self.display.append(max(temp_comp))
            self.computer.remove(max(temp_comp))
        elif len(temp_player) >= 1 and len(temp_comp) == 0:
            self.move = 'computer'
            self.display.append(max(temp_player))
            self.player.remove(max(temp_player))
        else:
            if max(temp_player) > max(temp_comp):
                self.move = 'computer'
                self.display.append(max(temp_player))
                self.player.remove(max(temp_player))
            elif max(temp_player) < max(temp_comp):
                self.move = 'player'
                self.display.append(max(temp_comp))
                self.computer.remove(max(temp_comp))

d = DominoGame()
d.shufle_domino()
d.set_domino()
print(f'Stock pieces: {d.stock_pieces}')
print(f'Computer pieces: {d.computer}')
print(f'player pieces: {d.player}')
print(f'Domino snake: {d.display}')
print(f'Status: {d.move}')