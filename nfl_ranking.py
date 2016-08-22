import collections
import csv


def ready_data():
    with open('ranking_nfl.csv', 'r') as csvfile:
        ranking = csv.reader(csvfile)
        ranked = []
        for row in ranking:
            cleaned = row[0].replace(': ', ',')
            ranked.append((cleaned.split(',')))
        return ranked


def player_pick():
    picked = input('Which player was chosen? ')
    return picked.lower().strip()


def clean_list(list):
    new_list = []
    for row in list:
        need_cleaned = []
        for thing in row:
            cleaned = thing.strip().lower()
            need_cleaned.append(cleaned)
        new_list.append(need_cleaned)
    return new_list
    
def find_player(current_list):
    player_name = input('Find a player by name: ')
    for row in current_list:
        for thing in row:
            if player_name == thing:
                print('\n')
                print(row[0], player_name)
    input('>')

                
def main(ranked):
    current_list = ranked
    menu = ['> [R]emove a player', '> [F]ind a player']
    for item in menu:
        print(item)
    menu_choice = input('>')
    if menu_choice.lower() =='r':
        picked = player_pick()
        exists = False
        for row in current_list:
            if picked in row:
                row.remove(picked)
                exists = True
        if exists == False:
            print('Player not found...')
    elif menu_choice.lower() == 'f':
        find_player(current_list)
    else:
        print('That is not a menu option')
    for row in current_list:
        print(row[0], row[1:6])
    print('\n')


if __name__ == "__main__":
    ranked = ready_data()
    cleaned = clean_list(ranked)
    while True:
        main(cleaned)
