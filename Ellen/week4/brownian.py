import distributions # make sure that thing to call is in the same directory as file that it is writing (ie brownian and distributions must be in same directory), only have to call the name and not the extension

import sys

import matplotlib.pyplot as plt #whenever you call the module matplotlib.pyplot, use plt as at the calling word (ie plt.plot)


class brownian: #wrap things like processes into classes, makes easier to run, normal and brownian class follow the same format, creating class brownian
    def __init__(self, start, rate): #need the starting place of the brownian motion and the rate at which it changes position
        self.start = start 
        self.rate = rate

    def run(self, ngen = 100):#something to do brownian motion, parameter of how many times to sample from brownian motion = 100. This is default, you could specify something different see below example
        res = [self.start] #container to put brownian motion in, will be organizing in discrete time, list of values that starts with self.start --> this is the first value
        cur_pos = self.start #current position, when you start is the starting position
        k = distributions.normal(0.0, self.rate) #creating k to be in the class normal, has the mean of 0.0 and the sd is the rate of movement
        #print(k)
        #sys.exit()
        for gen in range(ngen): #for loop going through range 0, ngen
            jump = k.random_ls(1)[0] #want one random number, returns list, must pull it out to be a float
            #print(jump)
            #sys.exit()
            #print(cur_pos)
            cur_pos = cur_pos +jump #changes the value of current position to add the jump
            #print(cur_pos)
            #sys.exit()
            res.append(cur_pos) #add this new value to the list that we initialized
        return res
    
#for i in range (1000): #New loop that is going through range 0,100
    #b = brownian(0, 1.0) #for each value of i define a brownian class b with start at 0 and a range of 1.0 that will become the sd in the the class normal that is applied in the function b.run below
    #path = b.run(100) #create a list of values (res from run function) which doe the brownian motion for this run i
    #plt.plot(range(len(path)), path) #plot the values of path for run i
#plt.show() #show plot that has run throug the above loop 100 times (or however many times you specify) ie there should be 100 lines

#print (path)


#Code created based on Euler's forward formula
class brownian_con:
    def __init__(self, start, rate):
        self.start = start
        self.rate = rate

    def run(self, ngen = 100, dt = 1):#something to do brownian motion, parameter of how many times to sample from brownian motion = 100. This is default, you could specify something different see below example
        res = [self.start] #container to put brownian motion in, will be organizing in discrete time, list of values that starts with self.start --> this is the first value
        cur_pos = self.start #current position, when you start is the starting position
        k = distributions.normal(0.0, self.rate) #creating k to be in the class normal, has the mean of 0.0 and the sd is the rate of movement
        t = 0
        timesteps = [t]
        #print(k)
        #sys.exit()
        for gen in range(ngen): #for loop going through range 0, ngen
            jump = (k.random_ls(1)[0]) #want one random number, returns list, must pull it out to be a float
            #print(jump)
            #sys.exit()
            #print(cur_pos)
            cur_pos = cur_pos +jump #changes the value of current position to add the jump
            t = t + dt
            #print(cur_pos)
            #sys.exit()
            res.append(cur_pos)#add this new value to the list that we initialized
            timesteps.append(t)
        return res, timesteps

    #def con_time(self, ngen = 100, dt = 1):
        #t = 0
        #timesteps = [t]
        #for gen in range(ngen):
            #t = t + dt
            #timesteps.append(t)
        #return timesteps

class brownian_con_2:
    def __init__(self, start, rate):
        self.start = start
        self.rate = rate

    def run(self, dt = 1.0, tmax = 50.0):#something to do brownian motion, parameter of how many times to sample from brownian motion = 100. This is default, you could specify something different see below example
        res = [self.start] #container to put brownian motion in, will be organizing in discrete time, list of values that starts with self.start --> this is the first value
        cur_pos = self.start #current position, when you start is the starting position
        k = distributions.normal(0.0, self.rate) #creating k to be in the class normal, has the mean of 0.0 and the sd is the rate of movement
        t = 0
        timesteps = [t]
        #print(k)
        #sys.exit()
        while True:
            if t >= tmax:
                break
            jump = (k.random_ls(1)[0]) #want one random number, returns list, must pull it out to be a float
            #print(jump)
            #sys.exit
            #print(cur_pos)
            cur_pos = cur_pos +jump #changes the value of current position to add the jump
            t = t + dt
            #print(cur_pos)
            #print(t)
            #print(tmax)
            #sys.exit()
            res.append(cur_pos)#add this new value to the list that we initialized
            timesteps.append(t)
            #print(res, timesteps)
            #sys.exit()
        return res, timesteps


##### NOTE. Make sure that what you include in the function brackets as default numbers are FLOATS. Otherwise the limiting phrase will not work probably (ie, it will go over by one interval)


#b = brownian_con(0, 1.0)
#path, time = b.run(1000, 0.001)
#plt.plot(time, path)
#plt.show()

#b = brownian(0, 1.0) #for each value of i define a brownian class b with start at 0 and a range of 1.0 that will become the sd in the the class normal that is applied in the function b.run below
#path = b.run(100) #create a list of values (res from run function) which doe the brownian motion for this run i
#plt.plot(range(len(path)), path) #plot the values of path for run i
#plt.show()

#b = brownian_con_2(0, 1.0)
#path, time = b.run(0.00001, 100)
#plt.plot(time, path)
#plt.show()

