# Import important files and libraries
import boxing_state

import pygame
pygame.init()

# Dimensions for window
window_width = 1100
window_height = 720

# Bool for if either king is dead
white_king_alive = True
black_king_alive = True

# Create the window and fonts for later on
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Chess Boxing!')
font = pygame.font.SysFont('freesansbold.ttf', 60)
small_font = pygame.font.SysFont('freesansbold.ttf', 25)

# Set up piece structure, the main way to detect where each piece is, the health and damage of each piece, and the list to store captured pieces
white_piece_structure = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook",
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
white_health_and_damage = [[100, 10], [75, 15], [75, 15], [100, 20], [150, 10], [75, 15], [75, 15], [100, 10],
                           [75, 10], [75, 10], [75, 10], [75, 10], [75, 10], [75, 10], [75, 10], [75, 10]]
white_piece_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
white_captured_pieces = []

black_piece_structure = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook",
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
black_health_and_damage = [[100, 10], [75, 15], [75, 15], [100, 20], [150, 10], [75, 15], [75, 15], [100, 10],
                           [75, 10], [75, 10], [75, 10], [75, 10], [75, 10], [75, 10], [75, 10], [75, 10]]
black_piece_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_captured_pieces = []

# More set up for future gameplay
current_turn = 0
selected_piece = 200
possible_moves = []

# Game pieces loaded in
white_pawn = pygame.image.load("files/WhitePawn.png")
white_pawn = pygame.transform.scale(white_pawn, (65, 65))

white_bishop = pygame.image.load("files/WhiteBishop.png")
white_bishop = pygame.transform.scale(white_bishop, (70, 70))

white_knight = pygame.image.load("Files/WhiteKnight.png")
white_knight = pygame.transform.scale(white_knight, (70, 70))

white_rook = pygame.image.load("files/WhiteRook.png")
white_rook = pygame.transform.scale(white_rook, (70, 70))

white_queen = pygame.image.load("files/WhiteQueen.png")
white_queen = pygame.transform.scale(white_queen, (70, 70))

white_king = pygame.image.load("files/WhiteKing.png")
white_king = pygame.transform.scale(white_king, (70, 70))

black_pawn = pygame.image.load("files/BlackPawn.png")
black_pawn = pygame.transform.scale(black_pawn, (65, 65))

black_bishop = pygame.image.load("files/BlackBishop.png")
black_bishop = pygame.transform.scale(black_bishop, (70, 70))

black_knight = pygame.image.load("files/BlackKnight.png")
black_knight = pygame.transform.scale(black_knight, (70, 70))

black_rook = pygame.image.load("files/BlackRook.png")
black_rook = pygame.transform.scale(black_rook, (70, 70))

black_queen = pygame.image.load("files/BlackQueen.png")
black_queen = pygame.transform.scale(black_queen, (70, 70))

black_king = pygame.image.load("files/BlackKing.png")
black_king = pygame.transform.scale(black_king, (70, 70))

white_images = [white_pawn, white_bishop, white_knight, white_rook, white_queen, white_king]
black_images = [black_pawn, black_bishop, black_knight, black_rook, black_queen, black_king]

chess_piece_list = ["pawn", "bishop", "knight", "rook", "queen", "king"]

# Health and damage for each of the piece types
chess_piece_health_and_damage = {
    "pawn": (75, 10),
    "bishop": (75, 15),
    "knight": (75, 15),
    "rook": (100, 15),
    "queen": (100, 20),
    "king": (150, 10),
}


# Draws important things that will show up before pieces
def display_game():
    # Display chessboard
    chessboard = pygame.image.load('files/chess board.png')
    window.blit(chessboard, (0, 0))
    pygame.draw.rect(window, 'gold', [720, 0, 380, window_height], 5)

    # Display side box with status text to say whose turn it is
    pygame.draw.rect(window, 'gold', [720, 600, 380, 120], 5)
    status_text = ['White turn', 'White to move',
                   'Black turn', 'Black to move']

    text = font.render(status_text[current_turn], True, 'black')
    text_rect = text.get_rect(center=(910, 660))
    window.blit(text, text_rect)


