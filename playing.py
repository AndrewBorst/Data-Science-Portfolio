# %%
msg = "Hello World"
print(msg)

# %%
from matplotlib.pyplot import imshow, show, gray
# from pylab import show,gray
from numpy import zeros,linspace

xmin = 0.250
xmax = 0.260
ymin = -0.025
ymax = 0.025

n=1000

M = zeros([n,n],int)
xvalues = linspace(xmin,xmax,n)
yvalues = linspace(ymin,ymax,n)

for u,x in enumerate(xvalues):
    for v,y in enumerate(yvalues):
        z = 0 + 0j
        c = complex(x,y)
        for i in range(100):
            z = z*z + c
            if abs(z) > 2.0:
                M[v,u] = 1
                break

imshow(M,origin="lower")
gray()
show()

# %%
