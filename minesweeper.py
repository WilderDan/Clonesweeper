import pygame
import random

################################################################################
###User Difficulty##############################################################
################################################################################
difficulty = raw_input("Choose difficulty: [    'baby'     'easy'     'medium'     'hard'     'master'     'insane'    ]\n  ==> ")


if difficulty == 'baby':
    num_tiles_height = 5 # number of tiles in each column
    num_tiles_width = 8  # number of tiles in each row
    num_of_mines = 3

if difficulty == 'easy':
    num_tiles_height = 9 # number of tiles in each column
    num_tiles_width = 9  # number of tiles in each row
    num_of_mines = 10


if difficulty == 'medium':
    num_tiles_height = 16 # number of tiles in each column
    num_tiles_width = 16  # number of tiles in each row
    num_of_mines = 40

if difficulty == 'hard':
    num_tiles_height = 16 # number of tiles in each column
    num_tiles_width = 30  # number of tiles in each row
    num_of_mines = 99

if difficulty == 'master':
    num_tiles_height = 30 # number of tiles in each column
    num_tiles_width = 30  # number of tiles in each row
    num_of_mines = 230

if difficulty == 'insane':
    num_tiles_height = 30 # number of tiles in each column
    num_tiles_width = 60  # number of tiles in each row
    num_of_mines = 600

################################################################################
###Housekeeping#################################################################
################################################################################

screen_height = (num_tiles_height * 21) # The tiles will be 20 x 20 so screen dimensions must take that into account.
screen_width = (num_tiles_width * 21)  # 21 instead of 20 is so the tiles will have a slight distance between each other.

size=[screen_width, screen_height]
screen=pygame.display.set_mode(size)

pygame.display.set_caption('Clonesweeper. Made by Dan Wilder')



################################################################################
###Graphic files################################################################
################################################################################
tile = pygame.image.load('tile.png').convert()
flag = pygame.image.load('flag.png').convert()
misplaced_flag = pygame.image.load('misplaced_flag.png').convert()
question = pygame.image.load('question.png').convert()

joke = pygame.image.load('joke.png').convert()

empty_tile = pygame.image.load('empty_tile.png').convert()

one = pygame.image.load('one.png').convert()
two = pygame.image.load('two.png').convert()
three = pygame.image.load('three.png').convert()
four = pygame.image.load('four.png').convert()
five = pygame.image.load('five.png').convert()
six = pygame.image.load('six.png').convert()
seven = pygame.image.load('seven.png').convert()
eight = pygame.image.load('eight.png').convert()

mine_image = pygame.image.load('mine.png').convert()
exploded_mine = pygame.image.load('exploded_mine.png').convert()

################################################################################
###Lists to be used#############################################################
################################################################################
grid_list = [] # List of *all* coordinates

potential_mine_list = []
mine_list = []
not_mine_list = []
revealed_list = []
flag_list = []
question_list = []

zero_list = []
one_list = []
two_list = []
three_list = []
four_list = []
five_list = []
six_list = []
seven_list = []
eight_list = []
mine_image_list = []

x_coord_to_append = 1 # Counter value for grid_list
y_coord_to_append = 1 # Counter value for grid_list

done = False # Tag to determine whether game is done or not

gameover = False # Allows input if false

################################################################################
###Functions####################################################################
################################################################################

def start_up():
    print ('')
    print('========================================')
    print ('New Game!!!')
    print('========================================')
    print ('{0} {1}').format('Difficulty set to:', difficulty)
    print ("Press the 'esc' key to exit")
    print ("Press the 'n' key to start a new game")

    for i in range (len (grid_list) ): # potential_mine_list
        potential_mine_list.append(grid_list[i])


    for i in range (num_of_mines): # mine_list
        mine = random.choice(potential_mine_list)
        potential_mine_list.remove(mine)
        mine_list.append(mine)


    for i in range ( len(grid_list) ): # not_mine_list
        if mine_list.__contains__(grid_list[i]) == False:
            not_mine_list.append(grid_list[i])

