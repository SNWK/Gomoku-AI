import numpy as np
import random
import time

COLOR_BLACK=-1
COLOR_WHITE=1
COLOR_NONE=0
INFINITY = 10000099999
minx = 14
miny = 14
maxx = 0
maxy = 0
random.seed(0)
LEVEL= 4
#don't change the class name
class AI(object):
#chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        #You are white or black
        self.color = color
        #the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need add your decision into your candidate_list. System will get the end of your candidate_list as your decision .
        self.candidate_list = []
        print ("color",color)



    # The input is current chessboard.
    def go(self, chessboard):
    # Clear candidate_list
        print (chessboard)
        self.candidate_list.clear()
        idx = get(self.color,chessboard)
        print("??",idx)
        max = -10000000000
        if len(idx) == 1:
            self.candidate_list.append (idx[0])
        else:
            self.candidate_list.append (idx[0])
            for i in range(0,len(idx)):
                if i == 0:
                    value = minn(idx[i],self.color,LEVEL,chessboard,-10000000000)
                    print (idx[i], value)
                else:
                    node = idx[i]
                    value = minn(idx[i],self.color,LEVEL,chessboard,max)
                    print(node,value)

                if value > max:
                    self.candidate_list.append(idx[i])
                    max = value



        print(self.candidate_list)
def minn(node, color, level, chessboard,max):
    #print("FUCK")
    chessboard[node[0]][node[1]] = color
    value = OnePointValue(node,  chessboard)
    if node == (1,1):
        print("ssssssss",node,value,chessboard)
    #if value >= 100000:
    #    chessboard[node[0]][node[1]] = 0
    #    return INFINITY + level
    #elif value >= 30000 and LEVEL - level <= 2:
    #    chessboard[node[0]][node[1]] = 0
    #    return value + 9000
#
    #if level <= 0:
    #    value = JUMIAN(node,color,chessboard)
    #    chessboard[node[0]][node[1]] = 0
    #    return value

    nodes, womax = get2(-color,node,chessboard) #敌方落子是womax

    if value >= 100000:
        chessboard[node[0]][node[1]] = 0
        return INFINITY + level
    elif value >= 30000 and womax < 100000:
        chessboard[node[0]][node[1]] = 0
        return value + level + 100000
    elif value >= 10000 and womax < 30000:
        chessboard[node[0]][node[1]] = 0
        return value + level + 100000
    elif level <= 0:
        value = JUMIAN (node, color, chessboard)
        chessboard[node[0]][node[1]] = 0
        return value

    print(level,"nodes",nodes)

    if nodes == []:
        min = JUMIAN (node, color, chessboard)

    for i in range(0, len(nodes)):
        if i == 0:
            min = maxm (nodes[0], -color, level-1, chessboard,INFINITY)
            #if nodes[0] == (8,3):
            #    print("sssssssss",nodes[0],min)
        else:
            value = maxm(nodes[i], -color, level-1, chessboard,min)
            if value < min:
                min = value
                #print(node,value)
        if min <= max or min <= -INFINITY:
            break
    chessboard[node[0]][node[1]] = 0
    return min

def maxm(node, color, level, chessboard,min):
    chessboard[node[0]][node[1]] = color
    value = OnePointValue(node,chessboard)
    #if node == (8,3):
    #    print (value)
    #if value >= 100000 :
    #    chessboard[node[0]][node[1]] = 0
    #    print(node,"changlian")
    #    return -INFINITY-level
    #elif value >= 30000 and LEVEL - level == 1:
    #    chessboard[node[0]][node[1]] = 0
    #    return -value - level
    #elif value >= 10000 and LEVEL - level == 3:
    #    chessboard[node[0]][node[1]] = 0
    #    return -value - level
