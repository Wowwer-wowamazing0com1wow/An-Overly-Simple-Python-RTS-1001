import numpy as np
import random as rand
import os
import EntityClasses as EntCl

def MapGen ( MapH, MapW):
    #For first int:1 is grassland, 2 is valley, 3 is mountain.
    #For second int: 1 is varient1, 2 is varient 2, 3 is varient 3
    MapInfo = []
    MapRowHolder = []
    for numH in range(MapH):
        for numW in range(MapW):
            MapRowHolder.append([rand.randint(1,3),rand.randint(1,3)])
        MapInfo.append(MapRowHolder)
        MapRowHolder = []
    return MapInfo
    
def Spawning(BuildingMap):
    BlueX = rand.randint(1,8)
    BlueY = rand.randint(1,4)
    RedX = rand.randint(1,8)
    RedY = rand.randint(5,8)
    BuildingMap[BlueY][BlueX][0] = EntCl.Castle("Blue",[BlueX,BlueY],"DragonKnight")
    BuildingMap[BlueY][BlueX+1][0] = EntCl.Builder("Blue",[BlueX,BlueY+1])
    BuildingMap[RedY][RedX][0] = EntCl.Castle("Red",[RedX,RedY],"DragonKnight")
    BuildingMap[RedY][RedX+1][0] = EntCl.Builder("Red",[RedX,RedY+1])
    #print(BuildingMap)
    return BuildingMap

def PhotoLoader(Subfolder):
    cwd = os.getcwd()+"\Downloads\PyprojectCreateTask\RTS Sprites"+Subfolder
    print(cwd)
    Photolist = os.listdir(cwd)
    
    for Photo in Photolist:
        Photolist[Photolist.index(Photo)] = cwd+"\\"+ Photolist[Photolist.index(Photo)]
    return Photolist
    
def HitboxMaker(canvas, Entity):
    print("Entered HitBoxMaker")
    # fit in this order [TopSide,LeftSide,BottomSide,RightSide]
    print(Entity)
    print("= Entity")
    coords = canvas.bbox(Entity[0])
    HitboxHolder = []
    if coords[0] < coords[2]:
        HitboxHolder.append(coords[0])
        if coords[1] < coords[3]:
            HitboxHolder.append(coords[1])
            HitboxHolder.append(coords[2])
            HitboxHolder.append(coords[3])
        else:
            HitboxHolder.append(coords[3])
            HitboxHolder.append(coords[2])
            HitboxHolder.append(coords[1])
    else:
        HitboxHolder.append(coords[2])
        if coords[1] < coords[3]:
            HitboxHolder.append(coords[1])
            HitboxHolder.append(coords[0])
            HitboxHolder.append(coords[3])
        else:
            HitboxHolder.append(coords[3])
            HitboxHolder.append(coords[0])
            HitboxHolder.append(coords[1])
    return HitboxHolder
    

        
#print(PhotoLoader())