import pyxel
from  random import randint
 
class App:
    def __init__(self):
        pyxel.init(160, 120)
 
        pyxel.load("final.pyxres")
 
        #STARTFLAG
        self.START = False
 
        #GAMEOVERフラグ
        self.GAMEOVER = False
 
        #スコア用変数
        self.score = 0
 
        #プレイヤー初期地位
        self.player_x = 20
        self.player_y = 60
        
        #重力系変数
        self.gravity = 2.0
        self.MAX_GRAVITY = self.gravity
        self.POWER = 0.25
 
        #爆弾の生成用
        self.bomb = [(i * 60, randint(0, 104)) for i in range(3,15)]

        #ポイントの生成用
        self.point= [(i * 60, randint(0, 104)) for i in range(3,15)]
 
        #遠い雲
        self.far_cloud = [(10, 25), (70, 35), (120, 15), (44, 45), (67, 75), (110, 95)]
 
 
        #音再生
        pyxel.playm(0, loop=True)
 
        pyxel.run(self.update, self.draw)
 
    def update(self):
 
        #終了する
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
 
        
        #スペース押された場合
        if pyxel.btn(pyxel.KEY_SPACE) :
            self.START = True
 
        if self.GAMEOVER and (pyxel.btn(pyxel.KEY_LEFT)) :
            self.reset()
 
 
        if not self.START or self.GAMEOVER:
            return
 
        #プレイヤーの更新
        self.update_player()
 
        #爆弾の表示
        for i, v in enumerate(self.bomb):
            self.bomb[i] = self.update_bomb(*v)

        for i,v in enumerate(self.point):
            self.point[i]=self.update_point(*v)
 
        # スコア
        # if not self.GAMEOVER:
        #     self.score += 1
        
 
 
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0,0,1,0,0,160,120,0)
        if self.GAMEOVER:
         pyxel.text(70,54,'score:'+str(self.score),2)
 
            MESSAGE =\
"""
     GAMEOVER

 
PUSH LEFT RESTART
"""
            pyxel.text(51, 40, MESSAGE, 2)
            pyxel.text(50, 40, MESSAGE, 7)
            return
 

        #キャラクタ表示
        if not self.GAMEOVER:
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 32, 0)
 
        # 爆弾表示
        for x, y in self.bomb:
            pyxel.blt(x, y, 0, 48, 0, 16, 16, 0)
        
        #ポイント表示
        for x,y in self.point:
            pyxel.blt(x,y,0,16,0,16,16,0)
 
 

 
        #スコア表示
        s = "SCORE {:>4}".format(self.score)
        pyxel.text(5, 4, s, 2)
        pyxel.text(4, 4, s, 7)
 
        if not self.START:
            MESSAGE ="PUSH SPACE KEY"
            pyxel.text(61, 50, MESSAGE, 2)
            pyxel.text(60, 50, MESSAGE, 7)
            return
 
    #プレイヤー更新関数
    def update_player(self):
 
        if pyxel.btn(pyxel.KEY_SPACE):
            if self.gravity > -self.MAX_GRAVITY:
                self.gravity = self.gravity - self.POWER
        else:
            if self.gravity < self.MAX_GRAVITY:
                self.gravity = self.gravity + self.POWER
 
        self.player_y = self.player_y + self.gravity 
 
        if( 0 > self.player_y ):
            self.player_y = 0
 
        if( self.player_y > pyxel.height -16 ):
            self.player_y = pyxel.height - 16
 
 
    #爆弾更新
    def update_bomb(self, x, y):
        if abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            self.GAMEOVER = True
            pyxel.blt(x, y, 0, 48, 0, 16, 16, 0)
            # pyxel.blt(self.player_x, self.player_y, 0, 16, 0, 16, 16, 0)
            
            pyxel.stop()
        x -= 2
 
        if x < -40:
            x += 240
            y = randint(0, 104)
 
        return (x, y)
    
    #ポイント更新
    def update_point(self,x,y):
        if abs(x-self.player_x)<12 and abs(y-self.player_y)<12:
            self.GAMEOVER=False
            self.score+=1
            pyxel.blt(x,y,0,8,0,16,16,0)

            pyxel.stop()
        x-=2

        if x<-40:
            x+=240
            y=randint(0,104)

        return (x,y)
 
    def reset(self):
        #STARTFLAG
        self.START = True
 
        #GAMEOVERフラグ
        self.GAMEOVER = False
 
        #スコア用変数
        self.score = 0
 
        #プレイヤー初期地位
        self.player_x = 20
        self.player_y = 60
        
        #重力系変数
        self.gravity = 2.5
        self.MAX_GRAVITY = self.gravity
        self.POWER = 0.25
 
        #爆弾の生成用
        self.bomb = [(i * 60, randint(0, 104)) for i in range(3,15)]

        self.point=[(i * 60, randint(0, 104)) for i in range(3,15)]
 
        #遠い雲
        self.far_cloud = [(10, 25), (70, 35), (120, 15), (44, 45), (67, 75), (110, 95)]
 
 
 
 
App()
