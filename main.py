game_turns = 2

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

while game_turns < 11:
    #Enter X and Y Position like this: "12" (Column 1, Row 2)
    position = input("Where do you want to put your mark? ")
    if position == "exit":
        print("Exit Program")
        exit()
    
    horizontal_position = int(position[0])
    vertical_position = int(position[1])

    selected_row = map[vertical_position-1]

    if game_turns % 2 == 0:
        selected_row[horizontal_position-1] = "X"
    else:
        selected_row[horizontal_position-1] = "O"

    print(f"{row1}\n{row2}\n{row3}")
    game_turns += 1

print("Ending Game")
exit()