# Draws the pieces in their designated spots
def display_pieces():
    # Based on the locations, use the single digit values and multiply them by each chess spots width/height (80)
    for i in range(len(black_piece_structure)):
        index = chess_piece_list.index(black_piece_structure[i])
        if black_piece_structure[i] == "pawn":
            window.blit(black_pawn, (black_piece_locations[i][0] * 80 + 45, black_piece_locations[i][1] * 80 + 45))
        else:
            window.blit(black_images[index], (black_piece_locations[i][0] * 80 + 45, black_piece_locations[i][1] * 80 + 45))

        if current_turn > 2:
            if selected_piece == i:
                pygame.draw.rect(window, "red", [black_piece_locations[i][0] * 80 + 40, black_piece_locations[i][1] * 80 + 40, 80, 80], 2)

    for i in range(len(white_piece_structure)):
        index = chess_piece_list.index(white_piece_structure[i])
        if white_piece_structure[i] == "pawn":
            window.blit(white_pawn, (white_piece_locations[i][0] * 80 + 45, white_piece_locations[i][1] * 80 + 45))
        else:
            window.blit(white_images[index], (white_piece_locations[i][0] * 80 + 45, white_piece_locations[i][1] * 80 + 45))

        if current_turn < 2:
            if selected_piece == i:
                pygame.draw.rect(window, "red", [white_piece_locations[i][0] * 80 + 40, white_piece_locations[i][1] * 80 + 40, 80, 80], 2)


# Checks all possible options to move by checking the type of piece and calling its function
def check_possible_move_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []

    # Find the name of the piece to call its function
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]

        if piece == "pawn":
            moves_list = check_pawn_moves(location, turn)
        elif piece == "bishop":
            moves_list = check_bishop_moves(location, turn)
        elif piece == "knight":
            moves_list = check_knight_moves(location, turn)
        elif piece == "rook":
            moves_list = check_rook_moves(location, turn)
        elif piece == "queen":
            moves_list = check_queen_moves(location, turn)
        elif piece == "king":
            moves_list = check_king_moves(location, turn)

        all_moves_list.append(moves_list)

    return all_moves_list


# Check pawn moves
def check_pawn_moves(piece_location, turn):
    available_moves = []

    # Check the different possible moves for a pawn (1 up, 2 up if it's the first move, or diagonal to take a piece)
    if turn == "black":
        if (piece_location[0], piece_location[1] + 1) not in black_piece_locations and (piece_location[0], piece_location[1] + 1) not in white_piece_locations and piece_location[1] < 7:
            available_moves.append((piece_location[0], piece_location[1] + 1))

        if (piece_location[0], piece_location[1] + 2) not in black_piece_locations and (piece_location[0], piece_location[1] + 2) not in white_piece_locations and piece_location[1] == 1 and (piece_location[0], piece_location[1] + 1) not in black_piece_locations and (piece_location[0], piece_location[1] + 1) not in white_piece_locations:
            available_moves.append((piece_location[0], piece_location[1] + 2))

        if (piece_location[0] + 1, piece_location[1] + 1) in white_piece_locations:
            available_moves.append((piece_location[0] + 1, piece_location[1] + 1))

        if (piece_location[0] - 1, piece_location[1] + 1) in white_piece_locations:
            available_moves.append((piece_location[0] - 1, piece_location[1] + 1))
    elif turn == "white":
        if (piece_location[0], piece_location[1] - 1) not in white_piece_locations and (piece_location[0], piece_location[1] - 1) not in black_piece_locations and piece_location[1] > 0:
            available_moves.append((piece_location[0], piece_location[1] - 1))

        if (piece_location[0], piece_location[1] - 2) not in white_piece_locations and (piece_location[0], piece_location[1] - 2) not in black_piece_locations and piece_location[1] == 6 and (piece_location[0], piece_location[1] - 1) not in white_piece_locations and (piece_location[0], piece_location[1] - 1) not in black_piece_locations:
            available_moves.append((piece_location[0], piece_location[1] - 2))

        if (piece_location[0] + 1, piece_location[1] - 1) in black_piece_locations:
            available_moves.append((piece_location[0] + 1, piece_location[1] - 1))

        if (piece_location[0] - 1, piece_location[1] - 1) in black_piece_locations:
            available_moves.append((piece_location[0] - 1, piece_location[1] - 1))

    return available_moves