#
    #if level <= 0:
    #    value = JUMIAN(node,color,chessboard)
    #    chessboard[node[0]][node[1]] = 0
    #    return -value

    nodes, womax = get2(-color, node,chessboard)
    #if node == (8,3):
    #    print(womax)
    if value >= 100000:
        chessboard[node[0]][node[1]] = 0
        return -INFINITY - level
    elif value >= 30000 and womax < 100000:
        chessboard[node[0]][node[1]] = 0
        return -value - level
    elif value >= 10000 and womax < 30000:
        chessboard[node[0]][node[1]] = 0
        return -value - level
    elif level <= 0:
        value = JUMIAN (node, color, chessboard)
        chessboard[node[0]][node[1]] = 0
        return -value
    #print (level, "nodes", nodes)
    if nodes == []:
        max = -JUMIAN (node, color, chessboard)

    for i in range (0, len (nodes)):
        if i == 0:
            max = minn (nodes[0], -color, level - 1, chessboard,-INFINITY)
        else:
            value = minn (nodes[i], -color, level - 1, chessboard,max)
            if value > max:
                max = value
        if max >= min:
            break
    chessboard[node[0]][node[1]] = 0
    return max


def get(color,chessboard):
    youzhi = np.where (chessboard != COLOR_NONE)
    youzhi = list (zip (youzhi[0], youzhi[1]))
    #print(youzhi)
    global minx
    global miny
    global maxx
    global maxy
    minx, miny = 14, 14
    maxx, maxy = 0, 0
    if youzhi == []:
        center = [(7,7)]
        minx, miny = 7, 7
        maxx, maxy = 7, 7
        return center
    for i in range(0,len(youzhi)):
        if youzhi[i][0] < minx : minx = youzhi[i][0]
        if youzhi[i][1] < miny: miny = youzhi[i][1]
        if youzhi[i][0] > maxx : maxx = youzhi[i][0]
        if youzhi[i][1] > maxy: maxy = youzhi[i][1]
    idx = np.where (chessboard == COLOR_NONE)
    idx = list(zip (idx[0], idx[1]))
    #print(idx)
    print(minx,miny,maxx,maxy)
    key = []
    for i in range (0, len (idx)):
        #print("jj",idx[i])
        if idx[i][0] < minx - 3 or idx[i][1] < miny - 3 or idx[i][0] > maxx + 3 or idx[i][1] > maxy + 3 or inneighber(idx[i],chessboard):
            key.append (i)
    key.sort (reverse=True)
    for i in range (0, len (key)):
        idx.pop (key[i])
    sortt = []
    for i in range (0, len (idx)):
        node = idx[i]
        chessboard[node[0]][node[1]] = color
        # print (Tchessboard)
        value = OnePointValue (node, chessboard)
        chessboard[node[0]][node[1]] = -color
        # print (Tchessboard)
        value += 0.9 * OnePointValue (node, chessboard)
        chessboard[node[0]][node[1]] = 0
        value -= abs(node[0] - len(chessboard[0])/2) + abs(node[1] - len(chessboard[0])/2)
        sortt.append ((i, value))
        print ("jj", idx[i],value)

    sortt.sort (key=takeSecond,reverse = True)
    print (sortt)
    final = []
    for i in range (0, 3):
        if i >= len (sortt):
            break
        final.append (idx[sortt[i][0]])
    print(final)
    #idx.sort(key=takeSecond,reverse=True)
    return final

def get2(color,node,chessboard):
    global minx
    global miny
    global maxx
    global maxy
    womax= 0
    #print("????????????????????????????????")
    idx = np.where (chessboard == COLOR_NONE)
    idx = list (zip (idx[0], idx[1]))
    # print(idx)
    #print(minx,miny,maxx,maxy)
    key = []
    for i in range (0, len (idx)):
        if i >= len (idx): break
        if idx[i][0] < minx - 1 or idx[i][1] < miny - 1 or idx[i][0] > maxx + 1 or idx[i][1] > maxy + 1 or inneighber(idx[i],chessboard):
            key.append(i)
    key.sort(reverse=True)
    for i in range(0,len(key)):
        idx.pop(key[i])
    sortt = []
    for i in range(0,len(idx)):
        node = idx[i]
        chessboard[node[0]][node[1]] = color
        # print (Tchessboard)
        value = OnePointValue (node, chessboard)

        if value > womax:  #找到我方最有利的点 及其估值
            womax = value


        chessboard[node[0]][node[1]] = -color
        # print (Tchessboard)
        nvalue = OnePointValue (node, chessboard)

        value += 0.9*nvalue
        value -= abs(node[0] - len(chessboard[0]) / 2) + abs(node[1] - len(chessboard[0]) / 2)
        chessboard[node[0]][node[1]] = 0
        sortt.append ((i, value))

    sortt.sort (key=takeSecond, reverse=True)
    final = []
    for i in range(0,3):
        if i >= len(sortt):
            break
        final.append(idx[sortt[i][0]])
    return final, womax

