import sys
import os
import random
import msvcrt


"""
an implentation of 2048 game 
to do : flush the output 
        set the end of the game(when score get 2048)
"""
ui = '|  %4s  |  %4s  |  %4s  |  %4s  |\n|  %4s  |  %4s  |  %4s  |  %4s  |\n|  %4s  |  %4s  |  %4s  |  %4s  |\n|  %4s  |  %4s  |  %4s  |  %4s  |\n'
new_numbers = ['2','4']

def usage():
    usage_line = "use the arrow key to control the direction, press q to exit\n"
    print(usage_line)
def draw_ui(status):
    print(ui % tuple(status), flush= True)

def judge(status, idx):
    if status[idx] == '2048':
        print('congratulations! You have got 2048')
        exit()

def init():
    idx1 = random.randint(0, 15)
    idx2 = random.randint(0, 15)
    while idx2 == idx1:
        idx2 = random.randint(0, 15)
    status = [' '] * 16
    new_number = new_numbers[random.randint(0, 1)]
    status[idx1] = new_number
    new_number = new_numbers[random.randint(0, 1)]
    status[idx2] = new_number
    return status

def move_left(status):
    has_moved = False
    for height in range(4):
        merged_location = dict([(i, False) for i in range(4)])
        for width in range(4):
            if width == 0:
                continue
            idx = width
            while True:
                if idx == 0 or status[height * 4 + idx] == ' ':
                    break

                if status[height * 4 + idx - 1] == ' ':
                    status[height * 4 + idx - 1] = status[height * 4 + idx]
                    status[height * 4 + idx] = ' '
                    merged_location[idx - 1] = merged_location[idx]
                    merged_location[idx] = False
                    has_moved = True
                elif status[height * 4 + idx - 1] != ' ' and status[height * 4 + idx - 1] == status[height * 4 + idx]:
                    if merged_location[idx] == True or merged_location[idx - 1] == True:
                        break
                    status[height * 4 + idx - 1] = str(int(status[height * 4 + idx]) * 2)
                    judge(status, height * 4 + idx - 1)
                    merged_location[idx - 1] = True
                    status[height * 4 + idx] = ' '
                    has_moved = True


                elif status[height * 4 + idx - 1] != ' ' and status[height * 4 + idx - 1] != status[height * 4 + idx]:
                    break
                idx -= 1
    empty_idx = [idx for idx in range(16) if status[idx] == ' ']
    new_number = new_numbers[random.randint(0, 1)]
    new_idx = empty_idx[random.randint(0, len(empty_idx) - 1)]
    if has_moved:
        status[new_idx] = new_number


def move_right(status):
    has_moved = False
    for height in range(4):
        merged_location = dict([(i, False) for i in range(4)])
        for width_left in range(4):
            width = 3 - width_left
            if width == 3:
                continue
            idx = width
            while True:
                if idx == 3 or status[height * 4 + idx] == ' ':
                    break

                if status[height * 4 + idx + 1] == ' ':
                    status[height * 4 + idx + 1] = status[height * 4 + idx]
                    status[height * 4 + idx] = ' '
                    merged_location[idx + 1] = merged_location[idx]
                    merged_location[idx] = False
                    has_moved = True
                elif status[height * 4 + idx + 1] != ' ' and status[height * 4 + idx + 1] == status[height * 4 + idx]:
                    if merged_location[idx] == True or merged_location[idx + 1] == True:
                        break
                    status[height * 4 + idx + 1] = str(int(status[height * 4 + idx]) * 2)
                    judge(status, height * 4 + idx + 1)
                    merged_location[idx + 1] = True
                    status[height * 4 + idx] = ' '
                    has_moved = True

                elif status[height * 4 + idx + 1] != ' ' and status[height * 4 + idx + 1] != status[height * 4 + idx]:
                    break
                idx += 1
    empty_idx = [idx for idx in range(16) if status[idx] == ' ']
    new_number = new_numbers[random.randint(0, 1)]
    new_idx = empty_idx[random.randint(0, len(empty_idx) - 1)]
    if has_moved:
        status[new_idx] = new_number