def count_unrevealed_neighbors (x, y):
            unrevealed_neighbors = 0

            if revealed_list.__contains__( (x - 1, y - 1) ) == False:
                if grid_list.__contains__( (x - 1, y - 1) ) == True:
                    if flag_list.__contains__( (x - 1, y - 1) ) == False:
                        unrevealed_neighbors += 1

            if revealed_list.__contains__( (x, y - 1) ) == False:
                if grid_list.__contains__( (x , y - 1) ) == True:
                    if flag_list.__contains__( (x, y - 1) ) == False:
                        unrevealed_neighbors += 1

            if revealed_list.__contains__( (x + 1, y - 1) ) == False:
                if grid_list.__contains__( (x + 1, y - 1) ) == True:
                    if flag_list.__contains__( (x + 1, y - 1) ) == False:
                        unrevealed_neighbors += 1

            if revealed_list.__contains__( (x - 1, y) ) == False:
                if grid_list.__contains__( (x - 1, y ) ) == True:
                    if flag_list.__contains__( (x - 1, y ) ) == False:
                        unrevealed_neighbors += 1

            if revealed_list.__contains__( (x + 1, y) ) == False:
                if grid_list.__contains__( (x + 1, y ) ) == True:
                    if flag_list.__contains__( (x + 1, y ) ) == False:
                        unrevealed_neighbors += 1

            if revealed_list.__contains__( (x - 1, y + 1) ) == False:
                if grid_list.__contains__( (x - 1, y + 1) ) == True:
                    if flag_list.__contains__( (x - 1, y + 1) ) == False:
                        unrevealed_neighbors += 1

            if revealed_list.__contains__( (x, y + 1) ) == False:
                if grid_list.__contains__( (x, y + 1) ) == True:
                    if flag_list.__contains__( (x, y + 1) ) == False:
                        unrevealed_neighbors += 1

            if revealed_list.__contains__( (x + 1, y + 1) ) == False:
                if grid_list.__contains__( (x + 1, y + 1) ) == True:
                    if flag_list.__contains__( (x + 1, y + 1) ) == False:
                        unrevealed_neighbors += 1

            return (unrevealed_neighbors)

def count_neighbor_flags (x, y):
            neighbor_flags = 0

            if flag_list.__contains__( (x - 1, y - 1) ) == True:
                if grid_list.__contains__( (x - 1, y - 1) ) == True:
                    neighbor_flags += 1

            if flag_list.__contains__( (x, y - 1) ) == True:
                if grid_list.__contains__( (x , y - 1) ) == True:
                    neighbor_flags += 1

            if flag_list.__contains__( (x + 1, y - 1) ) == True:
                if grid_list.__contains__( (x + 1, y - 1) ) == True:
                    neighbor_flags += 1

            if flag_list.__contains__( (x - 1, y ) ) == True:
                if grid_list.__contains__( (x - 1, y ) ) == True:
                    neighbor_flags += 1

            if flag_list.__contains__( (x + 1, y ) ) == True:
                if grid_list.__contains__( (x + 1, y ) ) == True:
                    neighbor_flags += 1

            if flag_list.__contains__( (x - 1, y + 1) ) == True:
                if grid_list.__contains__( (x - 1, y + 1) ) == True:
                    neighbor_flags += 1

            if flag_list.__contains__( (x, y + 1) ) == True:
                if grid_list.__contains__( (x, y + 1) ) == True:
                    neighbor_flags += 1

            if flag_list.__contains__( (x + 1, y + 1) ) == True:
                if grid_list.__contains__( (x + 1, y + 1) ) == True:
                    neighbor_flags += 1

            return (neighbor_flags)