def takeSecond(elem):
    return elem[1]



def JUMIAN(node,color, Tchessboard):
    global minx
    global miny
    global maxx
    global maxy
    womax = 0
    dimax = 0
    # print("????????????????????????????????")
    idx = np.where (Tchessboard == COLOR_NONE)
    idx = list (zip (idx[0], idx[1]))
    # print(idx)
    # print(minx,miny,maxx,maxy)
    key = []
    for i in range (0, len (idx)):
        if i >= len (idx): break
        if idx[i][0] < minx - 1 or idx[i][1] < miny - 1 or idx[i][0] > maxx + 1 or idx[i][1] > maxy + 1 or inneighber (
                idx[i], Tchessboard):
            key.append (i)
    key.sort (reverse=True)
    for i in range (0, len (key)):
        idx.pop (key[i])
    sortt = []
    for i in range (0, len (idx)):
        node = idx[i]
        Tchessboard[node[0]][node[1]] = color
        # print (Tchessboard)
        value = OnePointValue (node, Tchessboard)
        #Tchessboard[node[0]][node[1]] = 0
        if value > womax:  # 找到我方最有利的点 及其估值
            womax = value

        Tchessboard[node[0]][node[1]] = -color
        # print (Tchessboard)
        nvalue = OnePointValue (node, Tchessboard)
        Tchessboard[node[0]][node[1]] = 0
        if nvalue > dimax:
            dimax = nvalue

    if dimax >= 100000:
        return -INFINITY
    elif womax >= 100000 and dimax < 100000:
        return INFINITY
    elif dimax >= 30000:
        return -dimax
    elif womax >= 30000 and dimax < 30000:
        return womax
    elif dimax >= 10000:
        return -dimax
    elif womax >= 10000 and dimax < 10000:
        return womax
    else:
        return womax - 0.9*dimax

