import numpy as np
import tkinter as tk
import sys
import os
import GameBasics
import EntityClasses as EntCl
import time

#IMPORTANT, RUN IDE IN ADMINISTRATOR TO OPEN FILES

TL = tk.Toplevel()
TL.title("A Game")
TL.minsize(300,300)
ScreenPxH = TL.winfo_screenheight()
ScreenPxW = TL.winfo_screenwidth()

msg = tk.Message(TL, text=".....")
msg.grid(column = 0)

canvW = ScreenPxW*0.8
canvH = ScreenPxH*0.8
canv = tk.Canvas(TL, width = canvW, height = canvH, background = "white")
canv.grid(column = 1)

Photolist = []
MapW = 10
MapH = 10
MapInfo = GameBasics.MapGen(MapH,MapW)
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
MapGoPop = []


BuildingMap = []
for TileRow in MapInfo:
    BuildingRowHolder = []
    for Tile in TileRow:
        BuildingRowHolder.append([False, ""])
    BuildingMap.append(BuildingRowHolder)
#print(BuildingMap)
BuildingMap = GameBasics.Spawning(BuildingMap)
#print(BuildingMap)
    
Selectables = []
gameEntities = []
Selected = False

Keyname = tk.StringVar()
ActiveKeys = []

def GetPhotos(Subfolder):
    Photolist = GameBasics.PhotoLoader(Subfolder)
    for Photo in Photolist:
        Photolist[Photolist.index(Photo)] = tk.PhotoImage(file=Photolist[Photolist.index(Photo)])
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
    
def Init():
    Play.config(state = "disabled")
    DrawMap()

Buildinglist = GetPhotos("\Buildings")
Photolist = GetPhotos("\Ground Tiles")
Trooplist = GetPhotos("\Troops")

        # Y, X
Selector = [0,0, canv.create_image(DrawPosX ,DrawPosY, image = Buildinglist[2])]
#print(Buildinglist)
#print(Photolist)
#print(Trooplist)

def ClickCheck():
    global MapInfo
    global CameraX
    global CameraY
    global DrawPosX
    global DrawPosY
    global Selectables
    global Selected
    global ActiveKeys
    Hitboxes = []
    #print("Mouse X Down:"+str(MXD)+" Mouse X Up:"+str(MXU)+" Mouse Y Down:"+str(MYD)+" Mouse Y Up:"+str(MYU))
    """
    for objects in Selectables:
        print("Selectables: ")
        print(Selectables)
        Hitboxes.append([objects,GameBasics.HitboxMaker(canv, objects)])
        """
    
    if abs(abs(MXD)-abs(MXU)) <= 20 and abs(abs(MYD)-abs(MYU)) <= 20:
        print("Click")
        #print(Hitboxes)
        for box in Hitboxes:
            if MXD > box[1][1] and MXD < box[1][3] and MYD > box[1][0] and MYD < box[1][2]:
                print("yes")
                Entity = Selectables[Hitboxes.index(box)]
                gameEntities.pop(Entity)
                gameEntities.append(Entity)
                Selected = Entity
            else:
                print("No")
                Selected = False
    else:
        print("Drag")
        DrawPosY -= ((MYD-MYU))
        DrawPosX -= ((MXD-MXU))
        """
        for row in MapInfo:
            for column in row:
                if len(column) > 2:
                    print("Here")
                    print(MapInfo)
                    canv.delete(column[2])
                    column[2] = None
                else:
                    pass
                    """
        DrawMap()
        
    
