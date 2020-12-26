from game.content import Rooms
from game import Player, CommandParser, Constants


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
        print(CommandParser.parse_input(user_input, player))
        print('\n')


game_loop()