def move_up(status):
    has_moved = False
    for width in range(4):
        merged_location = dict([(i, False) for i in range(4)])
        for height in range(4):

            if height == 0:
                continue
            idx = height
            while True:
                if idx == 0 or status[idx  * 4 + width] == ' ':
                    break

                if status[(idx - 1)* 4 + width] == ' ':
                    status[(idx - 1) * 4 + width ] = status[idx * 4 + width]
                    status[idx * 4 + width] = ' '
                    merged_location[idx - 1] = merged_location[idx]
                    merged_location[idx] = False
                    has_moved = True
                elif status[(idx  - 1)* 4 + width ] != ' ' and status[(idx - 1) * 4 + width] == status[idx * 4 + width]:
                    if merged_location[idx] == True or merged_location[idx - 1] == True:
                        break
                    status[(idx - 1) * 4 + width ] = str(int(status[idx * 4 + width]) * 2)
                    judge(status, (idx - 1) * 4 + width)
                    merged_location[idx - 1] = True
                    status[idx * 4 + width] = ' '
                    has_moved = True

                elif status[(idx - 1) * 4 +  width] != ' ' and status[(idx - 1) * 4 + width] != status[idx * 4 + width]:
                    break
                idx -= 1
    empty_idx = [idx for idx in range(16) if status[idx] == ' ']
    new_number = new_numbers[random.randint(0, 1)]
    new_idx = empty_idx[random.randint(0, len(empty_idx) - 1)]
    if has_moved:
        status[new_idx] = new_number

def move_down(status):
    has_moved = False
    for width in range(4):
        merged_location = dict([(i, False) for i in range(4)])
        for height_up in range(4):
            height = 3 - height_up
            if height == 3:
                continue
            idx = height
            while True:
                if idx == 3 or status[idx  * 4 + width] == ' ':
                    break

                if status[(idx + 1)* 4 + width] == ' ':
                    status[(idx + 1) * 4 + width ] = status[idx * 4 + width]
                    status[idx * 4 + width] = ' '
                    merged_location[idx + 1] = merged_location[idx]
                    merged_location[idx] = False
                    has_moved = True
                elif status[(idx  + 1)* 4 + width ] != ' ' and status[(idx + 1) * 4 + width] == status[idx * 4 + width]:
                    if merged_location[idx] == True or merged_location[idx + 1] == True:
                        break
                    status[(idx + 1) * 4 + width ] = str(int(status[idx * 4 + width]) * 2)
                    judge(status, (idx + 1) * 4 + width)
                    merged_location[idx + 1] = True
                    status[idx * 4 + width] = ' '
                    has_moved = True

                elif status[(idx + 1) * 4 +  width] != ' ' and status[(idx + 1) * 4 + width] != status[idx * 4 + width]:
                    break
                idx += 1
    empty_idx = [idx for idx in range(16) if status[idx] == ' ']
    new_number = new_numbers[random.randint(0, 1)]
    new_idx = empty_idx[random.randint(0, len(empty_idx) - 1)]
    if has_moved:
        status[new_idx] = new_number


def move(status, direction):
    if direction == 'left':
        move_left(status)
    elif direction == 'right':
        move_right(status)
    elif direction == 'up':
        move_up(status)
    elif direction == 'down':
        move_down(status)

def abd(a_list):
    a_list[0] = '3'


if __name__ == '__main__':
    usage()
    status = init()
    # status = ['4', ' ', '2', '2',
    #           ' ', ' ', '2', ' ',
    #           ' ', '2', '2', '4',
    #           '2', ' ', '2', '4']
    # status = ['1024', '1024', ' ', ' ',
    #           ' ', ' ', ' ', ' ',
    #           ' ', ' ', ' ', ' ',
    #           ' ' ,' ' , ' ', ' ']
    draw_ui(status)
    # move(status, 'left')
    # draw_ui(status)
    # move(status, 'right')
    # draw_ui(status)
    # move(status, 'up')
    # draw_ui(status)
    # move(status, 'left')
    # draw_ui(status)
    # move(status, 'down')
    # draw_ui(status)

    while True:
        key = msvcrt.getch()
        if key == b'q':
            exit()

        if key == b'K':   # left
            print('left')
            move(status, 'left')
            #draw_ui(status)
            print(ui % tuple(status), flush=True)
            sys.stdout.flush()
        if key == b'M':   # right
            print('right')
            move(status, 'right')
            #draw_ui(status)
            print(ui % tuple(status), flush=True)
            sys.stdout.flush()
        if key == b'H':   # up
            print('up')
            move(status, 'up')
            print(ui % tuple(status), flush=True)
            sys.stdout.flush()
            #draw_ui(status)
        if key == b'P':   # down
            print('down')
            move(status, 'down')
            #draw_ui(status)
            print(ui % tuple(status), flush=True)
            sys.stdout.flush()
