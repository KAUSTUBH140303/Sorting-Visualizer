import pygame, random, time, sys

## Initializing Pygame
pygame.init()

####################################################################
## GLOBAL VARIABLES
## Colors Used in the Visualization
##          R       G       B
BLACK =    (0,      0,      0)
WHITE =    (255,    255,    255)
RED =      (255,    0,      0)
BLUE =     (0,      0,      255)
GREEN =    (0,      255,    0)
GREY =     (200,    200,    200)

## The Font used in the buttons is Georgia.
## This is matter of choice but the label positions
## need to be changed according to the font and its size.
FONT = pygame.font.SysFont("georgia", 21)
#####################################################################


######################################################################
## Window Creation
win = pygame.display.set_mode((1500, 750))
pygame.display.set_caption("Sorting Visualizer")
#######################################################################


#######################################################################
## Properties of each bar
class Bar:
	def __init__(self, height, color):
		self.height = height
		self.color = BLACK
		pass

	def makeBar(self, win, p):
		pygame.draw.rect(win, self.color, (40 + p, 120, 8, self.height))

########################################################################


#######################################################################
## UTILITY FUNCTIONS
########################################################################
def makeArray(): ## This is to create new array.
	array = []
	p = 200
	for i in range(158):
		x = random.randint(1, 600)
		bar = Bar(x, BLACK)
		array.append(bar)
		p += 1
	return array
#######################################################################

#######################################################################
def drawBoard(win, array): ## This creates the entire screen all over.
	win.fill(WHITE)
	pygame.draw.rect(win, BLACK, (0, 0, 1500, 100)) ## Dashboard
	## Buttons
	pygame.draw.rect(win, GREY, (25, 25, 200, 50)) ## Create New Array
	text = FONT.render("Create New Array", 1, BLACK)
	win.blit(text, (45, 37))
	pygame.draw.rect(win, GREY, (1250, 25, 200, 50)) ## Bubble Sort
	text = FONT.render("Bubble Sort", 1, BLACK)
	win.blit(text, (1300, 37))
	pygame.draw.rect(win, GREY, (1000, 25, 200, 50)) ## Merge Sort
	text = FONT.render("Merge Sort", 1,BLACK)
	win.blit(text, (1050, 37))
	pygame.draw.rect(win, GREY, (750, 25, 200, 50)) ## Insertion Sort
	text = FONT.render("Insertion Sort", 1, BLACK)
	win.blit(text, (780, 37))
	pygame.draw.rect(win, GREY, (500, 25, 200, 50)) ## Quick Sort
	text = FONT.render("Quick Sort", 1, BLACK)
	win.blit(text, (550, 37))
	pygame.draw.rect(win, GREY, (250, 25, 200, 50)) ## Heap Sort
	text = FONT.render("Heap Sort", 1, BLACK)
	win.blit(text, (300, 37))
	## Create Array and display it on the screen
    ## This is equivalent to mapping array of divs in JS
	p = 0
	for bar in array:
		bar.makeBar(win, p)
		p += 9
	pygame.display.update()
#####################################################################

#####################################################################
def handleClick(win, x, y, array): ## Function to handle clicks
	if x >= 25 and x <= 225 and y >= 25 and y <= 75:
		main(win)
	elif x >= 1000 and x <= 1200 and y >= 25 and y <= 75:
		mergeSort(win, array, 0, len(array) - 1)
	elif x >= 1250 and x <= 1450 and y >= 25 and y <= 75:
		bubbleSort(win, array)
	elif x >= 750 and x <= 950 and y >= 25 and y <= 75:
		insertionSort(win, array)
	elif x >= 500 and x <= 700 and y >= 25 and y <= 75:
		quickSort(win, array, 0, len(array) - 1)
	elif x >= 250 and x <= 450 and y >= 25 and y <= 75:
		heapSort(win, array)

######################################################################
######################################################################
######################################################################

## SORTING ALGORITHMS

#####################################################################
## Bubble Sort
#####################################################################
def bubbleSort(win, array):
	for i in range(len(array) - 1):
		for j in range(len(array) - i - 1):
			x = array[j].height
			y = array[j + 1].height
			if x > y:
				array[j], array[j + 1] = array[j + 1], array[j]
			array[j].color = RED
			array[j + 1].color = GREEN
			drawBoard(win, array)
			array[j].color = BLACK
			array[j + 1].color = BLACK
