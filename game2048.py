#!/usr/bin/python
#It is the game 2048, to try to writhe a program.

import numpy as np
import pandas as pd

class game:
    def add(self):
        #print('it is add')
        x=np.random.randint(low=0,high=4)
        y=np.random.randint(low=0,high=4)
        while self.table.xs(x)[y]!=0:
            x=np.random.randint(low=0,high=4)
            y=np.random.randint(low=0,high=4)
        self.table.xs(x)[y]=2*np.random.randint(low=1,high=3)

    def change(self, r):
        for j in range(2,-1,-1):
            if r[j]==0:
                for k in range(j,3):
                    r[k]=r[k+1]
                r[3]=0
        for j in range(3):
            if r[j]==r[j+1]:
                r[j]*=2
                for k in range(j+1,3):
                    r[k]=r[k+1]
                r[3]=0
        return r
    
    def sequence(self, r):
        a=r[0]
        r[0]=r[3]
        r[3]=a
        a=r[1]
        r[1]=r[2]
        r[2]=a
        return r

    def nextstep(self,s):
        if s=='w':
            #print('w')
            for i in range(4):
                aa=self.table[i]
                self.table[i]=game.change(self,aa)
        elif s=='s':
            #print('s')
            for i in range(4):
                aa=self.table[i]
                aa=game.sequence(self,aa)
                self.table[i]=game.sequence(self, game.change(self,aa))
        elif s=='a':
            #print('a')
            for i in range(4):
                aa=self.table.xs(i)
                self.table.xs(i)[0,1,2,3]=game.change(self,aa)
        elif s=='d':
            #print('d')
            for i in range(4):
                aa=self.table.xs(i)
                aa=game.sequence(self,aa)
                self.table.xs(i)[0,1,2,3]=game.sequence(self, game.change(self,aa))
        else:
            #print('else')
            print('You can choose from w, a, s, d buttons!')

    def win(self):
        for i in range(4):
            for j in range(4):
                #print(self.table[i][j])
                if self.table[i][j]==2048:
                    print(self.table)
                    print('You win!')
                    return 'true'
        return 'false'

    def lose(self):
        Table=pd.DataFrame([[0]*4]*4, columns=[0, 1, 2, 3])
        for i in range(4):
            for j in range(4):
                Table[i][j]=self.table[i][j]
        b='false'
        for i in ['w','s','a','d']:
            game.nextstep(self, i)
            for n in range(4):
                for m in range(4):
                    if Table[n][m]!=self.table[n][m]:
                        b='true'
        for i in range(4):
            for j in range(4):
                self.table[i][j]=Table[i][j]
        if b=='true':
            return 'false'
        print(self.table)
        print('You lose. Try again!')
        return 'true'

    def __init__(self):
        self.table=pd.DataFrame([[0]*4]*4, columns=[0, 1, 2, 3])
        game.add(self)
        game.add(self)
        #e=pd.Series([5,6,7,8])
        #self.table.xs(1)[3,2,1,0]=e
        #self.table[1][0,1,2,3]=e
        while 'true':
            print(self.table)
            s=input('Write the next step: ')
            if s=='exit':
                break
            #Table=[[0]*4]*4
            #Table=self.table
            Table=pd.DataFrame([[0]*4]*4, columns=[0, 1, 2, 3])
            same='true'
            for i in range(4):
                for j in range(4):
                    Table[i][j]=self.table[i][j]
            game.nextstep(self,s)
            for n in range(4):
                for m in range(4):
                    if Table[n][m]!=self.table[n][m]:
                        same='false'
            #b='false'
            #for i in range(4):
            #    for j in range(4):
            #        if self.table.astype('bool')[i][j]!=Table.astype('bool')[i][j]:
            #            b='true'
            #print(b)
            #if b=='true':
            if same=='false':
                game.add(self)
            #self.table[0][0]=2048
            if game.win(self)=='true':
                break
            if game.lose(self)=='true':
                break
        #r=self.table[0]
        #r=self.table.xs(1)#[0,1,2,3]
        #print(r.index)
        #for i in range(2,-1,-1):
        #    print(i)
        #print(r[3])
        #r=r.reindex(index=['a','b','c','d'])
        #print(r.index)
        #print(r)
        #print(r[3])



print('')
G=game()