def OnePointValue (point, chessboard):
    dir = []
    dir.append(DIR_UP(point, chessboard))
    dir.append (DIR_UPRIGHT(point, chessboard))
    dir.append (DIR_RIGHT(point, chessboard))
    dir.append (DIR_RIGHTDOWN(point, chessboard))
    dir.append (DIR_DOWN(point, chessboard))
    dir.append (DIR_DOWNLEFT(point, chessboard))
    dir.append (DIR_LEFT(point, chessboard))
    dir.append (DIR_LEFTUP(point, chessboard))
    #for i in dir: print(i)
    none, changlian, huosi, chongsi, huosan,  miansan, huoer, mianer, sisi, sisan, sier = 0,0,0,0,0,0,0,0,0,0,0
    #if point == (1,9):
    #    for i in dir: print (i)
    for i in range(4):
        if dir[i][0] + dir[i+4][0] >= 4:
            changlian += 1
        elif dir[i][0] + dir[i+4][0] == 3 and dir[i][1] + dir[i+4][1] == 0:
            huosi += 1
        elif (dir[i][0] + dir[i+4][0] == 3 and ((dir[i][1] == 1 and dir[i+4][2] != 0) or (dir[i+4][1] == 1 and dir[i][2] != 0))) or (dir[i][0] + dir[i+4][0] == 2 and dir[i][1] + dir[i+4][1] == 0 and (dir[i][2] >= 1.5 or  dir[i+4][2] >= 1.5)) or (dir[i][0] + dir[i+4][0] == 0 and dir[i][1] + dir[i+4][1] == 0 and (dir[i][2] >= 3.5 or  dir[i+4][2] >= 3.5)) or(dir[i][0] + dir[i+4][0] == 1 and dir[i][1] + dir[i+4][1] == 0 and (dir[i][2] >= 2 or  dir[i+4][2] >= 2)):
            chongsi += 1
        elif (dir[i][0] + dir[i + 4][0] == 2 and dir[i][1] + dir[i + 4][1] == 0) or (dir[i][0] + dir[i + 4][0] == 0 and dir[i][1] + dir[i + 4][1] == 0 and (dir[i][2] >= 2.5 or dir[i + 4][2] >= 2.5)):
            huosan += 1
            #print (point, "huosan +1")
        elif dir[i][0] + dir[i + 4][0] == 1 and dir[i][1] + dir[i + 4][1] == 0 and (dir[i][2] == 1.5 or dir[i + 4][2] == 1.5):
            huosan += 1
            #print (point, "huosan ++1")
        elif (dir[i][0] + dir[i+4][0] == 2 and dir[i][1] + dir[i+4][1] == 1 and (dir[i][2] != 0 or dir[i+4][2] != 0) )     or (dir[i][0] + dir[i+4][0] == 1 and dir[i][1] + dir[i+4][1] == 1 and (dir[i][2] == 1.5 or  dir[i+4][2] == 1.5)) or (dir[i][0] + dir[i+4][0] == 0 and dir[i][1] + dir[i+4][1] == 0 and (dir[i][2] == 2 or  dir[i+4][2] == 2))     or(dir[i][0] + dir[i+4][0] == 1 and dir[i][1] + dir[i+4][1] == 0 and (dir[i][2] == 1 or  dir[i+4][2] == 1)) or (dir[i][0] + dir[i+4][0] == 0 and dir[i][1] + dir[i+4][1] == 1 and (dir[i][2] == 2.5 or  dir[i+4][2] == 2.5))      or(dir[i][0] + dir[i+4][0] == 0 and dir[i][1] + dir[i+4][1] == 0 and dir[i][2] == 1.5 and  dir[i+4][2] == 1.5)    or(dir[i][0] + dir[i+4][0] == 2 and dir[i][1] + dir[i+4][1] == 0 and dir[i][2] == 0 and  dir[i+4][2] == 0):
            miansan += 1 #que 10011
        elif (dir[i][0] + dir[i+4][0] == 1 and dir[i][1] + dir[i+4][1] == 0 and dir[i][2] == 0.5 and dir[i+4][2] == 0.5) or (dir[i][0] + dir[i+4][0] == 0 and dir[i][1] + dir[i+4][1] == 0 and dir[i][2] == 1.5 and dir[i+4][2] == 0.5) or (dir[i][0] + dir[i+4][0] == 1 and dir[i][1] + dir[i+4][1] == 0 and dir[i][2] == 0.5 and dir[i+4][2] == 1.5):
            huoer += 1 # que 010010
        elif (dir[i][0] + dir[i+4][0] == 3 and dir[i][1] + dir[i+4][1] == 2) or(dir[i][0] + dir[i+4][0] == 3 and dir[i][1] + dir[i+4][1] == 1 and (dir[i][2] == 0 or dir[i+4][2] == 0)) :
            sisi += 1
        elif dir[i][0] + dir[i+4][0] == 2 and dir[i][1] + dir[i+4][1] == 2:
            sisan += 1
        elif dir[i][0] + dir[i+4][0] == 1 and dir[i][1] + dir[i+4][1] == 2:
            sier += 1
        elif dir[i][0] + dir[i+4][0] == 0 and dir[i][1] + dir[i+4][1] == 0 and dir[i][2] == 0.5 and dir[i+4][2] == 0.5:
            none += 1
        else:
            mianer += 1 #duo 10011 010010

    if changlian >= 1:
        value = 100000
    elif huosi > 1 or chongsi >= 2 or (huosi >= 1 and huosan >= 1):
        value = 60000
    elif huosi == 1:
        value = 30000
    elif (chongsi >= 1 and huosan >= 1) :
        value = 20000
    elif (huosan >= 2):
        value = 10000
    elif chongsi == 1:
        value = 1500
    elif chongsi == 1 and miansan == 1:
        value = 3000
    elif huosan == 1 and miansan > 1:
        value = 1000
    elif miansan == 1:
        value = 50
    elif huosan == 1: #que mian si
        value = 900
    elif huoer >= 1 and mianer >= 1:
        value = 100
    elif huoer == 1:
        value = 50
    elif mianer == 1:
        value = 30
    elif sisi >= 1:
        value = -3
    elif sisan >= 1:
        value = -5
    elif sier >= 1:
        value = -10
    else:
        value = 0

    return value

