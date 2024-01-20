#imported modules to enable API integration and randomised data selection
import random
import requests

# asking player name
player_name = input("What is your name? ")
print(f"Welcome {player_name} to Pokemon Top Trumps")

#setting the counter for the rounds of our game and creating the 'for' loop
player_count = 0
computer_count = 0

for rounds in range(5):
    print("Round ", rounds+1)

    # defining the random and linking the API
    def random_pokemon():
        pokemon_id = random.randint(1, 151)
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
        response = requests.get(url)
        pokemon = response.json()

    # making a dictionary of the stats we want
        return {
            'name': pokemon['name'],
            'id': pokemon['id'],
            'weight': pokemon['weight'],
            'height': pokemon['height'],
            'attack': pokemon['stats'][2]['base_stat'],
            'defence': pokemon['stats'][3]['base_stat'],
            'speed': pokemon['stats'][5]['base_stat'],
        }

    #gameplay script

    chosen_pokemon = random_pokemon()
    opponent_pokemon = random_pokemon()
    print(f"You have drawn {chosen_pokemon['name']} as your pokemon")
    
    #drowzee hating club
    if chosen_pokemon['id'] == 96:
        print(f"{chosen_pokemon['name']} is trash...yikes")
        print("but we move")
        print(f"id: {chosen_pokemon['id']}")
        print(f"weight: {chosen_pokemon['weight']} lbs")
        print(f"height: {chosen_pokemon['height']} ft")
        print(f"attack: {chosen_pokemon['attack']}")
        print(f"defence: {chosen_pokemon['defence']}")
        print(f"speed: {chosen_pokemon['speed']}")
        
    else:
        print(f"id: {chosen_pokemon['id']}")
        print(f"weight: {chosen_pokemon['weight']} lbs")
        print(f"height: {chosen_pokemon['height']} ft")
        print(f"attack: {chosen_pokemon['attack']}")
        print(f"defence: {chosen_pokemon['defence']}")
        print(f"speed: {chosen_pokemon['speed']}")

    #asking for stat choice

    stat_choice = input("Which stat would you like to use? ")

    chosen_stat = chosen_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

#opponent pokemon is picked
    print(f"Your opponent has been given {opponent_pokemon['name']}")
    if opponent_pokemon['id'] == 96:
        print(f"and as we all know {opponent_pokemon['name']} is garbage")
    print(f'Their {stat_choice} is {opponent_stat}')

#top trumps win conditions 
    if chosen_stat > opponent_stat:
        player_count = player_count + 1
        print("You win this round!")
    elif chosen_stat < opponent_stat:
        computer_count = computer_count + 1
        print("You lose this round!")
    else:
        print("It's a draw!")

#tally for each round
    print(f"{player_name}: {player_count}")
    print(f'Computer: {computer_count}')


#final score outside of loop
if player_count > computer_count:
    print(f"Congratulations {player_name}, you have won the game!")
if computer_count > player_count:
    print(f'The computer has beaten you at Pokemon Top Trumps, too bad!')


