from threading import Thread
import time

class Threads(Thread):
    def __init__(self,tid,str):
        super().__init__()
        self.tid = tid
        self.str = str

    def run(self):
        print('Starting thread ',self.tid)
        if self.tid == 1:
            self.palin()
        else:
            self.vowel()
        print('Exiting thread ',self.tid)

    def palin(self):
        if self.str == self.str[::-1]:
            print('Palindrome')
        else:
            print('Not a Palindrome')

    def vowel(self):
        cnt = 0
        for i in self.str:
            if i.lower() in 'aeiou':
                cnt += 1
        print('No. of vowels : ',cnt)

t1 = Threads(1,'czechoslovakia')
t2 = Threads(0,'czechoslovakia')
t1.start()
t2.start()
t1.join()
t2.join()