# Check bishop moves
def check_bishop_moves(piece_location, turn):
    available_moves = []

    if turn == 'white':
        other_team_list = black_piece_locations
        same_team_list = white_piece_locations
    else:
        same_team_list = black_piece_locations
        other_team_list = white_piece_locations

    for i in range(4):
        # Each iteration, check a different diagonal line path
        more_moves_available = True
        iterations = 1
        if i == 0:
            x_increment = 1
            y_increment = -1
        elif i == 1:
            x_increment = -1
            y_increment = -1
        elif i == 2:
            x_increment = 1
            y_increment = 1
        else:
            x_increment = -1
            y_increment = 1

        # As long as there are no obstacles in the way, add new spots in the line path into available_moves
        while more_moves_available:
            if (piece_location[0] + (iterations * x_increment), piece_location[1] + (iterations * y_increment)) not in same_team_list and 0 <= piece_location[0] + (iterations * x_increment) <= 7 and 0 <= piece_location[1] + (iterations * y_increment) <= 7:
                available_moves.append((piece_location[0] + (iterations * x_increment), piece_location[1] + (iterations * y_increment)))

                if (piece_location[0] + (iterations * x_increment), piece_location[1] + (iterations * y_increment)) in other_team_list:
                    more_moves_available = False
                iterations += 1
            else:
                more_moves_available = False

    return available_moves


# Check knight moves
def check_knight_moves(piece_location, turn):
    available_moves = []

    if turn == 'white':
        same_team_list = white_piece_locations
    else:
        same_team_list = black_piece_locations

    # All 8 combinations of moves a knight can do
    available_paths = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        # Check each path and see if it is available
        check_move = (piece_location[0] + available_paths[i][0], piece_location[1] + available_paths[i][1])
        if check_move not in same_team_list and 0 <= check_move[0] <= 7 and 0 <= check_move[1] <= 7:
            available_moves.append(check_move)

    return available_moves


# Check rook moves
def check_rook_moves(piece_location, turn):
    available_moves = []

    if turn == 'white':
        other_team_list = black_piece_locations
        same_team_list = white_piece_locations
    else:
        same_team_list = black_piece_locations
        other_team_list = white_piece_locations

    # Straight line movements
    for i in range(4):
        # Each iteration, check a different straight line path
        more_moves_available = True
        iterations = 1
        if i == 0:
            x_increment = 0
            y_increment = 1
        elif i == 1:
            x_increment = 0
            y_increment = -1
        elif i == 2:
            x_increment = 1
            y_increment = 0
        else:
            x_increment = -1
            y_increment = 0

        # As long as there are no obstacles in the way, add new spots in the line path into available_moves
        while more_moves_available:
            if (piece_location[0] + (iterations * x_increment), piece_location[1] + (iterations * y_increment)) not in same_team_list and 0 <= piece_location[0] + (iterations * x_increment) <= 7 and 0 <= piece_location[1] + (iterations * y_increment) <= 7:
                available_moves.append((piece_location[0] + (iterations * x_increment), piece_location[1] + (iterations * y_increment)))

                if (piece_location[0] + (iterations * x_increment), piece_location[1] + (iterations * y_increment)) in other_team_list:
                    more_moves_available = False
                iterations += 1
            else:
                more_moves_available = False
    return available_moves


