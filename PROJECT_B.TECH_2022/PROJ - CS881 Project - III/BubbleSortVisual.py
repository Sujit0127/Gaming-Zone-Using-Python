import pygame



#Initialise pygame window
pygame.init()
array1 = ""
array =[]
#Define screen dimensions, declare font for viewing text
screen = pygame.display.set_mode((700,500))
font = pygame.font.SysFont('ubuntu mono', 20)
run = True

#Initially fill the screen black
screen.fill((0,0,0,0))
block =  font.render("                                           Visualization Of Bubble Sort by Project Group - 2", True, (255,0,150))
screen.blit(block, (0,20))
block1 =  font.render("""                                                Enter Input and press ENTER to visualize""", True, (255,255,150))
screen.blit(block1, (0,40))
block2 =  font.render("                                       Add comma to separate the integers and backspace to pop", True, (255,255,150))
screen.blit(block2, (0,60))
pygame.display.update()



#Function to show text
def show_text(array):  
   #Create a new screen
   screen.fill((0,0,150,0))
   #Use the font to display the array
   block =  font.render(str(array), True, (255,255,150))
   #Display the array
   screen.blit(block, (20,20))

#Function to draw rectangles
def draw_rect():
   for i in range(len(array)):
       #Draw rectangles using array elements
       #To maintain gaps between rectangles, mention the top coordinate more than the width
       pygame.draw.rect(screen, (255, 125, 0),((50+i*25,50, 20, array[i]*2)))
   pygame.display.update()

#Function to implement bubble sort Implementer using PyGame
def bubble_sort():
   for i in range(len(array)):
       for j in range(len(array)-1):
           #Compare every element with every other element and switch places
           if array[j] > array[j+1]:
               array[j], array[j+1] = array[j+1], array[j]
       #Display the array 
       array1 = [str(i) for i in array]
       array1=",".join(array1)
       show_text(array1)
       #Draw the rectangular boxes
       draw_rect()
       #Keep a delay between changes
       pygame.time.delay(500)
       #Display the changes made
       pygame.display.update()



#Since changes keep happening, a loop is used
while run == True: 
   #Detect keyboard press
   for event in pygame.event.get():
       #Keyboard press condition
       if event.type == pygame.KEYDOWN:
           #Spacebar press
           if event.key == pygame.K_RETURN:
               #Start visualising and sorting
               #Convert string to array by splitting the string
               array = array1.split(",")
               array = [int(i) for i in array]
               draw_rect()
               pygame.time.delay(3000)
               bubble_sort()
           elif event.key == pygame.K_BACKSPACE:
               #Remove last element in case of any changes
               array1 = array1[:-1]
           else:
               #Check if the keyboard press is a digit
                   array1+=event.unicode
                   show_text(array1)
                   pygame.display.update()
       #Check if pygame exit is selected
       elif event.type == pygame.QUIT:
               run= False




#Quit and close the window
pygame.quit()