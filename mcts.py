import math, random, thread, time

def uct(w,n,N,c):
    return w/n+c*math.sqrt(math.log(N)/n);

def prin(s):
    print(s);

class tree:
    """This class takes as input a game position and three functions (and optionally a value for c)
    the first function moves(pos) returns a list of moves
    the second function play(pos,move) plays a move
    the third function ev(pos) says if a game is won (and by who) -1 is no one, 0 is first player, 1 is second player, 0.5 is tie"""
    def __init__(self,pos,moves,play,ev,player=0,c=1.41421):
        self.pos = pos;
        self.gm = moves;
        self.moves = {i:[0.5,1,None] for i in moves(pos)};
        self.play = play;
        self.ev = ev;
        self.c = c;
        self.n = 1;
        self.player = player;
        self.eva = ev(pos);
        self.ds = {self.pos:self};
    def select(self,hiss=[]):
        if self.eva != -1:
            return self.eva;
        if self.pos in hiss:
            #return 0.5; # tie # this hiss thing avoids infinite repetition (because if it happens, it will happen every time)
            # it's probably better to lose, since the select thing will always go that way if it winds up going that way
            # or rather the guy who gave us a postion we've already had should lose
            return self.player;
        move = max(self.moves,key=lambda i:uct(self.moves[i][0],self.moves[i][1],self.n,self.c));
        if self.moves[move][-1]:
            # the next node exists, select it!
            w = self.moves[move][-1].select(hiss+[self.pos]);
        else:
            # time to play out the game
            p = self.play(self.pos,move);
            if p in self.ds:
                t = self.ds[p];
            else:
                t = tree(p,self.gm,self.play,self.ev,1-self.player,self.c);
                t.ds = self.ds;
                self.ds[p] = t;
            self.moves[move][-1] = t;
            w = t.playout();
        # w is who one that
        self.moves[move][1] += 1;
        self.moves[move][0] += 1-abs(w-self.player);
        self.n += 1;
        return w;
    def playout(self):
        p = self.pos;
        r = self.eva;
        while r == -1:
            p = self.play(p,random.choice(self.gm(p)));
            r = self.ev(p);
        return r;
    def robest(self):
        return max(self.moves,key=lambda i:self.moves[i][1]);
    def bestav(self):
        return max(self.moves,key=lambda i:self.moves[i][0]/self.moves[i][1]);
    def start(self):
        def lol(a):
            i = 0;
            l = 0;
            upd = 1000000;
            inv = 50;
            while True:
                q = a.select();
                if i%upd > upd-inv:
                    l += q;
                if i%upd == upd-1:
                    l /= inv-1.0;
                    print 'Your millionial update: '+str(l);
                    l = 0;
                i += 1;
        thread.start_new_thread(lol,(self,));
    def stop(self):
        k = self.select;
        self.select = 'lol';
        time.sleep(0.1);
        self.select = k;

def playgame(a,pr=prin):
    while a.eva == -1:
        pr(a.pos);
        print;
        a = a.moves[a.robest()][-1];
    pr(a.pos);

def test(a,n=10000):
    l=[0.5]*10;
    for i in range(n):
        l.pop(0);
        l.append(a.select());
    return float(sum(l))/len(l);

def solve(*p):
    return a.ds[(p,0)].robest();

#a=tree(newboard(6,3),getmoves,removebox,ev,0);
#test(a);
#a.start();

class player:
    def __init__(self,t,pr,gm):
        self.t = t;
        self.cn = t;
        self.pr = pr;
        self.gm = gm;
        self.start();
    def think(self):
        while True:
            self.cn.select();
    def start(self):
        thread.start_new_thread(self.think,());
    def prin(self):
        self.pr(self.cn.pos);
    def move(self,m):
        if self.cn.eva != -1:
            print('The game is over!');
            return;
        self.cn = self.cn.moves[m][-1];
        if self.cn.eva != -1:
            print('The game is '+{0:'won by the first player',1:'won by the second player',0.5:'tied'}[self.cn.eva]);
        else:
            pass;
            #self.prin();
    def selfmove(self):
        if self.cn.eva != -1:
            print('The game is over!');
            return;
        self.move(self.cn.robest());
    def getmove(self):
        if self.cn.eva != -1:
            print('The game is over!');
            return;
        print('Current position:');
        self.prin();
        self.move(self.gm());
    def reset(self):
        self.cn = self.t;
    def stop(self):
        a = self.cn;
        self.cn = None;
        time.sleep(0.1);
        self.cn = a;
    def play(self,t=5):
        self.reset();
        p = int((raw_input('Do you want to be first? ')+' ')[0].lower() == 'y');
        #supermarket flowers
        if p == 0:
            self.prin();
            time.sleep(t);
            self.selfmove();
        while self.cn.eva == -1:
            try:
                self.getmove();
            except:
                print('Try again.');
                continue;
            self.prin();
            if self.cn.eva != -1:
                break;
            time.sleep(t);
            self.selfmove();
        print('You were '+['second','first'][p]);

a=player(tree(newboard(5,4),getmoves,removebox,ev),printboard,gm);