# Check queen moves
def check_queen_moves(piece_location, turn):
    available_moves = []

    # Simply use the bishop and rook checks as a queen is a combination
    available_moves = check_bishop_moves(piece_location, turn)
    moves_list_rook = check_rook_moves(piece_location, turn)
    for i in range(len(moves_list_rook)):
        available_moves.append(moves_list_rook[i])

    return available_moves


# Check king moves
def check_king_moves(piece_location, turn):
    available_moves = []

    if turn == 'white':
        same_team_list = white_piece_locations
    else:
        same_team_list = black_piece_locations

    # Only 8 spots to check for
    possible_king_moves = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        # Check if each of these spots are even open
        move = (piece_location[0] + possible_king_moves[i][0], piece_location[1] + possible_king_moves[i][1])
        if move not in same_team_list and 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
            available_moves.append(move)

    return available_moves


# Check possible moves for selected piece only
def check_possible_moves():
    if current_turn < 2:
        options_list = white_options
    else:
        options_list = black_options

    # Find the possible options to draw them for a single piece
    possible_options = options_list[selected_piece]
    return possible_options


# Display possible moves onto the window
def draw_possible_moves(moves_possible):
    # Draw each possible move based on who is selected using gray circles
    for i in range(len(moves_possible)):
        pygame.draw.circle(window, "gray", (moves_possible[i][0] * 80 + 80, moves_possible[i][1] * 80 + 80), 5)


# Display captured pieces
def display_captured_pieces():
    pygame.draw.line(window, 'black', (910, 5), (910, 600), 10)
    for i in range(len(white_captured_pieces)):
        captured_piece = white_captured_pieces[i]
        index = chess_piece_list.index(captured_piece)

        if i >= 8:
            window.blit(black_images[index], (800, 10 + 70 * (i - 8)))
        else:
            window.blit(black_images[index], (725, 10 + 70 * i))
    for i in range(len(black_captured_pieces)):
        captured_piece = black_captured_pieces[i]
        index = chess_piece_list.index(captured_piece)
        if i >= 8:
            window.blit(white_images[index], (1010, 10 + 70 * (i - 8)))
        else:
            window.blit(white_images[index], (935, 10 + 70 * i))


# counter for king check flashing
check_counter = 0


# King in check
def display_check():
    checked = False
    if current_turn < 2:
        if "king" in white_piece_structure:
            king_index = white_piece_structure.index("king")
            king_location = white_piece_locations[king_index]

            # Use a counter to flash a dark red square around the king
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if check_counter < 15:
                        pygame.draw.rect(window, "dark red", (white_piece_locations[king_index][0] * 80 + 40, white_piece_locations[king_index][1] * 80 + 40, 80, 80), 5)
    else:
        if "king" in white_piece_structure:
            king_index = white_piece_structure.index("king")
            king_location = black_piece_locations[king_index]

            # Use a counter to flash a dark red square around the king
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if check_counter < 15:
                        pygame.draw.rect(window, "dark red", (black_piece_locations[king_index][0] * 80 + 40, black_piece_locations[king_index][1] * 80 + 40, 80, 80), 5)


def check_king_death():
    white_king_not_dead = False
    black_king_not_dead = False

    for piece in white_piece_structure:
        if piece == "king":
            white_king_not_dead = True
            break
    for piece in black_piece_structure:
        if piece == "king":
            black_king_not_dead = True
            break

    return white_king_not_dead, black_king_not_dead

# Call the check_options function
black_options = check_possible_move_options(black_piece_structure, black_piece_locations, "black")
white_options = check_possible_move_options(white_piece_structure, white_piece_locations, "white")

# Timer and frames per second for flashing check
timer = pygame.time.Clock()
frames_per_second = 60

# Boxing-State check
piece_taken = False

# Taker wins boxing or taken wins
taker = None
taker_wins = None
original_selection = None

# Bools to check if each attack/block situation is active
player1Attack1 = False
player1Block1 = False

player2Attack1 = False
player2Block1 = False