def neighbor_reveal(x, y):
            if revealed_list.__contains__( (x - 1, y - 1) ) == False:
                if flag_list.__contains__( (x - 1, y - 1) ) == False:
                    if question_list.__contains__( (x - 1, y - 1) ) == False:
                        new_coordinates = (x - 1, y - 1)
                        reveal(new_coordinates)
            if revealed_list.__contains__( (x, y - 1) ) == False:
                if flag_list.__contains__( (x, y - 1) ) == False:
                    if question_list.__contains__( (x, y - 1) ) == False:
                        new_coordinates = (x, y - 1)
                        reveal(new_coordinates)
            if revealed_list.__contains__( (x + 1, y - 1) ) == False:
                if flag_list.__contains__( (x + 1, y - 1) ) == False:
                    if question_list.__contains__( (x + 1, y - 1) ) == False:
                        new_coordinates = (x + 1, y - 1)
                        reveal(new_coordinates)

            if revealed_list.__contains__( (x - 1, y) ) == False:
                if flag_list.__contains__( (x - 1, y) ) == False:
                    if question_list.__contains__( (x - 1, y) ) == False:
                        new_coordinates = (x - 1, y)
                        reveal(new_coordinates)
            if revealed_list.__contains__( (x + 1, y) ) == False:
                if flag_list.__contains__( (x + 1, y) ) == False:
                    if question_list.__contains__( (x + 1, y) ) == False:
                        new_coordinates = (x + 1, y)
                        reveal(new_coordinates)

            if revealed_list.__contains__( (x - 1, y + 1) ) == False:
                if flag_list.__contains__( (x - 1, y + 1) ) == False:
                    if question_list.__contains__( (x - 1, y + 1) ) == False:
                        new_coordinates = (x - 1, y + 1)
                        reveal(new_coordinates)
            if revealed_list.__contains__( (x, y + 1) ) == False:
                if flag_list.__contains__( (x, y + 1) ) == False:
                    if question_list.__contains__( (x, y + 1) ) == False:
                        new_coordinates = (x, y + 1)
                        reveal(new_coordinates)
            if revealed_list.__contains__( (x + 1, y + 1) ) == False:
                if flag_list.__contains__( (x + 1, y + 1) ) == False:
                    if question_list.__contains__( (x + 1, y + 1) ) == False:
                        new_coordinates = (x + 1, y + 1)
                        reveal(new_coordinates)


def reveal(coordinates):
    if grid_list.__contains__(coordinates) == True:
        revealed_list.append(coordinates)
        number = count_neighbor_mines(coordinates[0], coordinates[1])

        if mine_list.__contains__(coordinates) == True:
            mine_image_list.append(coordinates)
            print('========================================')
            print ('Gameover!')
            print('========================================')

        elif number == 1:
            one_list.append(coordinates)
        elif number == 2:
            two_list.append(coordinates)
        elif number == 3:
            three_list.append(coordinates)
        elif number == 4:
            four_list.append(coordinates)
        elif number == 5:
            five_list.append(coordinates)
        elif number == 6:
            six_list.append(coordinates)
        elif number == 7:
            seven_list.append(coordinates)
        elif number == 8:
            eight_list.append(coordinates)
        elif number == 0:
            zero_list.append(coordinates)
            neighbor_reveal(coordinates[0], coordinates[1])


def draw_grid():
    for i in range ( len(grid_list) ):
        screen_x_pos = (grid_list[i][0] * 21 ) - 20
        screen_y_pos = (grid_list[i][1] * 21 ) - 20
        screen.blit(tile, [screen_x_pos, screen_y_pos])

def draw_flags():
    for i in range ( len(flag_list) ):
        screen_x_pos = (flag_list[i][0] * 21) - 20
        screen_y_pos = (flag_list[i][1] * 21) -20
        screen.blit(flag, [screen_x_pos, screen_y_pos])

def draw_question():
    for i in range ( len(question_list) ):
        screen_x_pos = (question_list[i][0] * 21) - 20
        screen_y_pos = (question_list[i][1] * 21) - 20
        screen.blit(question, [screen_x_pos, screen_y_pos])


def draw_empty():
    for i in range ( len(zero_list) ):
        screen_x_pos = (zero_list[i][0] * 21) - 20
        screen_y_pos = (zero_list[i][1] * 21) - 20
        screen.blit(empty_tile, [screen_x_pos, screen_y_pos] )

