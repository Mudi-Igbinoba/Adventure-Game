import time
import random


def print_pause(intro):
    print(intro, flush=True)
    time.sleep(2)


def intro(villain):
    print_pause('You find yourself standing in an '
                'open field, filled with grass and '
                'yellow wildflowers.')

    print_pause(f'Rumor has it that a {villain} '
                'is somewhere around here, and has '
                'been terrifying the nearby village.')

    print_pause('In front of you is a house.')
    print_pause('To your right is a dark cave.')
    print_pause('In your hand you hold your trusty '
                '(but not very effective) dagger.')


def cave(villain, items, weapons, score, points):
    print_pause('You peer cautiously into the cave.')

    if weapons in items:
        print_pause("You've been here before, and "
                    'gotten all the good stuff. '
                    "It's just an empty cave now.")
    else:
        print_pause('It turns out to be only a very small cave.')
        print_pause('Your eye catches a glint of metal behind a rock.')
        print_pause(f'You have found the magical {weapons}!')
        print_pause('You discard your silly old '
                    'dagger and take the magical weapon with '
                    'with you.')
        items.append(weapons)
        score += 5
        print_pause(f'You just gained 5 points for getting the {weapons}')
    print_pause('You walk back out to the field.')
    main(villain, items, weapons, score, points)


def door(villain, items, weapons, score, points):
    print_pause('You approach the door of the '
                'house.')
    print_pause('You are about to knock when '
                'the door opens and out steps a'
                f' {villain}.')
    print_pause(f"Eep! This is the {villain}'s "
                'house!')
    print_pause(f'The {villain} attacks you!')

    if weapons in items:
        fight_or_run(villain, items, weapons, score, points)
    else:
        print_pause('You feel a bit under-prepared '
                    'for this, what with only '
                    'having a tiny dagger.')
        fight_or_run(villain, items, weapons, score, points)


def cave_or_door(villain, items, weapons, score, points):
    choice = valid_input('(Please enter 1 or 2).\n', ['1', '2'])
    if choice == '1':
        door(villain, items, weapons, score, points)
    else:
        cave(villain, items, weapons, score, points)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option


def fight(villain, items, weapons, score, points):
    print_pause("Here's 5 points for being brave. Good luck!")
    score += 5

    if weapons in items:
        print_pause(f'As the {villain} moves to attack, '
                    'you unsheath your new weapon.')
        print_pause(f'The {weapons} shines brightly'
                    ' in your hand as you brace yourself '
                    'for the attack.')
        print_pause(f'But the {villain} takes one '
                    'look at your shiny new toy and runs away!')
        print_pause('You have rid the town of the '
                    f'{villain}. You are victorious!')
        score += points
        print_pause(f'You just gained {points} points'
                    f' for defeating the {villain}.')
    else:
        print_pause('You do your best...')
        print_pause(f'but your dagger is no match for the {villain}.')
        print_pause('You have been defeated!')
        score -= points
        print_pause(f'You just lost {points} points '
                    f'for getting bested by the {villain}.')
    win_or_lose(score)
    play_again(score)


def run(villain, items, weapons, score, points):
    print_pause("You run back into the field. Luckily"
                ", you don't seem to have been followed.")
    score -= 2
    print_pause('You just lost 2 points for running away.')
    main(villain, items, weapons, score, points)


def fight_or_run(villain, items, weapons, score, points):
    response = valid_input('Would you like to (1) fight or (2) run away?',
                           ['1', '2'])

    if response == '1':
        fight(villain, items, weapons, score, points)
    else:
        run(villain, items, weapons, score, points)


def win_or_lose(score):
    if score < 5:
        print_pause(f'Sorry you lost the game, your score is {score}.')
    else:
        print_pause(f'Yayy! You won. Your score is {score}.')

    print_pause('\nGAME OVER!!!\n')


def main(villain, items, weapons, score, points):
    print_pause('')
    print_pause('Enter 1 to knock on the door of '
                'the house.')
    print_pause('Enter 2 to peer into the cave.')
    print('What would you like to do?')
    cave_or_door(villain, items, weapons, score, points)


def play_again(score):
    answer = input('Would you like to play again? (y/n)')

    if answer == 'n':
        print_pause('Thanks for playing! See you next time.')
    elif answer == 'y':
        print_pause('Excellent! Restarting the game ...')
        play_game()
    else:
        play_again(score)


def play_game():
    villain = random.choice(['troll', 'gorgon', 'dragon',
                             'wicked faerie', 'pirate'])
    items = []
    weapons = random.choice(["Sword of Ogoroth", "Sword of Excalibur",
                             "Hammer of Thor", "Lightning Bolt of Zeus",
                             "Trident of Poseidon"])
    score = 0
    points = random.randint(1, 5)
    intro(villain)
    main(villain, items, weapons, score, points)


play_game()