# First value is attack1, second value is block1, third value is attack2, fourth value is block2
white_piece_animation = {
    "pawn": (),
    "bishop": (),
    "knight": (),
    "rook": (),
    "queen": (),
    "king": ()
}

# First value is attack1, second value is block1, third value is attack2, fourth value is block2
black_piece_animation = {
    "pawn": (),
    "bishop": (),
    "knight": (),
    "rook": (),
    "queen": (),
    "king": ()
}

# Animation sprites for each block/attack
player1AttackAnimation1 = ["Files/Player1Attack1/Player1Attack1Image1.png", "Files/Player1Attack1/Player1Attack1Image2.png", "Files/Player1Attack1/Player1Attack1Image3.png", "Files/Player1Attack1/Player1Attack1Image4.png"]
player1BlockAnimation1 = ["Files/Player1Block1/Player1Block1Image1.png", "Files/Player1Block1/Player1Block1Image2.png"]

player2AttackAnimation1 = ["Files/Player2Attack1/Player2Attack1Image1.png", "Files/Player2Attack1/Player2Attack1Image2.png", "Files/Player2Attack1/Player2Attack1Image3.png", "Files/Player2Attack1/Player2Attack1Image4.png"]
player2BlockAnimation1 = ["Files/Player2Block1/Player2Block1Image1.png", "Files/Player2Block1/Player2Block1Image2.png"]