def draw_one():
    for i in range ( len(one_list) ):
        screen_x_pos = (one_list[i][0] * 21) - 20
        screen_y_pos = (one_list[i][1] * 21) - 20
        screen.blit(one, [screen_x_pos, screen_y_pos] )

def draw_two():
    for i in range ( len(two_list) ):
        screen_x_pos = (two_list[i][0] * 21) - 20
        screen_y_pos = (two_list[i][1] * 21) - 20
        screen.blit(two, [screen_x_pos, screen_y_pos] )

def draw_three():
    for i in range ( len(three_list) ):
        screen_x_pos = (three_list[i][0] * 21) - 20
        screen_y_pos = (three_list[i][1] * 21) - 20
        screen.blit(three, [screen_x_pos, screen_y_pos] )

def draw_four():
    for i in range ( len(four_list) ):
        screen_x_pos = (four_list[i][0] * 21) - 20
        screen_y_pos = (four_list[i][1] * 21) - 20
        screen.blit(four, [screen_x_pos, screen_y_pos] )

def draw_five():
    for i in range ( len(five_list) ):
        screen_x_pos = (five_list[i][0] * 21) - 20
        screen_y_pos = (five_list[i][1] * 21) - 20
        screen.blit(five, [screen_x_pos, screen_y_pos] )

def draw_six():
    for i in range ( len(six_list) ):
        screen_x_pos = (six_list[i][0] * 21) - 20
        screen_y_pos = (six_list[i][1] * 21) - 20
        screen.blit(six, [screen_x_pos, screen_y_pos] )

def draw_seven():
    for i in range ( len(seven_list) ):
        screen_x_pos = (seven_list[i][0] * 21) - 20
        screen_y_pos = (seven_list[i][1] * 21) - 20
        screen.blit(seven, [screen_x_pos, screen_y_pos] )

def draw_eight():
    for i in range ( len(eight_list) ):
        screen_x_pos = (eight_list[i][0] * 21) - 20
        screen_y_pos = (eight_list[i][1] * 21) - 20
        screen.blit(eight, [screen_x_pos, screen_y_pos] )

def draw_mine():
    for i in range ( len(mine_image_list) ):
        screen_x_pos = (mine_image_list[i][0] * 21) - 20
        screen_y_pos = (mine_image_list[i][1] * 21) - 20
        screen.blit(exploded_mine, [screen_x_pos, screen_y_pos] )

def draw_hidden_mine():
  if gameover == True:
    for i in range ( len(mine_list) ):
        if flag_list.__contains__( (mine_list[i][0], mine_list[i][1]) ) == False:
            screen_x_pos = (mine_list[i][0] * 21) - 20
            screen_y_pos = (mine_list[i][1] * 21) - 20
            screen.blit(mine_image, [screen_x_pos, screen_y_pos] )

def draw_misplaced_flags():
  if gameover == True:
    for i in range ( len(flag_list) ):
        if mine_list.__contains__( (flag_list[i][0], flag_list[i][1]) ) == False:
            screen_x_pos = (flag_list[i][0] * 21) - 20
            screen_y_pos = (flag_list[i][1] * 21) - 20
            screen.blit(misplaced_flag, [screen_x_pos, screen_y_pos] )


def draw_revealed():
    draw_empty()
    draw_one()
    draw_two()
    draw_three()
    draw_four()
    draw_five()
    draw_six()
    draw_seven()
    draw_eight()
    draw_misplaced_flags()
    draw_hidden_mine()
    draw_mine()


def count_neighbor_mines(x_coord, y_coord):
        number = 0

        if mine_list.__contains__((x_coord -1, y_coord)):
            number += 1
        if mine_list.__contains__((x_coord +1, y_coord)):
            number += 1
        if mine_list.__contains__((x_coord, y_coord - 1)):
            number += 1
        if mine_list.__contains__((x_coord, y_coord + 1)):
            number += 1
        if mine_list.__contains__((x_coord -1, y_coord - 1)):
            number += 1
        if mine_list.__contains__((x_coord -1, y_coord + 1)):
            number += 1
        if mine_list.__contains__((x_coord +1, y_coord - 1)):
            number += 1
        if mine_list.__contains__((x_coord +1, y_coord + 1)):
            number += 1

        return number

