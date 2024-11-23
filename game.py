'''Create a guessing game. Run the program from the command prompt or terminal
and play to guess the lucky numbers. 
This is similar to the password program, however, use a list datatype of numbers and use the "in" keyword. 
Each time the user enters a correct value in the list they get a point. Play with two players. 
Get their names and print scores after each round. Make the game user-friendly by giving the right prompts. 
do it with strings as well. #use if <value> in <your_list>: '''

guessing_number = [1,2,3]
print("welcome to the guessing game")
num_of_players = int(input("enter the number of players"))
player_list = {}

for players in range(num_of_players):
    player_name = input(f"enter the name of the player{players+1}")
    if player_name in player_list:
        print("player name already exist enter another name:")
    else:
        player_list[player_name]=[]
print(player_list)