# main game loop
playing = True
while playing:
    timer.tick(frames_per_second)
    if check_counter < 30:
        check_counter += 1
    else:
        check_counter = 0

    window.fill("gray")

    # Chess game-state
    if not piece_taken:
        # Call functions
        display_game()
        display_pieces()
        display_captured_pieces()

        display_check()

        # If selected piece is not 200, it means that there is actually a piece selected
        if selected_piece != 200:
            possible_moves = check_possible_moves()
            draw_possible_moves(possible_moves)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                with open("saved_info.txt", "a") as saved_info_file:
                    saved_info_file.write("DNF, DNF\n")
                playing = False

            # Check if any player had selected a piece or a new spot to move to
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x_coord = (event.pos[0] - 40) // 80
                y_coord = (event.pos[1] - 40) // 80
                click_cords = (x_coord, y_coord)

                # White turn information
                if current_turn <= 1:
                    if click_cords in white_piece_locations:
                        selected_piece = white_piece_locations.index(click_cords)
                        if current_turn == 0:
                            current_turn = 1

                    if click_cords in possible_moves and selected_piece != 200:
                        original_selection = white_piece_locations[selected_piece]
                        white_piece_locations[selected_piece] = click_cords
                        if click_cords in black_piece_locations:
                            # Move to boxing game-state after creating the 2 boxing classes
                            white_piece_name = white_piece_structure[selected_piece]
                            black_piece_name = black_piece_structure[black_piece_locations.index(click_cords)]

                            boxer1 = boxing_state.Boxer(window, 100, 200, player1AttackAnimation1, player1BlockAnimation1, white_health_and_damage[selected_piece][1], white_health_and_damage[selected_piece][0], index_to_change=selected_piece)
                            boxer2 = boxing_state.Boxer(window, 500, 200, player2AttackAnimation1, player2BlockAnimation1, black_health_and_damage[black_piece_locations.index(click_cords)][1], black_health_and_damage[black_piece_locations.index(click_cords)][0])

                            player1Attack1 = False
                            player2Attack1 = False
                            player1Block1 = False
                            player2Block1 = False

                            taker = "White"
                            taker_wins = None
                            piece_taken = True
                            break
                        black_options = check_possible_move_options(black_piece_structure, black_piece_locations, "black")
                        white_options = check_possible_move_options(white_piece_structure, white_piece_locations, "white")
                        current_turn = 2
                        selected_piece = 200
                        possible_moves = []

                # Black turn information
                if current_turn >= 2:
                    if click_cords in black_piece_locations:
                        selected_piece = black_piece_locations.index(click_cords)
                        if current_turn == 2:
                            current_turn = 3

                    if click_cords in possible_moves and selected_piece != 200:
                        original_selection = black_piece_locations[selected_piece]
                        black_piece_locations[selected_piece] = click_cords
                        if click_cords in white_piece_locations:
                            # Move to boxing game-state after creating the 2 boxing classes
                            black_piece_name = black_piece_structure[selected_piece]
                            white_piece_name = white_piece_structure[white_piece_locations.index(click_cords)]

                            boxer1 = boxing_state.Boxer(window, 100, 200, player1AttackAnimation1, player1BlockAnimation1, white_health_and_damage[white_piece_locations.index(click_cords)][1], white_health_and_damage[white_piece_locations.index(click_cords)][0])
                            boxer2 = boxing_state.Boxer(window, 500, 200, player2AttackAnimation1, player2BlockAnimation1, black_health_and_damage[selected_piece][1], black_health_and_damage[selected_piece][0], index_to_change=selected_piece)

                            player1Attack1 = False
                            player2Attack1 = False
                            player1Block1 = False
                            player2Block1 = False

                            taker = "Black"
                            taker_wins = None
                            piece_taken = True
                            break
                        black_options = check_possible_move_options(black_piece_structure, black_piece_locations, "black")
                        white_options = check_possible_move_options(white_piece_structure, white_piece_locations, "white")
                        current_turn = 0
                        selected_piece = 200
                        possible_moves = []
    # Boxing game-state
    else:
        # Check key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("saved_info.txt", "a") as saved_info_file:
                    saved_info_file.write("DNF, DNF\n")
                playing = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    taker_wins = False

                if event.key == pygame.K_w and not player1Block1:
                    player1Attack1 = True
                if event.key == pygame.K_UP and not player2Block1:
                    player2Attack1 = True

                if event.key == pygame.K_a:
                    player1Block1 = True
                if event.key == pygame.K_LEFT:
                    player2Block1 = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player1Block1 = False
                    boxer1.reset_block_bool()
                if event.key == pygame.K_LEFT:
                    player2Block1 = False
                    boxer2.reset_block_bool()

        # Display atmosphere for game-state
        boxing_ring = pygame.image.load("files/BoxingRing.png")
        boxing_ring = pygame.transform.scale(boxing_ring, (1100, 720))
        window.blit(boxing_ring, (0, 0))

        # Check and call functions for attacks and blocks or idle
        if player1Attack1:
            player1Attack1 = boxer1.attack(boxer2)
        elif player1Block1:
            player1Block1 = boxer1.defend()
        if not player1Block1 and not player1Attack1:
            boxer1.idle()

        if player2Attack1:
            player2Attack1 = boxer2.attack(boxer1)
        elif player2Block1:
            player2Block1 = boxer2.defend()
        if not player2Block1 and not player2Attack1:
            boxer2.idle()

        # Update and display health text
        boxer1.update_health(font, window, 100, 0)
        boxer2.update_health(font, window, 425, 720)

        # Display Controls
        pygame.draw.rect(window, 'light gray', [360, 0, 380, 125], 100)
        pygame.draw.rect(window, 'gold', [360, 0, 380, 125], 5)
        text_to_render = ["Controls (WASD and Arrow keys):", "Player 1: W for High Attack, A for High Block", "Player 2: ^ for High Attack, < for High Block"]

        for text in text_to_render:
            render = small_font.render(text, True, 'black')
            text_rect = render.get_rect(center=(550, 25 + (text_to_render.index(text) * 35)))
            window.blit(render, text_rect)

        boxer1_lose = boxer1.check_health()
        boxer2_lose = boxer2.check_health()

        # Check who had lost
        if boxer1_lose or boxer2_lose:
            if taker == "White":
                if boxer1_lose:
                    taker_wins = False
                    new_health = white_health_and_damage[boxer1.index_to_change][0] / 2
                    white_health_and_damage[boxer1.index_to_change][0] = int(new_health)
                if boxer2_lose:
                    white_health_and_damage[boxer1.index_to_change][0] = boxer1.health
                    taker_wins = True
            elif taker == "Black":
                if boxer1_lose:
                    taker_wins = True
                    black_health_and_damage[boxer2.index_to_change][0] = boxer2.health
                if boxer2_lose:
                    taker_wins = False
                    new_health = black_health_and_damage[boxer2.index_to_change][0] / 2
                    black_health_and_damage[boxer2.index_to_change][0] = int(new_health)

        # Once one player loses
        if taker_wins is not None:
            # Depending on who won, either go through with the move or just return without taking the piece
            if taker == "White":
                if taker_wins:
                    black_piece = black_piece_locations.index(click_cords)
                    white_captured_pieces.append(black_piece_structure[black_piece])
                    black_piece_structure.pop(black_piece)
                    black_piece_locations.pop(black_piece)
                    black_health_and_damage.pop(black_piece)
                else:
                    white_piece_locations[selected_piece] = original_selection
                black_options = check_possible_move_options(black_piece_structure, black_piece_locations, "black")
                white_options = check_possible_move_options(white_piece_structure, white_piece_locations, "white")
                current_turn = 2
                selected_piece = 200
                possible_moves = []
                piece_taken = False
            elif taker == "Black":
                if taker_wins:
                    white_piece = white_piece_locations.index(click_cords)
                    black_captured_pieces.append(white_piece_structure[white_piece])
                    white_piece_structure.pop(white_piece)
                    white_piece_locations.pop(white_piece)
                    white_health_and_damage.pop(white_piece)
                else:
                    black_piece_locations[selected_piece] = original_selection
                black_options = check_possible_move_options(black_piece_structure, black_piece_locations, "black")
                white_options = check_possible_move_options(white_piece_structure, white_piece_locations, "white")
                current_turn = 0
                selected_piece = 200
                possible_moves = []

                taker_wins = None
                piece_taken = False

            white_king_alive, black_king_alive = check_king_death()

            if not white_king_alive or not black_king_alive:
                if not black_king_alive:
                    with open("saved_info.txt", "a") as saved_info_file:
                        saved_info_file.write("Win, Lose\n")
                elif not white_king_alive:
                    with open("saved_info.txt", "a") as saved_info_file:
                        saved_info_file.write("Lose, Win\n")
                playing = False

    pygame.display.update()

