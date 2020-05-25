from generator import randomstatsgenerator as rsg

if __name__=='__main__':
    print("You are running main.")
    # rsg.linear((0,100), coef=2, noise=2)
    rsg.quadratic((-10,10), coef=[2,0], noise=2)

