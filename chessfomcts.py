def newboard():
    # 0 is capital
    # (board state, turn, flags) -- flags = (0ck, 0cq, 1ck, 1cq, pdp)
    return (('rnbqkbnr','p'*8,)+(' '*8,)*4+('P'*8,'RNBQKBNR'),0,(1,1,1,1,0));

def prinboard(b):
    print ['White','Black'][b[1]]+'\'s turn:\n\n  0 1 2 3 4 5 6 7';
    print '\n'.join(map(lambda i:str(i)+' '+' '.join(b[0][i]),range(len(b[0]))));
    print;

def getp(x,y,b):
    return b[0][y][x];

def playmove(m,b):
    if len(m) == 5:
        m,p = m[:4],m[4];
        x0,y0,x,y = map(int,m);
    else:
        x0,y0,x,y = map(int,m);
        p = l[y0][x0];
    l = map(list,b[0]);
    l[y][x] = p;
    l[y0][x0] = ' ';
    return (tuple(map(''.join,l)),1-b[1],b[-1]);

def pawnmoves(x,y,b):
    # pawns are actually annoying
    # anyways promotions are 'xyxyp' with p the piece to become
    pass;

def rookmoves(x,y,b):
    if getp(x,y,b) != 'Rr'[b[1]]:
        return [];
    z = [];
    take = 'rnbqkp';
    if b[1]:
        take = take.upper();
    for i in range(x+1,len(b[0][0])):
        q = getp(i,y,b);
        if q not in take+' ': break;
        z.append(str(x)+str(y)+str(i)+str(y));
        if q in take: break;
    for i in range(x-1,-1,-1):
        q = getp(i,y,b);
        if q not in take+' ': break;
        z.append(str(x)+str(y)+str(i)+str(y));
        if q in take: break;
    for i in range(y+1,len(b[0])):
        q = getp(x,i,b);
        if q not in take+' ': break;
        z.append(str(x)+str(y)+str(x)+str(i));
        if q in take: break;
    for i in range(y-1,-1,-1):
        q = getp(x,i,b);
        if q not in take+' ': break;
        z.append(str(x)+str(y)+str(x)+str(i));
        if q in take: break;
    return z;

def bishopmoves(x0,y0,b):
    if getp(x0,y0,b) != 'Bb'[b[1]]:
        return [];
    z = [];
    take = 'rnbqkp';
    if b[1]:
        take = take.upper();
    for v in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        x,y = x0+v[0],y0+v[1];
        while 0 <= x < len(b[0][0]) and 0 <= y < len(b[0]):
            q = getp(x,y,b);
            if q not in take+' ': break;
            z.append(str(x0)+str(y0)+str(x)+str(y));
            if q in take: break;
            x += v[0]; y += v[1];
    return z;

def knightmoves(x0,y0,b):
    if getp(x0,y0,b) != 'Nn'[b[1]]:
        return [];
    z = [];
    take = 'rnbqkp ';
    if b[1]:
        take = take.upper();
    for v in sum([((i,j),(j,i)) for i in (1,-1) for j in (2,-2)],()):
        x,y = x0+v[0],y0+v[1];
        if 0 <= x < len(b[0][0]) and 0 <= y < len(b[0]):
            q = getp(x,y,b);
            if q in take:
                z.append(str(x0)+str(y0)+str(x)+str(y));
    return z;

def queenmoves(x0,y0,b):
    if getp(x0,y0,b) != 'Bb'[b[1]]:
        return [];
    z = [];
    take = 'rnbqkp';
    if b[1]:
        take = take.upper();
    for v in [(i,j) for i in range(-1,2) for j in range(-1,2) if i*i+j*j>0]:
        x,y = x0+v[0],y0+v[1];
        while 0 <= x < len(b[0][0]) and 0 <= y < len(b[0]):
            q = getp(x,y,b);
            if q not in take+' ': break;
            z.append(str(x0)+str(y0)+str(x)+str(y));
            if q in take: break;
            x += v[0]; y += v[1];
    return z;

def kingmoves(x0,y0,b):
    if getp(x0,y0,b) != 'Kk'[b[1]]:
        return [];
    z = [];
    take = 'rnbqkp ';
    if b[1]:
        take = take.upper();
    for v in [(i,j) for i in range(-1,2) for j in range(-1,2) if i*i+j*j>0]:
        x,y = x0+v[0],y0+v[1];
        if 0 <= x < len(b[0][0]) and 0 <= y < len(b[0]):
            q = getp(x,y,b);
            if q in take:
                z.append(str(x0)+str(y0)+str(x)+str(y));
    return z;

def getmoves(b):
    z = [];
    for x in range(len(b[0][0])):
        for y in range(len(b[0])):
            p = getp(x,y,b);
            if p != ' ':
                z += {'p':pawnmoves,'r':rookmoves,'b':bishopmoves,'n':knightmoves,'q':queenmoves,'k':kingmoves}[p](x,y,b);

a=(('rnbqkbnr',
    'pppppppp',
    '        ',
    '        ',
    '        ',
    '  B     ',
    'PPPPPPPP',
    'RN QKBNR'), 0);
prinboard(a);
#bishopmoves(2,5,a);
