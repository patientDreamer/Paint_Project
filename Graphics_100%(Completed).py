from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter import filedialog          #Import libraries

root=Tk()
root.withdraw() 
font.init()

'''
The shortcut keys are setup for fun so conviencey
key1=pencil  z_key=pencil stamp
key2=eraser  x_key=calculator stamp
key3=lines   c_key=percent stamp
key4=brush   v_key=book stamp
key5=rectangle  b_key=backpack stamp
key6=spray
key7=circle
key8=polygon
'''


width,height=1100,750
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
CYAN=(50, 160, 168)
ORANGE=(255,165,0)
PURPLE=(137, 50, 168)
COFFEE=(208, 187, 148)
BROWN=(111,78,55)
CYAN=(50, 129, 168)
INDIGO=(66, 138, 245)
SKY=(0,206,230)
NAVY=(32,42,68)

count=0 #counter for music(mouse left click accumlator)
pos=0   #position for music playlist
myClock=time.Clock()
init()

#toolRects
background=image.load("graphics/J2.jpg")     #Import my_background
colors=image.load("graphics/Colors.chart.jpg")           #Import all the images that need a variable
pen_stamp=image.load("graphics/pencil_stamp.png")
cal_stamp=image.load("graphics/calculator.png")
text=image.load("graphics/text3.png")
percent_stamp=image.load("graphics/stamp3.png")
book_stamp=image.load("graphics/bookstamp.png")
backpack_stamp=image.load("graphics/backpack.png")



                        
#Adjusted labels
adj=transform.scale(background,(1100,750))
color_spec=transform.scale(colors, (93, 85))


tool_icons = [
             transform.scale(image.load("graphics/Pencil.jpg"),(60,60)),     #load my icons (graphics is my folder name,NOT an actual file)
             transform.scale(image.load("graphics/new_eraser.jpg"),(60,60)), #(That don't need variables)
             transform.scale(image.load("graphics/line_.jpg"),(60,60)),
             transform.scale(image.load("graphics/new_brush.jpg"),(60,60)),
             transform.scale(image.load("graphics/rect_tool.jpg"),(60,60)),
             transform.scale(image.load("graphics/spray.jpg"), (60, 60)),
             transform.scale(image.load("graphics/oval.png"),(60,60))
             ]


my_stamps = [
            transform.scale(image.load("graphics/pencil_stamp.jpg"),(60,60)),    #load my stamps in list to be more efficient
            transform.scale(image.load("graphics/calculator.jpg"),(60,60)),      #These don't need variables
            transform.scale(image.load("graphics/stamp3.jpg"),(60,60)),
            transform.scale(image.load("graphics/bookstamp.jpg"),(60,60)),
            transform.scale(image.load("graphics/backpack.jpg"),(60,60)),
            transform.scale(image.load("graphics/polygon.jpg"),(60,60))
            ]


#Stamps&tools shorcuts
stamps=["pencil stamp","calculator stamp", "percent stamp","book stamp","backpack stamp",]  #list of stamps(names)
png_files=[pen_stamp,cal_stamp,percent_stamp,book_stamp,backpack_stamp]     #list of stamp png files
keys_stamps=[K_z,K_x,K_c,K_v,K_b]#list of stamps keys(shortcuts)

keys_list=[K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8] #list of tool keys(shorcuts,except for undo/redo, trashcan)
my_tools=["pencil","eraser","line tool","brush tool","rectangle","spray paint","circle","polygon"]

#Musics playlist
my_BGM=["Musics/TenYears.mp3","Musics/Mercury record.mp3","Musics/piano.mp3"]

    
#make icons visible
screen.blit(adj,(0,0))
screen.blit(color_spec,(961,170))
left=image.load("graphics/left.jpg")
right=transform.flip(left,True,False)
pause=image.load("graphics/pause.jpg")
unpause=image.load("graphics/unpause.jpg")
screen.blit(pause,(435,93))
screen.blit(left,(395,95))
screen.blit(right,(480,95))
leftRect=Rect(395,95,35,35)
rightRect=Rect(480,95,35,35)
draw.rect(screen,BLACK,leftRect,3)
draw.rect(screen,BLACK,rightRect,3)

