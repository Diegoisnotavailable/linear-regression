import numpy as np
import matplotlib.pyplot as plt


def init_parameters(lista):
    size=len(lista)+1
    y=np.random.randint(1,5,size)
    return y

def predict(parameters,x):
    y=[]
    for index in range(len(x[0])):
        r=parameters[len(x)]
        for values in range(len(x)):
            r=r+x[values][index]*parameters[values]
            #print(x[values][index],parameters[values])
        y.append(r)
    return y


def mse(real_val,calc_val):
    r=0
    for i in range(len(real_val)):
        r=r+(real_val[i]-calc_val[i])**2
    return r/len(real_val)

def local_search(index,parameters):
    r=[]
    y=0
    for val in range(len(parameters)):
        if val==index:
            #simbol=-1**np.random.randint(6)
            y=np.random.randint(5000)/(np.random.randint(5000)+0.01)
            #y=y*simbol
        else:
            y=parameters[val]
        r.append(y)
    return r
        
        
        

def opt(parameters,x,y):
    best_parameters=parameters
    p1=predict(parameters,x)
    err1=mse(p1,y)
    for index in range(len(parameters)):
        new_parameters=local_search(index,parameters)
        p=predict(new_parameters,x)
        err=mse(p,y)
        if err<err1:
            best_parameters=new_parameters
            err1=err
    return best_parameters
        

        

def linear_reg(x,y):
    it=0
    parametros=init_parameters(x)
    p1=predict(parametros,x)
    error1=mse(p1,y)
    err=[]
    while error1>2 and it<5000:
        it=it+1
        parametros=opt(parametros,x,y)
        p1=predict(parametros,x)
        error1=mse(p1,y)
        print(error1)
        err.append(error1)
    x_plot=np.linspace(0,len(err),len(err))
    plt.plot(x_plot,err)
    plt.show()
    print(y,p1)
        
x=[[1,5,10,12],[3,9,6,7],[5,10,12,24]]#r2,r1,vin
def vout(r2,r1,vin):
    y=[]
    for i in range(len(r2)):
        y.append(vin[i]*(r2[i]/(r1[i]+r2[i])))
    return y
y=vout(x[0],x[1],x[2])
t1=linear_reg(x,y)