def DrawMap():
    print("DrawMap")
    global DrawPosX
    global DrawPosY
    global MapInfo
    global DrawPosXOrg
    global Trooplist
    global Photolist
    global Buildinglist
    global MapGoPop
    global canv
    rowCount = 0
    colCount = 0
    DrawPosXOrg = DrawPosX
    DrawPosYOrg = DrawPosY
    gameEntities = []
    #print(BuildingMap)
    for row in MapInfo:
        for column in row:
            colCount += 1
            if column[0] ==1:
                if column[1] == 1:
                    if len(column) <= 2:
                        Temp = canv.create_image(DrawPosX, DrawPosY, image=Photolist[2])
                        column.append(Temp)
                        #print(column)
                    else:
                        #print(column[2])
                        #type(column[2])
                        #print(canv.coords(column[2]))
                        TempX = canv.coords(column[2])[0]
                        TempY = canv.coords(column[2])[1]
                        canv.move(column[2],DrawPosX-TempX,DrawPosY-TempY)
                    #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "green")
                elif column[1] == 2:
                    if len(column) <= 2:
                        Temp = canv.create_image(DrawPosX, DrawPosY, image=Photolist[3])
                        column.append(Temp)
                    else:
                        TempX = canv.coords(column[2])[0]
                        TempY = canv.coords(column[2])[1]
                        canv.move(column[2],DrawPosX-TempX,DrawPosY-TempY)
                    #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "brown")
                elif column[1] == 3:
                    if len(column) <= 2:
                        Temp = canv.create_image(DrawPosX, DrawPosY, image=Photolist[4])
                        column.append(Temp)
                    else:
                        TempX = canv.coords(column[2])[0]
                        TempY = canv.coords(column[2])[1]
                        canv.move(column[2],DrawPosX-TempX,DrawPosY-TempY)
                    #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "blue")
                else:
                    if len(column) <= 2:
                        Temp = canv.create_image(DrawPosX, DrawPosY, image=Photolist[0])
                        column.append(Temp)
                    else:
                        TempX = canv.coords(column[2])[0]
                        TempY = canv.coords(column[2])[1]
                        canv.move(column[2],DrawPosX-TempX,DrawPosY-TempY)
                    #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "purple")
            if column[0] == 2 :
                if column[1] == 1:
                    if len(column) <= 2:
                        Temp = canv.create_image(DrawPosX, DrawPosY, image=Photolist[7])
                        column.append(Temp)
                    else:
                        TempX = canv.coords(column[2])[0]
                        TempY = canv.coords(column[2])[1]
                        canv.move(column[2],DrawPosX-TempX,DrawPosY-TempY)
                    #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "green")
                elif column[1] == 2:
                    if len(column) <= 2:
                        Temp = canv.create_image(DrawPosX, DrawPosY, image=Photolist[8])
                        column.append(Temp)
                    else:
                        TempX = canv.coords(column[2])[0]
                        TempY = canv.coords(column[2])[1]
                        canv.move(column[2],DrawPosX-TempX,DrawPosY-TempY)
                    #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "brown")
                elif column[1] == 3:
                    if len(column) <= 2:
                        Temp = canv.create_image(DrawPosX, DrawPosY, image=Photolist[7])
                        column.append(Temp)
                    else:
                        TempX = canv.coords(column[2])[0]
                        TempY = canv.coords(column[2])[1]
                        canv.move(column[2],DrawPosX-TempX,DrawPosY-TempY)
                    #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "blue")
                else:
                    if len(column) <= 2:
                        Temp = canv.create_image(DrawPosX, DrawPosY, image=Photolist[0])
                        column.append(Temp)
                    else:
                        TempX = canv.coords(column[2])[0]
                        TempY = canv.coords(column[2])[1]
                        canv.move(column[2],DrawPosX-TempX,DrawPosY-TempY)
                    #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "purple")
            if column[0] == 3 :
                if column[1] == 1:
                    if len(column) <= 2:
                        Temp = canv.create_image(DrawPosX, DrawPosY, image=Photolist[1])
                        column.append(Temp)
                    else:
                        TempX = canv.coords(column[2])[0]
                        TempY = canv.coords(column[2])[1]
                        canv.move(column[2],DrawPosX-TempX,DrawPosY-TempY)
                    #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "green")
                elif column[1] == 2:
                    if len(column) <= 2:
                        Temp = canv.create_image(DrawPosX, DrawPosY, image=Photolist[6])
                        column.append(Temp)
                    else:
                        TempX = canv.coords(column[2])[0]
                        TempY = canv.coords(column[2])[1]
                        canv.move(column[2],DrawPosX-TempX,DrawPosY-TempY)
                    #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "brown")
                elif column[1] == 3:
                    if len(column) <= 2:
                        Temp = canv.create_image(DrawPosX, DrawPosY, image=Photolist[1])
                        column.append(Temp)
                    else:
                        TempX = canv.coords(column[2])[0]
                        TempY = canv.coords(column[2])[1]
                        canv.move(column[2],DrawPosX-TempX,DrawPosY-TempY)
                    #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "blue")
                else:
                    if len(column) <= 2:
                        Temp = canv.create_image(DrawPosX, DrawPosY, image=Photolist[0])
                        column.append(Temp)
                    else:
                        TempX = canv.coords(column[2])[0]
                        TempY = canv.coords(column[2])[1]
                        canv.move(column[2],DrawPosX-TempX,DrawPosY-TempY)
            if MapInfo.index(row) == Selector[1] and row.index(column) == Selector[0]:
                TempX = canv.coords(Selector[2])[0]
                TempY = canv.coords(Selector[2])[1]
                canv.move(Selector[2], DrawPosX - TempX, DrawPosY- TempY)
                canv.tag_raise(Selector[2])
                    #canv.create_rectangle((DrawPosX,DrawPosY,DrawPosX+TileSize,DrawPosY+TileSize ),fill = "purple")
            #print(BuildingMap)
            #print("\n")
            CurrentBuilding = BuildingMap[MapInfo.index(row)][row.index(column)][0]
            if  CurrentBuilding != False:
                #print(BuildingMap[MapInfo.index(row)][row.index(column)][0])
                #print(MapInfo)
                #print(BuildingMap[MapInfo.index(row)][row.index(column)])
                if BuildingMap[MapInfo.index(row)][row.index(column)][1] == "":
                    if isinstance(CurrentBuilding ,EntCl.Castle):
                        print("Here Castle " + CurrentBuilding.Alliance )
                        print(str(MapInfo.index(row))+ "," + str(row.index(column)))
                        #print(BuildingMap[MapInfo.index(row)][row.index(column)])
                        if CurrentBuilding.Alliance == "Blue":
                            BuildingMap[MapInfo.index(row)][row.index(column)][1]=(canv.create_image(DrawPosX, DrawPosY, image = Buildinglist[0]))
                            #gameEntities.append(BuildingMap[MapInfo.index(row)][row.index(column)][1])
                        elif CurrentBuilding.Alliance == "Red":
                            BuildingMap[MapInfo.index(row)][row.index(column)][1]=(canv.create_image(DrawPosX, DrawPosY, image = Buildinglist[1]))
                        #gameEntities.append(BuildingMap[MapInfo.index(row)][row.index(column)][1])
                    elif isinstance(CurrentBuilding, EntCl.Builder):
                        print("Here Builder " + CurrentBuilding.Alliance )
                        print(str(MapInfo.index(row))+ "," + str(row.index(column)))
                        if CurrentBuilding.Alliance == "Red":
                            BuildingMap[MapInfo.index(row)][row.index(column)][1]=(canv.create_image(DrawPosX, DrawPosY, image = Trooplist[1]))
                            #gameEntities.append(BuildingMap[MapInfo.index(row)][row.index(column)][1])
                        elif CurrentBuilding.Alliance == "Blue":
                            BuildingMap[MapInfo.index(row)][row.index(column)][1]=(canv.create_image(DrawPosX, DrawPosY, image = Trooplist[0]))
                            #gameEntities.append(BuildingMap[MapInfo.index(row)][row.index(column)][1])
                    else:
                        print("Unit Error")
                        print(type(CurrentBuilding))
                else:
                    TempX = canv.coords(BuildingMap[MapInfo.index(row)][row.index(column)][1])[0]
                    TempY = canv.coords(BuildingMap[MapInfo.index(row)][row.index(column)][1])[1]
                    canv.move(BuildingMap[MapInfo.index(row)][row.index(column)][1],DrawPosX-TempX,DrawPosY-TempY)
            colCount = 0
            DrawPosX+=TileSize
            #print(DrawPosX)
        rowCount += 1
        DrawPosX = DrawPosXOrg
        DrawPosY+=TileSize
        #print(DrawPosY)
    DrawPosX= DrawPosXOrg
    DrawPosY = DrawPosYOrg
    rowCount = 0
    colCount = 0
    """
    print(MapInfo)
    for item in canv.find_all():
        print(canv.type(item))
        print(canv.coords(item))"""
    #print(BuildingMap)
    #print(gameEntities)
    
    UpdateEntities()

