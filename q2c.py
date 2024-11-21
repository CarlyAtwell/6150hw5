import numpy as np

def main():
    # run the experiments
    t= 16e4
    times_cross = np.zeros(50)
    for j in range(50):
        x = 0
        x_prev = x
        for i in range(int(t)):
            move = np.random.choice([-1,1])
            #print("move: "+ str(move))
            x_new = x + move
            #print("x: "+ str(x))
            #print("x_new: "+ str(x_new))
            #if(x < 0):
                #print("negative")
                #print(x)
            if (abs(x_new) + abs(x_prev) != abs(x_new+x_prev)):
                times_cross[j]+=1
            x_prev = x
            x = x_new
        #print(times_cross[j])
    avg_times_cross = times_cross.mean()
    print(avg_times_cross)
    

if __name__ == "__main__":
    main()