################################################################################
###Lists########################################################################
################################################################################

for i in range (num_tiles_height):  # grid_list
    for i in range (num_tiles_width):
        grid_list.append( (x_coord_to_append, y_coord_to_append) )
        x_coord_to_append += 1
    x_coord_to_append = 1
    y_coord_to_append += 1


start_up()


################################################################################
###Program Loop#################################################################
################################################################################
print('========================================')
print ('New Game!!!')
print('========================================')
print ('{0} {1}').format('Difficulty set to:', difficulty)
print ("Press the 'esc' key to exit")
print ("Press the 'n' key to start a new game")
print("Left click a revealed square for probability...")




while done != True: #Main Loop

    pos = pygame.mouse.get_pos() # Gets mouse coordinates
    mouse_x_pos = pos[0]
    mouse_y_pos = pos[1]

    x_coord = round ( (mouse_x_pos / 21) + 0.51 ) # x_coord of grid tile clicked
    y_coord = round ( (mouse_y_pos / 21) + 0.51 ) # y_coord of grid tile clicked
    coordinates = (x_coord, y_coord)

    for event in pygame.event.get():  # Code chunk to decide if to exit
        if event.type == pygame.QUIT: # Click window 'X'
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Press esc key
                done = True

            if event.key == pygame.K_n: # Press 'n' key
                potential_mine_list = []
                mine_list = []
                not_mine_list = []
                revealed_list = []
                flag_list = []
                question_list = []

                zero_list = []
                one_list = []
                two_list = []
                three_list = []
                four_list = []
                five_list = []
                six_list = []
                seven_list = []
                eight_list = []
                mine_image_list = []


                start_up()
                gameover = False


################################################################################
###Action#######################################################################
################################################################################

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
         # Left click
            if gameover == False:

                if revealed_list.__contains__(coordinates) == True:
                    neighbor_mines = float ( count_neighbor_mines(coordinates[0], coordinates[1]) )
                    neighbor_flags = float ( count_neighbor_flags(coordinates[0], coordinates[1]) )
                    hidden_neighbors = float ( count_unrevealed_neighbors(coordinates[0], coordinates[1]) )

                    if hidden_neighbors != 0:
                        probability = ( (neighbor_mines - neighbor_flags) / hidden_neighbors) * 100
                        # A negative probability implies a misplaced flag by the user
                        print ('')
                        print ('{0}{1} {2}').format(probability, '%', 'chance of hitting a mine')

                    else:
                        print ('')
                        print ('N/A')





                if revealed_list.__contains__(coordinates) == False:
                    if flag_list.__contains__(coordinates) == False:
                        if question_list.__contains__(coordinates) == False:
                            reveal(coordinates)
                            if len(revealed_list) == len(grid_list) - len(mine_list):
                                if len(flag_list) == num_of_mines:
                                    print ('')
                                    print ('You win!!!')
                                    gameover = True
                            if mine_list.__contains__(coordinates) == True:
                                gameover = True



        elif event.type == pygame.MOUSEBUTTONDOWN: # Right click
            if gameover == False:
                if revealed_list.__contains__(coordinates) == False:

                    if question_list.__contains__(coordinates) == True:
                        question_list.remove(coordinates)

                    elif flag_list.__contains__(coordinates) == True:
                        flag_list.remove(coordinates)
                        question_list.append(coordinates)

                    else:
                        flag_list.append(coordinates)
                        if len(revealed_list) == len(grid_list) - len(mine_list):
                            if len(flag_list) == num_of_mines:
                                print ('')
                                print ('You win!!!')
                                gameover = True


################################################################################
###Graphics#####################################################################
################################################################################

    draw_grid()
    draw_flags()
    draw_question()
    draw_revealed()

    pygame.display.flip()

pygame.quit()