def UpdateEntities():
    print("At Update Ent")
    global Selectables
    global BuildingMap
    #print(BuildingMap)
    iterX = 0
    iterY = 0
    for row in BuildingMap:
        for column in row:
            if column[0] !=False and column[1] != "":
                Selectables.append([column[1],iterX,iterY])
            iterY += 1
        iterY = 0
        iterX+=1
    #print(Selectables)
    print("leaving Update Ent")
        
def Turn():
    DrawMap()
    
def KeyCheck():
    global ActiveKeys
    print("Here")
    if ActiveKeys != False:
        if 65 in ActiveKeys:
            Left()
            canv.update()
        if 87 in ActiveKeys:
            Up()
            canv.update()
        if 83 in ActiveKeys:
            Down()
            canv.update()
        if 68 in ActiveKeys:
            Right()
            canv.update()
    print(Selector)
    DrawMap()
    
def PrintStuff():
    global Selectables
    print(Selectables)

def MotionUpdate(event):
    canv.delete("all")
    DrawMap()

def MouseDown(event):
    global MXD,MYD
    MXD = event.x
    MYD = event.y
    #print("Mouse 1 Down")
    
def MouseUp(event):
    global MXU, MYU
    MXU = event.x
    MYU = event.y
    UpdateEntities()
    print(Selector)
    ClickCheck()
    #print("Mouse 1 Up")

