'''
최소 10개의 조건문과 5개의 사용자 입력을 포함합니다.
적어도 하나의 조건문이 다른 조건문 안에 중첩되어 있다
사용자 입력 중 하나는 특정 범위 내의 숫자여야 하며,
귀하의 코드는 사용자 입력이 1) 유효한 숫자 2) 귀하가 정의한 범위 내에 있는지 확인해야 합니다.
사용자 입력이 요구 사항을 충족하지 않으면 다시 입력을 요청하십시오.
시간 지연을 사용하여 대화형 경험을 개선합니다.
사용자 입력이 다른 것으로 이어지는 지점이 적어도 하나 이상 있어야 합니다.

Bonus

일부 인쇄 기능에 타이핑 효과를 추가하여 서스펜스를 추가하세요
당신이 마음대로 사용할 수 있는 모든 UTF-8 캐릭터를 가지고 있다는 것을 기억하세요,
그러니 창의력을 발휘하고 마음껏 가세요!
'''
import time

def type_effect(text, delay=0.05):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()  # 줄 바꿈

exit_game = False

while True:
    user = input('put the name : ')
    type_effect(f'hello, {user}! 🌟Welcome to the Adventure Land🌟')
    time.sleep(1)

    lv = 1
    hp = 20
    exp = 0

    while True:
        type_effect('\nWhat would you like to do?', 0.03)
        choice = input('a : Go hunting, b : Train, c : Exit the game\n')
        if choice == 'a': # 사냥하기
            if lv < 2:
                print('⚠️you are not allowed to go hunting⚠️\n')
                print('Level up to at least 2!\n')
                # 다시 누르기
            else:
                hp -= 10
                exp += 10
                print("Hunting...")
                time.sleep(1.5)
                print(f'You have {hp}HP left.')

        elif choice == 'b': # 기본능력치 올리기
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

                if exp >= 25:
                    lv += 1
                    exp = 0
                    hp += 5
                    time.sleep(1)
                    type_effect(f'🎉{user} level is now Lv.{lv}🎉', 0.02)


        elif choice == 'c':
            while True:
                last_choice=input(f'{user}, R U really want to exit? (y/n) : ')
                if last_choice.lower() == 'y':
                    type_effect("Goodbye~👋", 0.02)
                    time.sleep(1)
                    exit_game = True
                    break
                elif last_choice.lower() == 'n':
                    type_effect("Back to game!", 0.02)
                    time.sleep(0.5)
                    break
                else:
                    print("❗ Please enter only 'y' or 'n'❗")
        else:
            print('please choose a valid option : a, b or c')

        if hp == 0:
            type_effect(f"\n💀{user}'s HP is 0. Game over💀", 0.02)
            time.sleep(1.5)
            break
            ß
        if hp < 0:
            type_effect(f"\n💀{user}'s HP is under 0. Game over💀", 0.02)
            time.sleep(1.5)
            break

        if exit_game:
            break
    break


