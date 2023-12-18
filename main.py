from rich.console import Console
from rich.table import Table

console = Console()
ascii_art = """
┏┳┓┳┏┓  ┏┳┓┏┓┏┓  ┏┳┓┏┓┏┓
 ┃ ┃┃ ━━ ┃ ┣┫┃ ━━ ┃ ┃┃┣ 
 ┻ ┻┗┛   ┻ ┛┗┗┛   ┻ ┗┛┗┛

[bold white] By @aayamrajshakya [/bold white]
"""

console.print(ascii_art, style='bold red', justify='center')
game_run = True
board = ['-'] * 25
print('Board types: \n1.(3x3)\n2.(5x5)')
print()
board_type = int(input('Select: '))
playerX = input('Who is playing X? ')
playerO = input('Who is playing O? ')
print()
turns = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24
]

n = 1
board_range = 0


def display_board_3x3():
  table = Table()
  table.add_column("3x3 Mode", justify="center", style="cyan", no_wrap=True)
  table.add_row(f'|{board[0]}| |{board[1]}| |{board[2]}|')
  table.add_row(f'|{board[3]}| |{board[4]}| |{board[5]}|')
  table.add_row(f'|{board[6]}| |{board[7]}| |{board[8]}|')
  console.print(table)


def display_board_5x5():
  table = Table()
  table.add_column("5x5 Mode", justify="center", style="cyan")
  table.add_row(
      f'|{board[0]}| |{board[1]}| |{board[2]}| |{board[3]}| |{board[4]}|')
  table.add_row(
      f'|{board[5]}| |{board[6]}| |{board[7]}| |{board[8]}| |{board[9]}|')
  table.add_row(
      f'|{board[10]}| |{board[11]}| |{board[12]}| |{board[13]}| |{board[14]}|')
  table.add_row(
      f'|{board[15]}| |{board[16]}| |{board[17]}| |{board[18]}| |{board[19]}|')
  table.add_row(
      f'|{board[20]}| |{board[21]}| |{board[22]}| |{board[23]}| |{board[24]}|')
  console.print(table)


def play_game():
  global game_run
  while game_run:
    player_turn()
    check_column()
    check_row()
    check_diagonal()
    check_win()
    check_tie()


def player_turn():
  global n
  if n % 2 != 0:
    if board_type == 1:
      display_board_3x3()
    else:
      display_board_5x5()
    turn_choice = place_move(playerX)
    board[turn_choice] = 'X'
  else:
    if board_type == 1:
      display_board_3x3()
    else:
      display_board_5x5()
    turn_choice = place_move(playerO)
    board[turn_choice] = 'O'
  n += 1


def place_move(player):
  if board_type == 1:
    board_range = 9
  else:
    board_range = 25
  while True:
    turn_choice = int(input(f"{player}, make your move: "))
    turn_choice -= 1
    if board_type == 1 and turn_choice not in range(board_range):
      print("Invalid move for 3x3 board. Please choose a number from 1 to 9.")
    elif board[turn_choice] != '-':
      print("Invalid move. Please choose an empty space.")
    else:
      return turn_choice


def check_row():
  global game_run
  if board_type == 1:
    for i in range(0, 9, 3):
      if board[i] == board[i + 1] == board[i + 2] != '-':
        game_run = False
        return board[i]
  else:
    for i in range(0, 25, 5):
      if board[i] == board[i + 1] == board[i + 2] == board[i + 3] == board[
          i + 4] != '-':
        game_run = False
        return board[i]


def check_column():
  global game_run
  if board_type == 1:
    for i in range(3):
      if board[i] == board[i + 3] == board[i + 6] != '-':
        game_run = False
        return board[i]
  elif board_type == 2:
    for i in range(5):
      if board[i] == board[i + 5] == board[i + 10] == board[i + 15] == board[
          i + 20] != '-':
        game_run = False
        return board[i]


def check_diagonal():
  global game_run
  if board_type == 1:
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'
    if diagonal1 or diagonal2:
      game_run = False
      return board[4]
  else:
    diagonal1 = board[0] == board[6] == board[12] == board[18] == board[
        24] != '-'
    diagonal2 = board[4] == board[8] == board[12] == board[16] == board[
        20] != '-'
    if diagonal1 or diagonal2:
      game_run = False
      return board[12]


def check_win():
  win_by_column = check_column()
  win_by_row = check_row()
  win_by_diagonal = check_diagonal()

  if 'X' in (win_by_column, win_by_row, win_by_diagonal):
    if board_type == 1:
      display_board_3x3()
    else:
      display_board_5x5()
    print(f"{playerX} won!")

  elif 'O' in (win_by_column, win_by_row, win_by_diagonal):
    if board_type == 1:
      display_board_3x3()
    else:
      display_board_5x5()
    print(f"{playerO} won!")


def check_tie():
  global game_run
  if '-' not in board:
    if board_type == 1:
      display_board_3x3()
    else:
      display_board_5x5()
    print("It's a tie!")
    game_run = False


if __name__ == "__main__":
  play_game()
