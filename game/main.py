from game import Player, Command_Parser, Constants
from game.content import Rooms


# Main game loop
def game_loop():
    continue_playing = True
    player = Player.Player(Rooms.DRIVEWAY_ROOM, [])
    print(Constants.WELCOME_MESSAGE)
    print('\n')
    print(Rooms.DRIVEWAY_ROOM.describe_room())

    while continue_playing:
        print('Enter command:')
        user_input = input()
        print(Command_Parser.parse_input(user_input, player))


game_loop()