def KeyLogger(event):
    global ActiveKeys
    #print("Here")
    if event.keycode not in ActiveKeys:
        ActiveKeys.append(event.keycode)
    KeyCheck()
        
def KeyPopper(event):
    global ActiveKeys
    if event.keycode in ActiveKeys:
        ActiveKeys.pop(ActiveKeys.index(event.keycode))

def Left():
    #print("Here")
    global Selector
    if Selector[0] > 0:
        Selector[0] = Selector[0] -1
    
def Right():
    #print("Here")
    global Selector
    if Selector[0] < MapH - 1:
        Selector[0] = Selector[0] +1
    
def Up():
    #print("Here")
    global Selector
    if Selector[1] > 0:
        Selector[1] = Selector[1] -1
    
def Down():
    #print("Here")
    global Selector
    if Selector[1] < MapW - 1:
        Selector[1] = Selector[1] +1


Play = tk.Button(TL, text = "Play!", command = Init)
Play.grid(column = 1, row = 2)

Exit = tk.Button(TL, text="Exit", command=TL.quit)
Exit.grid(column = 1,row = 3)

NxtTurn = tk.Button(TL, text= "Next Turn", command=Turn())
NxtTurn.grid(column = 0, row = 2)

Export = tk.Button(TL, text = "Save and Export!")
Export.grid(column = 0, row = 3)

DebugHelp = tk.Button(TL, text = "Debugger", command = PrintStuff())
DebugHelp.grid(column = 2, row  = 2)

canv.bind('<Motion>')
canv.bind('<ButtonPress-1>', MouseDown)
canv.bind('<ButtonRelease-1>', MouseUp)
canv.bind_all("<KeyPress>", KeyLogger)
canv.bind_all("<KeyRelease>", KeyPopper)


TL.mainloop()

TL.destroy()
sys.exit()