import pygame

pygame.init()
window = pygame.display.set_mode((1180, 720))
window.fill((128, 60, 60))

chessboard = pygame.image.load("Files/chess board.png").convert()
window.blit(chessboard, (0, 0))

chessboard_squares = []
chessboard_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("as")
for l in range(8):
    chessboard_row = []
    for n in range(8):
        chessboard_column = [(40 + (n * 80), 40 + (l * 80)), chessboard_letters[n] + str(l + 1)]

        king_piece = pygame.image.load("Files/King.png").convert_alpha()
        window.blit(king_piece, (chessboard_column[0][0], chessboard_column[0][1]))

        chessboard_row.append(chessboard_column)

    chessboard_squares.append(chessboard_row)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
