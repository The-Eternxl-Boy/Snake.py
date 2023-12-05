# Snake.py
this program was cooked in my binary brain




Summary:

initialize_curses(): Initializes the curses library and sets up the game window.
print_score(win, score): Prints the current score on the game window.
print_snake_title(win): Prints the title "SNAKE" on the game window.
generate_food(snake): Generates random coordinates for the food, ensuring it doesn't overlap with the snake.
print_food(win, food): Prints the food '*' on the game window at the specified coordinates.
handle_boundary_crossing(snake): Checks if the snake has crossed the boundaries and adjusts its position.
check_self_collision(snake): Checks if the snake has collided with itself.
move_snake(snake, key): Moves the snake based on the current direction determined by the key.
handle_food_eating(snake, food, score, win): Handles the logic when the snake eats the food, including updating the score and generating a new food location.
main(): The main function to run the Snake game, coordinating the game loop and interactions with curses.
This modular structure improves code organization and readability.
