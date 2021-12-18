import numpy as np
import tkinter as tk
import sys
import os
import GameBasics

#IMPORTANT, RUN IDE IN ADMINISTRATOR TO OPEN FILES

TL = tk.Toplevel()
TL.title("A Game")
TL.minsize(300,300)
ScreenPxH = TL.winfo_screenheight()
ScreenPxW = TL.winfo_screenwidth()

msg = tk.Message(TL, text=".....")
msg.grid(column = 0)

canvW = ScreenPxW*0.9
canvH = ScreenPxH*0.9
canv = tk.Canvas(TL, width = canvW, height = canvH, background = "white")
canv.grid(column = 1)

Photolist = []
MapInfo = GameBasics.MapGen(100,100)
CameraX = 0
CameraY = 0
TileSize = 100
DrawPosX = TileSize/2
DrawPosY = TileSize/2
DrawPosXOrg = DrawPosX
DrawPosYOrg = DrawPosY
MXD = 0
MYD = 0
MXU = 0
MYU = 0
gameEntities = []
Selected = False

def GetPhotos():
    global Photolist
    Photolist = GameBasics.PhotoLoader()
    for Photo in Photolist:
        Photolist[Photolist.index(Photo)] = tk.PhotoImage(file=Photolist[Photolist.index(Photo)])
    canv.create_image(DrawPosX, DrawPosY, image=Photolist[2])
    return Photolist
#PhotoList = GameBasics.PhotoLoader()

#NON FUNCTIONAL-----
"""TkinterPhotoList = []
__dir__=os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(__dir__, r"C:/Users/brick/Downloads/PyProjectCreateTask/RTS Sprites/Ground Tiles")
print(filename)
for Photo in Photolist:
    TkinterPhotoList.append(tk.PhotoImage(file=filename))"""
#NON FUNCTIONAL-----
def DebugCom():
    print("Hello!")
    


def ClickCheck():
    global CameraX
    global CameraY
    global DrawPosX
    global DrawPosY
    global gameEntities
    global Selected
    Hitboxes = []
    print("Mouse X Down:"+str(MXD)+" Mouse X Up:"+str(MXU)+" Mouse Y Down:"+str(MYD)+" Mouse Y Up:"+str(MYU))
    for objects in gameEntities:
        Hitboxes.append(GameBasics.HitboxMaker(canv, objects))
    if abs(abs(MXD)-abs(MXU)) <= 20 or abs(abs(MYD)-abs(MYU)) <= 20:
        print("Click")
        for box in Hitboxes:
            if MXD > box[1] and MXD < box[3] and MYD > box[0] and MYD < box[2]:
                Entity = gameEntities[Hitboxes.index(box)]
                gameEntities.pop(Entity)
                gameEntities.append(Entity)
                Selected = Entity
            else:
                Selected = False
    else:
        print("Drag")
        CameraY += ((MYD-MYU))
        CameraX += ((MXD-MXU))
        print(DrawPosY)
        print(DrawPosX)
    
def DrawMap():
    global DrawPosX
    global DrawPosY
    global MapInfo
    
    Photolist = GetPhotos()
    for row in MapInfo:
        if DrawPosY < canvH:
            for column in row:
                if DrawPosX< canvW:
                    if column[1] == 1:
                        canv.create_image(DrawPosX, DrawPosY, image=Photolist[2])
                        #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "green")
                    elif column[1] == 2:
                        canv.create_image(DrawPosX, DrawPosY, image=Photolist[3])
                        #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "brown")
                    elif column[1] == 3:
                        canv.create_image(DrawPosX, DrawPosY, image=Photolist[4])
                        #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "blue")
                    else:
                        canv.create_image(DrawPosX, DrawPosY, image=Photolist[0])
                        #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "purple")
                DrawPosX+=TileSize
            #print(DrawPosX)
        DrawPosX = TileSize/2
        DrawPosY+=TileSize
        #print(DrawPosY)
    DrawPosX = DrawPosXOrg
    DrawPosY = DrawPosYOrg


def MouseDown(event):
    global MXD,MYD
    MXD = event.x
    MYD = event.y
    print("Mouse 1 Down")
    
def MouseUp(event):
    global MXU, MYU
    MXU = event.x
    MYU = event.y
    ClickCheck()
    print("Mouse 1 Up")

Dismiss = tk.Button(TL, text="Dismiss", command=TL.quit)
Dismiss.grid(column = 1,row = 2)

Reload = tk.Button(TL, text= "Reload Map", command=DrawMap)
Reload.grid(column = 0, row = 2)

canv.bind('<Motion>')
canv.bind('<ButtonPress-1>', MouseDown)
canv.bind('<ButtonRelease-1>', MouseUp)



TL.mainloop()

TL.destroy()
sys.exit()