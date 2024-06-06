import math
import numpy as np
#a ,d ,alpha, theta
matrix=[[0      ,0.333      ,-math.pi/2     ,math.pi/2], #row one of HD matrix - transformation from position 0 to 1
        [0      ,0          ,math.pi/2      ,-math.pi/2],
        [0.0825 ,0.3173     ,math.pi/2      ,3*math.pi/2],
        [-0.0825,0          ,-math.pi/2     ,-math.pi],
        [0      ,0.28195    ,math.pi/2      ,math.pi/6],
        [0.08724,0          ,math.pi/2      ,math.pi/4],
        [0      ,0.1171     ,0              ,math.pi/2],
        [0      ,0.1034     ,0              ,0]
]
#starting position
dh=[[1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
    ]

#calculat one transformation matrix
def DH_from_params(a,d,alpha,theta):
    ret=[[math.cos(theta),-math.cos(alpha)*math.sin(theta),math.sin(alpha)*math.sin(theta),a*math.cos(theta)],
         [math.sin(theta), math.cos(alpha)*math.cos(theta),-math.sin(alpha)*math.cos(theta),a*math.sin(theta)],
         [0,math.sin(alpha),math.cos(alpha),d],
         [0,0,0,1]
         ]
    return ret
print(dh)
for a,d,alpha,theta in matrix:
    dh=np.matmul(dh,DH_from_params(a,d,alpha,theta))
    print(dh)