#Icon
X=435
Y=550
for icon in tool_icons:         #Use for loop to make the icons visible
    screen.blit(icon,(X,Y))
    X+=70
    
X=435
Y=620
for stamp in my_stamps:         #use for loop to make the stamps visible
    screen.blit(stamp,(X,Y))
    X+=70


#My program name
undoPic=transform.scale(image.load("graphics/undo.jpg"),(40,40))     #load undo
redoPic=screen.blit(transform.flip(undoPic,True,False),(850,93))        #redo
screen.blit(text,(24,69))
screen.blit(image.load("graphics/size_sub.png"),(940,30))
screen.blit(image.load("graphics/pick_sub.png"),(945,240))
screen.blit(image.load("graphics/current.png"),(955,387))
screen.blit(image.load("graphics/tips.png"),(150,600))
screen.blit(undoPic,(800,93))
screen.blit(transform.scale(image.load("graphics/trashcan.png"),(60,60)),(855,620))
screen.blit(transform.scale(image.load("graphics/save.png"),(40,40)),(0,640))
screen.blit(transform.scale(image.load("graphics/load.png"),(40,40)),(0,690))


canvasRect=Rect(395,140,522,367)     #canvas
paletteRect=Rect(20,50,60,20)        #palette
colorRect=Rect(957,170,100,84)       #color chart
S1Rect=Rect(435,620,60,60)       #Pencil stamp
S2Rect=Rect(505,620,60,60)       #Calculator stamps
T3Rect=Rect(575,620,60,60)       #stamp3
T4Rect=Rect(645,620,60,60)       #stamp4
T5Rect=Rect(715,620,60,60)       #stamp5
polygonRect=Rect(785,620,60,60) #polygon
clean=Rect(855,620,60,60)       #trash can
surface=Rect(0,0,1100,750)      #the screen

pencilRect=Rect(435,550,60,60)        #pencil
eraserRect=Rect(505,550,60,60)       #eraser
lineRect=Rect(575,550,60,60)          #line tool
brushRect=Rect(645,550,60,60)        #paint brush
outline_rect=Rect(715,550,60,60)    #Rectangle tool
spray=Rect(785,550,60,60)           #spray tool
oval=Rect(855,550,60,60)            #Oval tool
sav=Rect(0,640,40,40)               #save
loadRect=Rect(0,690,40,40)          #load
undoRect=Rect(800,93,40,40)         #undo
redoRect=Rect(850,93,40,40)         #redo
pauseRect=Rect(435,93,40,40)        #pause(bgm)


screen.blit(image.load("graphics/clock_back.png"),(586,12))
chem=transform.scale(image.load("graphics/chem.jpg"),(163,87)) #background pictures
basketball=transform.scale(image.load("graphics/basketball.jpg"),(172,84))
bus=transform.scale(image.load("graphics/bus.jpg"),(160,87))

draw.line(screen,BROWN,(50,175),(50,270),8) #The bookshelf(to look good)
draw.line(screen,BROWN,(218,175),(218,262),20)
draw.line(screen,BROWN,(385,175),(385,269),8)
draw.line(screen,BROWN,(50,265),(385,265),8)

screen.blit(chem,(55,175))
screen.blit(basketball,(150,270))
screen.blit(bus,(225,175))

chemRect=Rect(55,175,163,87)
basketRect=Rect(150,270,172,84)
busRect=Rect(225,175,160,87)

draw.rect(screen,BLACK,pauseRect,2)

#Backgrounds
picNames=["graphics/chem.jpg","graphics/basketball.jpg","graphics/bus.jpg"]  
picList=[] 
for i in picNames:
    pic=image.load(i)#loading 1 picture at a time
    picList.append(pic) #append the picture into the picList
    


#Variables
running=True
Fill=False                          #Fill is the variable for the options to fill or unfill shapes
col=BLACK                           #Starts with black(color)
tool=""                             #current tool
bgcol=WHITE                         #CANVAS Background
s_size=25                           #Thickness for the spray paint
size=1                              #Thicknesses other than spray
draw.rect(screen,WHITE,canvasRect)      
screenshot=screen.subsurface(canvasRect).copy() #screenshot of the canvas (to capture the screenshot so it wont disappear)
w=pen_stamp.get_width()             #get the width and height(stamps)
h=pen_stamp.get_height()
poly_list=[]                        #The list that will contain the coordinate of positions for polygon
polygon=True                        #Variable for polygon(boolean for stop infinite polygon)
BGM=False                           #BGM boolean(initially turned off)



