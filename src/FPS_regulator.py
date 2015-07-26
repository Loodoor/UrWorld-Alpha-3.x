__author__ = 'Moustillon'

import time


class IAFPS:
    def __init__(self, FPS):
        self.FPS = FPS / 10
        self.defaut_value = self.FPS
        self.reduction = 0.0005
        self.wait = 0.001
        self.cpt_tour = 0
        self.frame_rate = 0
        self.begin_time = time.time() + 0.1

    def actualise(self):
        if self.begin_time < time.time():
            self.cpt_tour = 0
            self.timer(self.cpt_tour)
        else:
            self.cpt_tour += 1

    def timer(self, frame_rate):
        self.frame_rate = frame_rate
        if self.frame_rate > self.FPS:
            self.wait += self.reduction
        elif self.frame_rate < self.FPS:
            self.wait -= self.reduction
            if self.wait <= 0:
                self.wait = 0
                #print("temps de pause (sec) :: " + str(self.wait))
                #print("frame_rate compté dans la boucle :: " + str(self.frame_rate))

    def pause(self):
        time.sleep(self.wait)

    def set_FPS(self, nv_FPS):
        self.FPS = nv_FPS / 10

    def default(self):
        self.FPS = self.defaut_value