#####################################################################
## Insertion Sort
#####################################################################
def insertionSort(win, array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >=0 and key.height < array[j].height :
                array[j].color = RED
                array[j + 1].color = GREEN
                drawBoard(win, array)
                array[j].color = BLACK
                array[j + 1].color = BLACK
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key
#####################################################################
## Merge Sort and related functions
#####################################################################
def mergeSort(win, array, l, r):
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(win, array, l, m)
        mergeSort(win, array, m + 1, r)
        merge(array, l, m, r, win)

def merge(arr, l, m, r, win):
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1) 
    R = [0] * (n2)  
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j]  
    i = 0 
    j = 0 
    k = l
    while i < n1 and j < n2 : 
        if L[i].height <= R[j].height: 
            arr[k] = L[i] 
            i += 1
            arr[k].color = GREEN
            drawBoard(win, arr)
            arr[k].color = BLACK
        else: 
            arr[k] = R[j] 
            j += 1
            arr[k].color = GREEN
            drawBoard(win, arr)
            arr[k].color = BLACK
        k += 1
        time.sleep(0.02)
    while i < n1: 
        arr[k] = L[i]
        arr[k].color = GREEN
        drawBoard(win, arr)
        arr[k].color = BLACK 
        i += 1
        k += 1
    while j < n2: 
        arr[k] = R[j]
        arr[k].color = GREEN
        drawBoard(win, arr)
        arr[k].color = BLACK
        j += 1
        k += 1
###############################################################
## Quick Sort and related functions
###############################################################
def partition(win, arr, low, high): 
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):  
        if arr[j].height <= pivot.height: 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i].color = GREEN
            arr[j].color = GREEN
            drawBoard(win, arr)
            arr[i].color = BLACK
            arr[j].color = BLACK
            time.sleep(0.01)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    drawBoard(win, arr)
    return (i+1) 

def quickSort(win, arr, low, high): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
        pi = partition(win, arr, low, high) 
        quickSort(win, arr, low, pi-1) 
        quickSort(win, arr, pi+1, high)
##############################################################
## Heap Sort and related functions
##############################################################
def heapify(win, arr, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i].height < arr[l].height: 
        largest = l
        arr[i].color = GREEN
        arr[0].color = GREEN
        drawBoard(win, arr)
        arr[i].color = BLACK
        arr[0].color = BLACK
    if r < n and arr[largest].height < arr[r].height: 
        largest = r
        arr[i].color = GREEN
        arr[0].color = GREEN
        drawBoard(win, arr)
        arr[i].color = BLACK
        arr[0].color = BLACK
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]
        arr[i].color = GREEN
        arr[0].color = GREEN
        heapify(win, arr, n, largest)
        drawBoard(win, arr)
        arr[i].color = BLACK
        arr[0].color = BLACK

def heapSort(win, arr): 
    n = len(arr)  
    for i in range(n // 2 - 1, -1, -1): 
        heapify(win, arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]
        arr[i].color = GREEN
        arr[0].color = GREEN
        arr[i].color = BLACK
        arr[0].color = BLACK
        heapify(win, arr, i, 0)
############################################################
############################################################

## MAIN FUNCTION
def main(win):
	run = True ## To handle Game Loop
	array = makeArray() ## The main array
	drawBoard(win, array) ## To create the main screen
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
			if pygame.mouse.get_pressed()[0]:
				x, y = pygame.mouse.get_pos()
				handleClick(win, x, y, array)
main(win)


"""
This is a visulaization of some of the most famous sorting algorithms.
These include-
1. Bubble Sort
2. Selection Sort
3. Merge Sort
4. Insertion Sort
5. Quick Sort
6. Heap Sort
The screen size is 1500px in width and 750px in height. These
are arbitrary numbers and the window seemed to fit perfectly 
on my device screen.
The number of array elements is 158. I experimented with larger
values like 1100 and 1300, and although it looked better visually, 
the window kept freezing mid-algorithm due to the large array size.
Each array bar is 8px wide and this too is a result of experimentation.
In some algorithms like merge sort, I have used time delay. This is 
due to fast speed of those algorithms and the animations looked
better when slower.
Explantions for each algorithm can be found on GeeksForGeeks.
"""