class brownian_xy: #wrap things like processes into classes, makes easier to run, normal and brownian class follow the same format, creating class brownian
    def __init__(self, start, rate): #need the starting place of the brownian motion and the rate at which it changes position
        self.start = start 
        self.rate = rate

    def run(self, ngen = 100):#something to do brownian motion, parameter of how many times to sample from brownian motion = 100. This is default, you could specify something different see below example
        x_res = [self.start] #container to put brownian motion in, will be organizing in discrete time, list of values that starts with self.start --> this is the first value
        y_res = [self.start]
        cur_pos_x = self.start #current position, when you start is the starting position
        cur_pos_y = self.start
        k = distributions.normal(0.0, self.rate) #creating k to be in the class normal, has the mean of 0.0 and the sd is the rate of movement
        #print(k)
        #sys.exit()
        for gen in range(ngen): #for loop going through range 0, ngen
            jump_x = k.random_ls(1)[0] #want one random number, returns list, must pull it out to be a float
            jump_y = k.random_ls(1)[0]
            #print(jump)
            #sys.exit()
            #print(cur_pos)
            cur_pos_x = cur_pos_x +jump_x #changes the value of current position to add the jump
            cur_pos_y = cur_pos_y +jump_y
            #print(cur_pos)
            #sys.exit()
            x_res.append(cur_pos_x) #add this new value to the list that we initialized
            y_res.append(cur_pos_y)
        return x_res, y_res

#b = brownian_xy(0, 1.0)
#x, y = b.run(100)
#plt.plot(x, y)
#plt.show()

#for i in range (100): #New loop that is going through range 0,100
    #b = brownian_xy(0, 1.0) #for each value of i define a brownian class b with start at 0 and a range of 1.0 that will become the sd in the the class normal that is applied in the function b.run below
    #x, y = b.run(100) #create a list of values (res from run function) which doe the brownian motion for this run i
    #plt.plot(x, y) #plot the values of path for run i
#plt.show() #show plot that has run throug the above loop 100 times (or however many times you specify) ie there should be 100 lines




class brownian_con_xy:
    def __init__(self, start, rate):
        self.start = start
        self.rate = rate

    def run(self, dt = 1.0, tmax = 50.0):#something to do brownian motion, parameter of how many times to sample from brownian motion = 100. This is default, you could specify something different see below example
        x_res = [self.start] #container to put brownian motion in, will be organizing in discrete time, list of values that starts with self.start --> this is the first value
        y_res = [self.start]
        cur_pos_x = self.start #current position, when you start is the starting position
        cur_pos_y = self.start
        k = distributions.normal(0.0, self.rate) #creating k to be in the class normal, has the mean of 0.0 and the sd is the rate of movement
        t = 0
        timesteps = [t]
        #print(k)
        #sys.exit()
        while True:
            if t >= tmax:
                break
            jump_x = k.random_ls(1)[0] #want one random number, returns list, must pull it out to be a float
            jump_y = k.random_ls(1)[0] #want one random number, returns list, must pull it out to be a float
            #print(jump)
            #sys.exit
            #print(cur_pos)
            cur_pos_x = cur_pos_x +jump_x #changes the value of current position to add the jump
            cur_pos_y = cur_pos_y +jump_y
            t = t + dt
            #print(cur_pos)
            #print(t)
            #print(tmax)
            #sys.exit()
            x_res.append(cur_pos_x) #add this new value to the list that we initialized
            y_res.append(cur_pos_y)
            timesteps.append(t)
            #print(res, timesteps)
            #sys.exit()
        return x_res, y_res, timesteps

#b = brownian_con_xy(0, 1.0)
#x, y, time = b.run(1.0, 10.0)
#plt.plot(x, y, time)
#plt.show()

#fig = plt.figure()
#ax = plt.axes(projection="3D")
#ax.scatter3D(x, y, time, 'gray')
#plt.show()

class brownian_xy_2: #wrap things like processes into classes, makes easier to run, normal and brownian class follow the same format, creating class brownian
    def __init__(self, start_x, rate_x, start_y, rate_y): #need the starting place of the brownian motion and the rate at which it changes position
        self.start_x = start_x 
        self.rate_x = rate_x
        self.start_y = start_y 
        self.rate_y = rate_y

    def run(self, ngen = 100):#something to do brownian motion, parameter of how many times to sample from brownian motion = 100. This is default, you could specify something different see below example
        x_res = [self.start_x] #container to put brownian motion in, will be organizing in discrete time, list of values that starts with self.start --> this is the first value
        y_res = [self.start_y]
        cur_pos_x = self.start_x #current position, when you start is the starting position
        cur_pos_y = self.start_y
        k_x = distributions.normal(0.0, self.rate_x) #creating k to be in the class normal, has the mean of 0.0 and the sd is the rate of movement
        k_y = distributions.normal(0.0, self.rate_y)
        #print(k)
        #sys.exit()
        for gen in range(ngen): #for loop going through range 0, ngen
            jump_x = k_x.random_ls(1)[0] #want one random number, returns list, must pull it out to be a float
            jump_y = k_y.random_ls(1)[0]
            #print(jump)
            #sys.exit()
            #print(cur_pos)
            cur_pos_x = cur_pos_x +jump_x #changes the value of current position to add the jump
            cur_pos_y = cur_pos_y +jump_y
            #print(cur_pos)
            #sys.exit()
            x_res.append(cur_pos_x) #add this new value to the list that we initialized
            y_res.append(cur_pos_y)
        return x_res, y_res

#b = brownian_xy_2(0.0, 1.0, 2.0, 2.0)
#x, y = b.run(100)
#plt.plot(x, y)
#plt.show()

for i in range (100): #New loop that is going through range 0,100
    b = brownian_xy_2(0, 1.0, 50, 5.0) #for each value of i define a brownian class b with start at 0 and a range of 1.0 that will become the sd in the the class normal that is applied in the function b.run below
    x, y = b.run(100) #create a list of values (res from run function) which doe the brownian motion for this run i
    plt.plot(x, y) #plot the values of path for run i
plt.show()
        
