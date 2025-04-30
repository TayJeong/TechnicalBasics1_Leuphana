import time

exp_to_levelUp = 25
initial_hp = 20
levelUp_hp_increase = 5
hunt_hp_decrease = 10
hunt_exp_increase = 10

def type_effect(text, delay=0.05):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()  # 줄 바꿈

def hunting(lv, hp, exp):
    if lv < 2:
        print('⚠️you are not allowed to go hunting⚠️\n')
        print('Level up to at least 2!\n')
    else:
        hp -= 10
        exp += 10
        print("Hunting")
        time.sleep(1.5)
        print(f'You have {hp}HP left.')
    return hp, exp

def exit_confirm(user):
    while True:
        last_choice=input(f'{user}, R U really want to exit? (y/n) : ')
        if last_choice == 'y': # game finish
            type_effect("Goodbye~👋", 0.02)
            time.sleep(1)
            return True
        elif last_choice == 'n': #still game
            type_effect("Back to game!", 0.02)
            time.sleep(0.5)
            return False
        else:
            print("❗ Please enter only 'y' or 'n'❗")

def level_up(user, lv, hp, exp):
    if exp >= 25:
        lv += 1
        exp = 0
        hp += 5
        time.sleep(1)
        type_effect(f'🎉{user} level is now Lv.{lv}🎉', 0.02)
    return lv, hp, exp

def game_over_hp(user, hp):
    if hp == 0:
        type_effect(f"\n💀{user}'s HP is 0. Game over💀", 0.02)
        time.sleep(1.5)
        return True
    elif hp < 0:
        type_effect(f"\n💀{user}'s HP is under 0. Game over💀", 0.02)
        time.sleep(1.5)
        return True

    return False # game keep going


def main():
    exit_game = False
    user = input('put the name : ')
    type_effect(f'hello, {user}! 🌟Welcome to the Adventure Land🌟')
    time.sleep(1)

    lv = 1
    hp = initial_hp
    exp = 0

    while True:
        type_effect('\nWhat would you like to do?', 0.03)
        choice = input('a : Go hunting, b : Train, c : Exit the game\n')
        if choice == 'a': # huntiong
            hp, exp = hunting(lv, hp, exp)

        elif choice == 'b': # training
            type_effect(f'📊Your status level : {lv}, hp : {hp}, exp : {exp}.', 0.03)
            time.sleep(1)

            while True:
                choice2 = input('\n1. eat, 2.sleep, 3.exercise, 4.check condition, 5.exit🔙\n')

                if not choice2.isdigit() or int(choice2) not in range(1,6):
                    print("Please enter a number between 1 and 5.")
                    continue

                choice2 = int(choice2)

                if choice2 == 1:
                    hp += 5
                    print(f'🍖{user}, eats🍖 hp : {hp}')

                elif choice2 == 2:
                    hp += 10
                    exp += 5
                    print(f'💤{user}, sleeps💤 hp : {hp}, exp : {exp}')

                elif choice2 == 3:
                    exp += 20
                    hp -= 5
                    print(f'🏋️{user}, exercises🏋 hp : {hp}, exp : {exp}')

                elif choice2 == 4:
                    print(f'{user}📊 hp : {hp}, exp : {exp}, level : {lv}')

                elif choice2 == 5:
                    print('Back to main menu.')
                    time.sleep(1)
                    break

                lv, hp, exp = level_up(user, lv, hp, exp)

        elif choice == 'c':
            exit_game = exit_confirm(user)
            if exit_game:
                break

        else:
            print('please choose a valid option : a, b or c')

        if game_over_hp(user, hp):
            break

if __name__ == '__main__':
    main()