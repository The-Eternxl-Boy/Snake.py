import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

def initialize_curses():
    """
    Initializes the curses library and sets up the game window.
    """
    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)
    return win

def print_score(win, score):
    """
    Prints the current score on the game window.
    """
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')

def print_snake_title(win):
    """
    Prints the title "SNAKE" on the game window.
    """
    win.addstr(0, 27, ' SNAKE ')

def generate_food(snake):
    """
    Generates random coordinates for the food, ensuring it doesn't overlap with the snake.
    """
    food = []
    while food == []:
        food = [randint(1, 18), randint(1, 58)]
        if food in snake:
            food = []
    return food

def print_food(win, food):
    """
    Prints the food '*' on the game window at the specified coordinates.
    """
    win.addch(food[0], food[1], '*')

def handle_boundary_crossing(snake):
    """
    Checks if the snake has crossed the boundaries and adjusts its position accordingly.
    """
    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1

def check_self_collision(snake):
    """
    Checks if the snake has collided with itself.
    """
    return snake[0] in snake[1:]

def move_snake(snake, key):
    """
    Moves the snake based on the current direction determined by the key.
    """
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1),
                     snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

def handle_food_eating(snake, food, score, win):
    """
    Handles the logic when the snake eats the food, including updating the score and generating a new food location.
    """
    if snake[0] == food:
        food = generate_food(snake)
        score += 1
        print_food(win, food)
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    
    return food, score

def main():
    """
    Main function to run the Snake game.
    """
    win = initialize_curses()
    
    key = KEY_RIGHT  # Initializing values
    score = 0

    snake = [[4, 10], [4, 9], [4, 8]]  # Initial snake coordinates
    food = generate_food(snake)  # First food coordinates

    print_food(win, food)
    
    while key != 27:  # While Esc key is not pressed
        win.border(0)
        print_score(win, score)
        print_snake_title(win)
        win.timeout(150 - (len(snake) // 5 + len(snake) // 10) % 120)  # Increases the speed of Snake as its length increases

        event = win.getch()
        key = key if event == -1 else event

        if key == ord(' '):  # If SPACE BAR is pressed, wait for another one (Pause/Resume)
            key = -1
            while key != ord(' '):
                key = win.getch()
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:  # If an invalid key is pressed
            key = KEY_RIGHT  # Set default direction

        handle_boundary_crossing(snake)

        if check_self_collision(snake):
            break

        food, score = handle_food_eating(snake, food, score, win)

        move_snake(snake, key)
        win.addch(snake[0][0], snake[0][1], '=')

    curses.endwin()
    print("Score - " + str(score))

if __name__ == "__main__":
    main()