def DIR_UP (point, chessboard):
    n = 0
    du = 0
    off = 0
    x = point[0]
    y = point[1]
    for i in range(1, 6):
        if judge(y+i,len(chessboard[0])):
            du = -100
            break
        if chessboard[x][y + i] == chessboard[x][y]:
            n = n + 1
        elif chessboard[x][y + i] == -chessboard[x][y]:
            du = 1
            break
        else:
            for j in range(i+1,i+5):
                if judge (y + j, len (chessboard[0])):
                    break
                if chessboard[x][y + j] == -chessboard[x][y]:
                    break
                if chessboard[x][y + j] == chessboard[x][y]:
                    off = off + 1
                elif chessboard[x][y + j] == 0:
                    off = off + 0.5
                    break
            du = 0
            break
    num = [n, du, off]
    return num
def DIR_UPRIGHT (point, chessboard):

    n = 0
    du = 0
    x = point[0]
    y = point[1]
    off = 0

    for i in range (1, 6):
        if judge(y+i,len(chessboard[0])) or judge(x+i,len(chessboard[0])):
            du = -100
            break
        if chessboard[x + i][y + i] == chessboard[x][y]:
            n = n + 1
        elif chessboard[x + i][y + i] == -chessboard[x][y]:
            du = 1
            break
        else:
            for j in range(i+1,i+5):
                if judge (y + j, len (chessboard[0])) or judge (x + j, len (chessboard[0])):
                    break
                if chessboard[x+j][y + j] == -chessboard[x][y]:
                    break
                if chessboard[x + j][y + j] == chessboard[x][y]:
                    off = off + 1
                elif chessboard[x + j][y + j] == 0:
                    off = off + 0.5
                    break
            du = 0
            break

    num = [n, du, off]
    return num
def DIR_RIGHT (point, chessboard):
    n = 0
    du = 0
    off = 0
    x = point[0]
    y = point[1]
    for i in range (1, 6):
        if judge(x+i,len(chessboard[0])):
            du = -100
            break
        if chessboard[x + i][y] == chessboard[x][y]:
            n = n + 1
        elif chessboard[x + i][y] == -chessboard[x][y]:
            du = 1
            break
        else:
            for j in range(i+1,i+5):
                if judge (x + j, len (chessboard[0])):
                    break
                if chessboard[x+j][y] == -chessboard[x][y]:
                    break
                if chessboard[x + j][y] == chessboard[x][y]:
                    off = off + 1
                elif chessboard[x+ j][y ] == 0:
                    off = off + 0.5
                    break
            du = 0
            break
    num = [n, du, off]
    return num
def DIR_RIGHTDOWN (point, chessboard):
    n = 0
    du = 0
    off = 0
    x = point[0]
    y = point[1]
    for i in range (1, 6):
        if judge(x+i,len(chessboard[0])) or judge(y-i,len(chessboard[0])):
            du = -100
            break
        if chessboard[x + i][y - i] == chessboard[x][y]:
            n = n + 1
        elif chessboard[x + i][y - i] == -chessboard[x][y]:
            du = 1
            break
        else:
            for j in range(i+1,i+5):
                if judge (x + j, len (chessboard[0])) or judge (y - j, len (chessboard[0])):
                    break
                if chessboard[x + j][y - j]== -chessboard[x][y]:
                    break
                if chessboard[x + j][y - j] == chessboard[x][y]:
                    off = off + 1
                elif chessboard[x+ j][y - j] == 0:
                    off = off + 0.5
                    break
            du = 0
            break
    num = [n, du, off]
    return num
