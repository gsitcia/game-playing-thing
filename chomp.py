import random;

"""
# the old way

def newboard(w,h):
    l = [];
    i = (0,0);
    v = (-1,1);
    while i != (w-1,h-1):
        l.append(i);
        #print i;
        i = (i[0]+v[0],i[1]+v[1]);
        s = False;
        if i[0] < 0:
            i = (i[0]+1,i[1]);
            s = True;
        if i[1] < 0:
            i = (i[0],i[1]+1);
            s = True;
        if i[0] == w:
            if not s:
                i = (i[0],i[1]+1);
            i = (i[0]-v[0],i[1]-v[1]);
            s = True;
        if i[1] == h:
            if not s:
                i = (i[0]+1,i[1]);
            i = (i[0]-v[0],i[1]-v[1]);
            s = True;
        if s:
            v = (-v[0],-v[1]);
        #if raw_input():
        #    break;
    return l+[(w-1,h-1)];

def removebox(l,x,y):
    i = l.index((x,y));
    while i < len(l):
        if l[i][0] >= x and l[i][1] >= y:
            l.pop(i);
        else:
            i += 1;
    return l;
"""

def newboard(w,h):
    return ((w,)*h,0);

def removebox(l,xy):
    x,y = xy;
    l,t = l;
    if x == 0:
        return (l[:y],1-t);
    i = y;
    z = list(l[:y]);
    while i < len(l):
        if l[i] < x:
            return (tuple(z)+l[i:],1-t);
        z.append(x);
        i += 1;
    return (tuple(z),1-t);

def printboard(l):
    if l[0] == ():
        return;
    l = l[0];
    if l == []:
        return;
    print 'XX'+'[]'*(l[0]-1);
    for i in l[1:]:
        print '[]'*i;

def getmoves(l):
    l = l[0];
    return sum([[(j,i) for j in xrange(l[i])] for i in xrange(len(l))],[]);

def ev(p):
    if p[0] == ():
        return p[1];
    return -1;

def gm():
    return eval(raw_input('Name your move: '));

