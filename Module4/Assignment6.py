import random
ACC = 100 #Accuracy
N = input()
n = 0
i = 0
while i < int(N):
    x = random.randint(0, int(ACC)) / int(ACC)
    y = random.randint(0, int(ACC)) / int(ACC)
    if x*x+y*y<1:
        n+=1
    i+=1
print("Approximation of pi: " + str(4*int(n)/int(N)))