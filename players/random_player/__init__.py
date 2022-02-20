import abstract
from connect_4.consts import BOARD_COLS
import random

class Player(abstract.AbstractPlayer):
    def __init__(self, setup_time, player_color, time_per_k_turn):
        abstract.AbstractPlayer.__init__(self, setup_time, player_color, time_per_k_turn)

    def get_move(self, game_state, possible_moves):
        print('Available moves:')
        for move in possible_moves:
            print("{}".format(str(move)))
        while True:
            # Trying to get the next move index from the user.
            idx = random.randint(0, 7)
            try:
                idx = int(idx)
                if idx < 0 or idx >= BOARD_COLS or idx not in possible_moves:
                    print("invalid column")
                    continue
                return idx
            except ValueError:
                # Ignoring
                pass

    def __repr__(self):
        return 'random'