while not white_king_alive or not black_king_alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            white_king_alive = True
            black_king_alive = True

    window.fill("black")

    pygame.draw.rect(window, 'gold', [720, 0, 380, window_height], 5)
    pygame.draw.rect(window, 'gold', [720, 600, 380, 120], 5)

    with open("saved_info.txt", "r") as saved_info_file:
        reader = saved_info_file.readlines()
        player1_wins = 0
        player2_wins = 0
        for line in reader:
            line_split = line.split(", ")
            if line_split[0] == "Win":
                player1_wins += 1
            elif line_split[1] == "Win":
                player2_wins += 1

        if not black_king_alive:
            texts = ["The Black King has been defeated! ", "Player 1 is the winner! ", "Player 1 now has " + str(player1_wins) + " wins! ", "Press Space to reset the game from ",  "scratch or simply exit the game."]
            for i in range(len(texts)):
                text = font.render(texts[i], True, 'White')
                text_rect = text.get_rect(center=(560, 250 + 50*i))
                window.blit(text, text_rect)
        if not white_king_alive:
            texts = ["The White King has been defeated! ", "Player 2 is the winner! ", "Player 2 now has " + str(player2_wins) + " wins! ", "Press Space to reset the game from ", "scratch or simply exit the game."]
            for i in range(len(texts)):
                text = font.render(texts[i], True, 'White')
                text_rect = text.get_rect(center=(560, 250 + 50*i))
                window.blit(text, text_rect)

    pygame.display.update()

pygame.quit()