def DIR_DOWN (point, chessboard):
    n = 0
    du = 0
    off = 0
    x = point[0]
    y = point[1]
    for i in range (1, 6):
        if judge(y-i,len(chessboard[0])):
            du = -100
            break
        if chessboard[x][y - i] == chessboard[x][y]:
            n = n + 1
        elif chessboard[x][y - i] == -chessboard[x][y]:
            du = 1
            break
        else:
            for j in range(i+1,i+5):
                if judge (y - j, len (chessboard[0])):
                    break
                if chessboard[x][y - j] == -chessboard[x][y]:
                    break
                if chessboard[x][y - j] == chessboard[x][y]:
                    off = off + 1
                elif chessboard[x][y - j] == 0:
                    off = off + 0.5
                    break
            du = 0
            break
    num = [n, du, off]
    return num
def DIR_DOWNLEFT (point, chessboard):
    n = 0
    du = 0
    off = 0
    x = point[0]
    y = point[1]
    for i in range (1, 6):
        if judge(x-i,len(chessboard[0])) or judge(y-i,len(chessboard[0])):
            du = -100
            break
        if chessboard[x - i][y - i] == chessboard[x][y]:
            n = n + 1
        elif chessboard[x - i][y - i] == -chessboard[x][y]:
            du = 1
            break
        else:
            for j in range(i+1,i+5):
                if judge (x - j, len (chessboard[0])) or judge (y - j, len (chessboard[0])):
                    break
                if chessboard[x - j][y - j] == -chessboard[x][y]:
                    break
                if chessboard[x - j][y - j] == chessboard[x][y]:
                    off = off + 1
                elif chessboard[x - j][y - j] == 0:
                    off = off + 0.5
                    break
            du = 0
            break
    num = [n, du, off]
    return num
def DIR_LEFT (point, chessboard):
    n = 0
    du = 0
    off = 0
    x = point[0]
    y = point[1]
    for i in range (1, 6):
        if judge(x-i,len(chessboard[0])):
            du = -100
            break
        if chessboard[x-i][y] == chessboard[x][y]:
            n = n + 1
        elif chessboard[x-i][y] == -chessboard[x][y]:
            du = 1
            break
        else:
            for j in range(i+1,i+5):
                if judge (x - j, len (chessboard[0])):
                    break
                if chessboard[x - j][y] == -chessboard[x][y]:
                    break
                if chessboard[x - j][y] == chessboard[x][y]:
                    off = off + 1
                elif chessboard[x - j][y] == 0:
                    off = off + 0.5
                    break
            du = 0
            break
    num = [n, du, off]
    return num

def DIR_LEFTUP (point, chessboard):
    n = 0
    du = 0
    off = 0
    x = point[0]
    y = point[1]
    for i in range (1, 6):
        if judge(x-i,len(chessboard[0])) or judge(y+i,len(chessboard[0])):
            du = -100
            break
        if chessboard[x-i][y + i] == chessboard[x][y]:
            n = n + 1
        elif chessboard[x-i][y + i] == -chessboard[x][y]:
            du = 1
            break
        else:
            for j in range(i+1,i+5):
                if judge (x - j, len (chessboard[0])) or judge (y + j, len (chessboard[0])):
                    du = -100
                    break
                if chessboard[x - j][y + j] == -chessboard[x][y]:
                    break
                if chessboard[x - j][y + j] == chessboard[x][y]:
                    off = off + 1
                elif chessboard[x - j][y + j] == 0:
                    off = off + 0.5
                    break
            du = 0
            break
    num = [n, du, off]
    return num

def judge(a,size):
    if(a<0 or a > size-1):
        return True
    else:
        return False

def inneighber(node,chessboard):

    minx = max(node[0] - 2,0)
    maxx = min(node[0] + 2, len(chessboard[0])-1)
    miny = max (node[1] - 2, 0)
    maxy = min (node[1] + 2, len (chessboard[0])-1)
    for i in range(minx,maxx+1):
        for j in range(miny,maxy+1):
            if i == node[0] and j == node[1]:
                continue
            elif chessboard[i][j] != 0:
                return False

    return True