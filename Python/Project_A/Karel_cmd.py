N_COLS = 3
N_ROWS = 3

def main():
    print("Welcome to first person Karel. You're at row 1, column 1, facing East (facing column " + str(N_COLS) + ")")
    facing_direction = 'East'
    current_col = 1
    current_row = 1
    action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    while action != '':
        if action == "move":
            if facing_direction == 'East' and current_col < N_COLS:  # move right
                current_col += 1
                print("You moved one step forward and now you're at row " + str(current_row) + " column " + str(current_col))
            elif facing_direction == 'West' and current_col > 1:  # move left
                current_col -= 1
                print("You moved one step forward and now you're at row " + str(current_row) + " column " + str(current_col) + ".")
            elif facing_direction == 'North' and current_row < N_ROWS:  # move up
                current_row += 1
                print("You moved one step forward and now you're at row " + str(current_row) + " column " + str(current_col) + ".")
            elif facing_direction == 'South' and current_row > 0:  # move down
                current_row -= 1
                print("You moved one step forward and now you're at row " + str(current_row) + " column " + str(current_col) + ".")
            else:
                print("You can't move forward!")

        elif action == "turn left":
            if facing_direction == 'East':
                facing_direction = 'North'
            elif facing_direction == 'North':
                facing_direction = 'West'
            elif facing_direction == 'West':
                facing_direction = 'South'
            elif facing_direction == 'South':
                facing_direction = 'East'
            print("You turned left and are now facing " + str(facing_direction) + ".")
        else:
            print("You've entered some wrong command which karel can't perform any operation")
        action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    print("You've ended up at row " + str(current_row) + " and column " + str(current_col) + " facing " + facing_direction + ".")

if __name__ == "__main__":
    main()