##Size selector
Font1=font.SysFont("Arial",13)#Fonts that is used for stamps only
Font3=font.SysFont("Arial",20)  #Fonts
Font2=font.SysFont("Aharoni",30)    #Subtitles


screenshot=screen.subsurface(canvasRect).copy() #screenshot for the white canvas
undo=[screenshot]   #canvas is always the first element in the undo list
redo=[]

    
while running:
    click=False
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            sx,sy=evt.pos    #The position of x and y when clicked
            if evt.button==1:       #When left click is the mouse event
                click=True
            if evt.button==3:
                if tool=="polygon":
                    polygon=False  #the polygon will be finished when right clicked 
                    if len(poly_list)>2 and polygon==False: #the poly_list need to have at least 3 elements to draw polygon
                        if Fill==False: #unfill
                            draw.polygon(screen,col,poly_list,size)
                        else:    #fill
                            draw.polygon(screen,col,poly_list)
                    poly_list.clear()  #clear all old coordinate where the old polygon is completed
                    polygon=True       #reset the boolean
                    screenCap=screen.subsurface(canvasRect).copy() 
                    undo.append(screenCap) #add to undo list
                  
        if evt.type==MOUSEBUTTONUP:     #when the button is released
            screen.set_clip(canvasRect)
            if  tool=="undo" and undoRect.collidepoint(mx,my):  #when hovering the icon and current tool is undo     
                if len(undo)>1:             #Must include the screenshot of canvas so length must>1
                    redo.append(undo[-1])   #append the last element to the redo list
                    undo.pop()              #delete the last element in the undo list
                    screen.blit(undo[-1],(395,140)) #blit the second last element in the orignal undo list
                                                    #(currently the last element in the undo list)
                if len(poly_list)>0 and mb[0]:
                    backup=poly_list.copy()         #backup polygon list for redo
                    poly_list.pop()

                                
            if tool=="redo" and redoRect.collidepoint(mx,my):
                try:                                 #handler to avoid an error that will crash my program(sometimes)
                    if len(redo)>0 and len(undo)>=1:
                        screen.blit(redo[-1],(395,140)) #blit the last element from redo
                        undo.append(redo[-1])   #append the last element from redo list to the undo list
                        redo.pop()              #remove the last element from redo list
                    if mb[0] and len(poly_list)>1:
                        ind=poly_list.index(poly_list[-1])  #get the index of the last element in the polygon list
                        t=backup.count(backup[ind+1])   #count how many last element we need to recover from the backup list
                        for i in range(t):    
                            poly_list.append(backup[ind+1]) 
                            ind+=1
                except IndexError:
                    print("")

         
            if tool=="line tool":
                screenshot=screen.subsurface(canvasRect).copy() #screenshot the screen then blit it so it won't disappear
                draw.line(screen,col,(sx,sy),(mx,my),size) #sx,sy is the position when clicked
                screen.blit(screenshot,canvasRect)

                
            if tool=="pencil stamp":
                mouse.set_visible(True)  #The cursor is visible when released mouse and tool is a stamp
                
            if tool=="percent stamp":
                mouse.set_visible(True)

            if tool=="book stamp":
                mouse.set_visible(True)

            if tool=="calculator stamp":
                mouse.set_visible(True)
                
            if tool=="backpack stamp":
                mouse.set_visible(True)

            if tool=="brush tool":
                draw.circle(screen,col,(mx,my),size)    #draw circles with current size
                
                                                
            if tool=="spray paint":         
                screenshot=screen.subsurface(canvasRect).copy()     #save a screenshot of spray when released mouse

                
            if tool=="circle":  
                if Fill==False: #Unfill
                    screenshot=screen.subsurface(canvasRect).copy()
                    draw.ellipse(screen,col,[sx,sy,(mx-sx),(my-sy)],size)
                    screen.blit(screenshot,canvasRect)

                else:   #Fill
                    draw.ellipse(screen,col,[sx,sy,(mx-sx),(my-sy)])

                    
            if tool=="polygon":
                screenshot=screen.subsurface(canvasRect).copy()
                

            if tool=="clear screen":
                screenshot=screen.subsurface(canvasRect).copy()     
                draw.rect(screen,bgcol,canvasRect)
                poly_list.clear()   #clear the polygon list when clear the screen
            #three backgrounds
            if chemRect.collidepoint(mx,my)and mb[0]==True:
                back1=image.load("graphics/chem_lab.jpg")
                screen.blit(back1,(395,140))
                screenshot=screen.subsurface(canvasRect).copy()
                undo.append(screenshot) #append the background to undolist so we are able to undo it, if needed
                
            if basketRect.collidepoint(mx,my) and mb[0]:
                back2=image.load("graphics/basket.jpg")
                screen.blit(back2,(395,140))
                screenshot=screen.subsurface(canvasRect).copy()
                undo.append(screenshot)

            if busRect.collidepoint(mx,my) and mb[0]:
                back2=image.load("graphics/bus_back.jpg")
                screen.blit(back2,(395,140))
                screenshot=screen.subsurface(canvasRect).copy()
                undo.append(screenshot)
                

            if canvasRect.collidepoint(mx,my)and mb[0]:     #screen capture only when cursor is on canvas and clicked
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)                  #add the screen capture to the undo list
            
            screen.set_clip(None)                                
                                                                    #Makesure to save a screenshot when released the mouse
                                                                    #"None" means back to normal
            screenshot = screen.subsurface(canvasRect).copy()       #screenshot the canvas so it won't be gone(disappear)
            screen.blit(screenshot, canvasRect)                     #blit the screenshot that you just took

        keys=key.get_pressed()      #define the keys variable                                                                            
        if evt.type==KEYDOWN:       #Keyboard events
            if evt.key==K_DOWN and size>1:                                  #size is the variable for general tools
                size-=1                                                        #Down key size -1 each time
            if evt.key==K_UP and size<=34:                                     #Max thickness is 35   
                size+=1                                                        #Up key size+1 each time
            if evt.key==K_UP and s_size<=34 and tool=="spray paint":        #s_size is the variable for spray thickness
                s_size+=2
            if evt.key==K_DOWN and s_size>25 and tool=="spray paint":
                s_size-=2
            if keys[K_f]:
                Fill=True       #When user click the f key the Fill variable then becomes true(Use to fill shapes)
            if keys[K_u]:
                Fill=False      #When user clicked the u key the Fill variable will be False(Use to unfill shapes)
            for i in range(len(keys_list)):  #short cuts for tools/stamps(for fun)
                if evt.key==keys_list[i]:
                    ind=keys_list.index(keys_list[i])
                    tool=my_tools[i]
            for i in range(len(keys_stamps)):
                if evt.key==keys_stamps[i]:
                    ind=keys_stamps.index(keys_stamps[i])
                    tool=stamps[ind]
                    

         
    mx,my=mouse.get_pos()#getting the current mx and my
    mb=mouse.get_pressed()

    #All the outlines for tools
    x=365
    y=550
    for i in range (7):                             #draw all the outline boxes for the icons using loops
        x+=70
        draw.rect(screen,CYAN,[x,y,60,60],2)
    y=620
    x=365
    for _ in range(7):
        x+=70
        draw.rect(screen,CYAN,[x,y,60,60],2)

    #Size indicator
    draw.rect(screen,WHITE,[980,134,50,30])
    draw.rect(screen,BLACK,[980,134,50,30],3)           #The box for number indicator
    draw.rect(screen,WHITE,[980,78,50,50])
    draw.rect(screen,BLACK,[980,78,50,50],3)             #The box for circle thickness indicator
    draw.rect(screen,WHITE,[967,435,93,45])                 
    draw.rect(screen,BLACK,[967,435,93,45],3)           #The box for the current tool
    draw.rect(screen,BLACK,sav,3)
    draw.rect(screen,BLACK,loadRect,3)             #The load button

            


    #BGM BUTTONS
    if pauseRect.collidepoint(mx,my)and click:
        count+=1            #When mouse is clicked(counter)
        if count%2!=0:      #Only odd number times of click will play the bgm, since it's started from stop
            BGM=True
            screen.blit(unpause,(435,93))
            if BGM==True:
                mixer.music.load(my_BGM[pos])
                mixer.music.play(-1)  #play musics(infinitely)

        else:
            BGM=False
            screen.blit(pause,(435,93))
            if BGM==False:
                mixer.music.fadeout(100)
        draw.rect(screen,BLACK,pauseRect,2)


    if leftRect.collidepoint(mx,my)and click:   #If clicked back to the previous song button
        if BGM==True:
            if 0<=pos<=2:       #Make sure the position is not out of my BGM list's range
                if pos==0:      #If it's first song, it will be back to the last song in the list 
                    pos=2
                else:           #If it's not the first song, just return to the previous song
                    pos-=1
            if pos==2:
                mixer.music.load(my_BGM[2])     
                mixer.music.play(-1)    #The parameter -1 will play the song infinitely
            elif pos==1:
                mixer.music.load(my_BGM[1])
                mixer.music.play(-1)
            else:
                mixer.music.load(my_BGM[0])
                mixer.music.play(-1)

            
    if rightRect.collidepoint(mx,my)and click: #same method as the previous bgm button
        if BGM==True:
            if 0<=pos<=2:
               if pos==2:
                   pos=0
               else:
                   pos+=1
            if pos==0:
                mixer.music.load(my_BGM[0])
                mixer.music.play(-1)
            elif pos==1:
                mixer.music.load(my_BGM[1])
                mixer.music.play(-1)
            else:
                mixer.music.load(my_BGM[2])
                mixer.music.play(-1)
            

        
    #Indicator for stamps
    if "stamp" in tool:     #All stamps
        cur_tool=Font1.render(tool,True,BLACK)
        screen.blit(cur_tool,(980,445))
    
    #Indicator for rectangle or circle tool    
    if tool=="rectangle" or tool=="circle" or tool=="polygon": #Only rectangle,polygon and oval/circle can be filled or unfilled
        if size==1 or s_size==1:
            draw.circle(screen,col,(1005,103),1)
        if Fill==False:
            cur_tool=Font3.render(f"{tool}",True,BLACK) #formatted string
            unfill=Font3.render("(Unfilled)",True,RED)
            screen.blit(cur_tool,(986,435))
            screen.blit(unfill,(983,453))
        else:
            cur_tool=Font3.render(f"{tool}",True,BLACK)
            fill=Font3.render("(Filled)",True,GREEN)
            screen.blit(cur_tool,(986,435))
            screen.blit(fill,(983,453))

            
    #The text indicator (except undo/redo,trashcan)    
    if tool =="pencil" or tool=="eraser" or tool=="line tool" or tool=="brush tool" or tool=="spray paint":
        if tool=="spray paint":
            cur_tool=Font3.render(tool,True,BLACK)      #since word "pencil","eraser","brush tool","spray paint" and "line tool" are relatively shorter
            screen.blit(cur_tool,(975,445))             #I need to adjust the dimension to make it more close to the center
        elif tool=="pencil" or tool=="eraser":
            cur_tool=Font3.render(tool,True,BLACK)
            screen.blit(cur_tool,(990,445))
        else:
            cur_tool=Font3.render(tool,True,BLACK)
            screen.blit(cur_tool,(983,445))
            
    #The dot indicator     
    if tool!="spray paint"and tool!="pencil" and tool!="undo" and tool!="redo" and tool!="clear screen" and "stamp" not in tool:    #Set up restrictions(all tools except stamps,pencil and spray) as stamps don't have sizes
            c_size=Font3.render(str(size),True,BLACK)                   #pencil tool cannot change size and size for spray is in another variable
            screen.blit(c_size,(999,135))       #for the number(numerical) indicator
            draw.circle(screen,col,(1005,103),size//1.55)#Ensure the circle indicator stays inside the box
            if tool=="eraser":                  
                if size==1:
                    draw.circle(screen,GREY,(1005,103),1)
                else:
                    draw.circle(screen,GREY,(1005,103),size//1.55)                                        
                
            elif tool!="eraser" and size==1 or s_size==1:
                draw.circle(screen,col,(1005,103),1)    #Initial is thickness is one 
                
                
    if tool=="pencil":                               #pencil's thickness can only be one                                         
        draw.circle(screen,col,(1005,103),1)
        c_size=Font3.render(str(1),True,BLACK)                                
        screen.blit(c_size,(1000,135))      
        
    if tool=="spray paint":
        c_size=Font3.render(str(s_size),True,BLACK)#I used a seperate variable for spray thickness
        screen.blit(c_size,(995,135))       #for the number indicator
        draw.circle(screen,col,(1005,103),s_size//1.55)
            

    #selecting the tools
    if click: #When selected any tools
        if pencilRect.collidepoint(mx,my):
           tool="pencil"
        if eraserRect.collidepoint(mx,my):
           tool="eraser"
        if lineRect.collidepoint(mx,my):       
           tool="line tool"
        if brushRect.collidepoint(mx,my):
           tool="brush tool"
        if S1Rect.collidepoint(mx,my):
           tool="pencil stamp"
        if outline_rect.collidepoint(mx,my):
            tool="rectangle"    
        if S2Rect.collidepoint(mx,my):
            tool="calculator stamp"
        if T3Rect.collidepoint(mx,my):
            tool="percent stamp"
        if T4Rect.collidepoint(mx,my):
            tool="book stamp"
        if T5Rect.collidepoint(mx,my):
            tool="backpack stamp"
        if spray.collidepoint(mx,my):
            tool="spray paint"
        if oval.collidepoint(mx,my):
            tool="circle"
        if sav.collidepoint(mx,my):
            try:        
                fname=filedialog.asksaveasfilename(defaultextension=".png") #Default saving extension is .png file
                image.save(screen.subsurface(canvasRect),fname)
            except Exception:           #To avoid the python error when user clicked exit without type anything for file name
                print("Empty input")      #Set a general exception so" pygame.error: SDL_RWFromFile(): No file or no mode specified
                                                #won't display and my program won't crash
            
        if loadRect.collidepoint(mx,my):
            fname=filedialog.askopenfilename()
            supported_extension=[".png",".jpg",".jpeg"]  #Find the extension type from the postion of . to the end of the file name
            ext=fname[fname.rfind("."):len(fname)]   #Find the type of extension on the file that user want to load(from right)
            if ext in supported_extension:          #Check whether the extension is supported then load
                pic=image.load(fname)           #load the image
                if pic.get_width()>522:     #Check whether the length(width) of the image can fit into my canvas or not
                    pic=transform.scale(pic,(522,pic.get_height())) #if not, resize the length(width)
                if pic.get_height()>367:        #Check for the width(height) of the image
                    pic=transform.scale(pic,(pic.get_width(),367))  #if not, resize the width(height)
                screen.blit(pic,canvasRect)
                

        if undoRect.collidepoint(mx,my):
            tool="undo"
        if redoRect.collidepoint(mx,my):
            tool="redo"
        if polygonRect.collidepoint(mx,my):
            tool="polygon"
        if clean.collidepoint(mx,my):
            tool="clear screen"


    #Hovering
    for i in range(len(tool_icons)):
        if pencilRect.collidepoint(mx,my)and tool!="pencil":     #when only hovering on specific tool, outline with red
            draw.rect(screen,RED,pencilRect,2)
        if eraserRect.collidepoint(mx,my)and tool!="eraser":
            draw.rect(screen,RED,eraserRect,2)
        if lineRect.collidepoint(mx,my)and tool!="line tool":
            draw.rect(screen,RED,lineRect,2)
        if brushRect.collidepoint(mx,my)and tool!="brush tool":
            draw.rect(screen,RED,brushRect,2)
        if spray.collidepoint(mx,my)and tool!="spray paint":
            draw.rect(screen,RED,spray,2)
        if oval.collidepoint(mx,my) and tool!="circle":
            draw.rect(screen,RED,oval,2)
        if outline_rect.collidepoint(mx,my)and tool!="rectangle":
            draw.rect(screen,RED,outline_rect,2)
            
            
    for i in range(len(my_stamps)):
        if S2Rect.collidepoint(mx,my)and tool!="calculator stamp":
            draw.rect(screen,RED,S2Rect,2)
        if T3Rect.collidepoint(mx,my)and tool!="percent stamp":
            draw.rect(screen,RED,T3Rect,2)
        if T4Rect.collidepoint(mx,my) and tool!="book stamp":
            draw.rect(screen,RED,T4Rect,2)
        if T5Rect.collidepoint(mx,my) and tool!="backpack stamp":
            draw.rect(screen,RED,T5Rect,2)
        if S1Rect.collidepoint(mx,my)and tool!="pencil stamp":
            draw.rect(screen,RED,S1Rect,2)
        if polygonRect.collidepoint(mx,my)and tool!="polygon":
            draw.rect(screen,RED,polygonRect,2)
        if clean.collidepoint(mx,my)and tool!="clear screen":
            draw.rect(screen,RED,clean,2)



##Hovering undo/redo
    draw.rect(screen,BLACK,undoRect,2)
    draw.rect(screen,BLACK,redoRect,2)
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,RED,undoRect,2)
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,RED,redoRect,2)
    

#Hightlight the current selected tool
    if undoRect.collidepoint(mx,my) and mb[0]:   #when mouse is on the undo/redo icon and clicked
        draw.rect(screen,GREEN,undoRect,2)
    if redoRect.collidepoint(mx,my) and mb[0]:
        draw.rect(screen,GREEN,redoRect,2)
        
    for i in range(len(tool_icons)):    #iterate through all the icons in the tool_icons list
        if tool=="pencil":
            draw.rect(screen,GREEN,pencilRect,2)    #tool variable is the current selected tool, outline with green
        if tool=="eraser":
            draw.rect(screen,GREEN,eraserRect,2)
        if tool=="line tool":
            draw.rect(screen,GREEN,lineRect,2)
        if tool=="brush tool":
            draw.rect(screen,GREEN,brushRect,2)
        if tool=="spray paint":
            draw.rect(screen,GREEN,spray,2)
        if tool=="circle":
            draw.rect(screen,GREEN,oval,2)
        if tool=="rectangle":
            draw.rect(screen,GREEN,outline_rect,2)

    for i in range(len(my_stamps)):     #iterate through all the stamps in the my_stamps list
        if tool=="calculator stamp":
            draw.rect(screen,GREEN,S2Rect,2)
        if tool=="percent stamp":
            draw.rect(screen,GREEN,T3Rect,2)
        if tool=="book stamp":
            draw.rect(screen,GREEN,T4Rect,2)
        if tool=="backpack stamp":
            draw.rect(screen,GREEN,T5Rect,2)
        if tool=="pencil stamp":
            draw.rect(screen,GREEN,S1Rect,2)
        if tool=="polygon":
            draw.rect(screen,GREEN,polygonRect,2)
        if clean.collidepoint(mx,my) and mb[0]: #When mouse on the clear screen icon and only when clicked
            draw.rect(screen,GREEN,clean,2)

           
    #Selecting color   
    draw.rect(screen,BLACK,(970,305,73,60),2)       #The color preview box
    compRect=Rect(970,382,80,20)
    draw.rect(screen,SKY,compRect)
    
    GREY_sel=draw.rect(screen,GREY,(1070,320,25,25))
    if GREY_sel.collidepoint(mx,my) and mb[0]:      #Grey is not on my color chart 
        draw.rect(screen,GREY,(970,305,73,60))
        col=GREY
        
    if colorRect.collidepoint(mx,my) and mb[0]:     #When the color chart and user's cursor collide then get the color:
        col=screen.get_at((mx,my))                  #Special command to get the color
        draw.rect(screen,col,(970,305,73,60))

    if surface.collidepoint(mx,my):
        component=Font1.render(f"{col[0],col[1],col[2]}",True,NAVY) #Display the R,G,B components of selected color
        screen.blit(component,(975,380))
        

    #use the tool
    if canvasRect.collidepoint(mx,my) and mb[0]:        #When mouse on the canvas and get pressed
        screen.set_clip(canvasRect)         #Setup correctly so the drawing don't come outside the canvas     
        if tool=="pencil":
            draw.line(screen,col,(oldmx,oldmy),(mx,my))     #connect line between the location from the previous frame to the location in the current frame
            screenshot=screen.subsurface(canvasRect).copy() #screenshot of the canvas

            
        if tool=="eraser":
            distance=sqrt((oldmx-mx)**2+(oldmy-my)**2)      #Calculate the slope(pythagorean) to ensure there is no gap in between each circle
            dx=mx-oldmx                                   
            dy=my-oldmy 
            for i in range(int(distance)):              #connect the two points with circles
                dotX=oldmx+dx*i/distance                #Calculate the position of the circles
                dotY=oldmy+dy*i/distance
                draw.circle(screen,WHITE,(int(dotX),int(dotY)),size) 
            screenshot=screen.subsurface(canvasRect).copy()

                
        if tool=="line tool":
            screen.blit(screenshot, canvasRect)
            draw.line(screen,col,(sx,sy),(mx,my),size)  #sx and sy are the initial position when user clicked and draw line that connected to the current positions
            
        if tool=="brush tool":
            distance=sqrt((oldmx-mx)**2+(oldmy-my)**2)    #The distance from the previous location of the mouse to the current location
            dx=mx-oldmx                                   #calculate using pythagorean theory(hypot)
            dy=my-oldmy 
            for i in range(int(distance)):              #To connect gap
                dotX=oldmx+dx*i/distance                
                dotY=oldmy+dy*i/distance                #calculate the position(dotX is the x-value, dotY is the y-vlaue) of each circle
                draw.circle(screen,col,(int(dotX),int(dotY)),size)

                
        if tool=="rectangle":
            if Fill==False:         #When NOT filled
                screen.blit(screenshot,canvasRect)
                my_rect=Rect(sx,sy,(mx-sx),(my-sy))         #The first coordinate is the position of the cursor when the user clicked the mouse(sx,sy)
                my_rect.normalize()                     #Calculte the difference between current position and the initial position
                draw.rect(screen,col,my_rect,size)      # for rectangle's length and width
            else:                   #When filled
                screen.blit(screenshot,canvasRect)
                my_rect=Rect(sx,sy,(mx-sx),(my-sy))         
                my_rect.normalize()
                draw.rect(screen,col,my_rect)
                
        if tool=="spray paint":
            for i in range(s_size*4):    #Want to draw spray size*4 amount of small circles each time 
                rx=randint(-s_size,s_size)  
                ry=randint(-s_size,s_size)
                distance=sqrt((mx-(mx+rx))**2+(my-(my+ry))**2)  #Use the equation of circle and use square root(pythagorean) afterwards to reduce the gap in between each circles
                if distance<=s_size:                            #only draw when it's smaller than or equal to the size of spray
                    draw.circle(screen,col,(mx+rx,my+ry),1)     #each circle has radius of 1
                    
        if tool=="circle":
            if Fill==False:
                screen.blit(screenshot,canvasRect)
                my_oval=Rect(sx,sy,(mx-sx),(my-sy))         #The first coordinate is the position of the cursor when the user clicked the mouse(sx,sy)
                my_oval.normalize()                     #Calculte the difference between current position and the initial position
                draw.ellipse(screen,col,my_oval,size)   #draw ellipse instead of rectangle
            else:
                screen.blit(screenshot,canvasRect)
                my_oval=Rect(sx,sy,(mx-sx),(my-sy))         
                my_oval.normalize()                     
                draw.ellipse(screen,col,my_oval)

      
        if tool=="polygon":
            if polygon==True:
               screenshot=screen.subsurface(canvasRect).copy()
               screen.blit(screenshot,canvasRect)
               if click:
                   poly_list.append((mx,my))           #Append the coordinates of mouse's current position(mx,my)
                   draw.circle(screen,col,(mx,my),1)
                   
                        
        for i in range(len(stamps)):    #iterate through the stamps list
             if stamps[i]==tool:         #if current tool is any stamp
                mouse.set_visible(False)    #hide the cursor
                screen.blit(screenshot,canvasRect)  #screenshot
                screen.blit(png_files[i],(mx-w//2,my-h//2)) #center the cursor and put on the png file that corresponds
                                                                #to the stamp in the list
        
        if tool=="clear screen":
            screenshot=screen.subsurface(canvasRect).copy()     
            draw.rect(screen,bgcol,canvasRect) #draw a rectangle that cover the canvas

        screen.set_clip(None)


    oldmx,oldmy=mx,my #oldmx oldmy is the location of the mouse in the PREVIOUS FRAME
    display.flip()
    myClock.tick(150)    #-FPS
            
quit()
