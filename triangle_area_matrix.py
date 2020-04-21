import sys
# (x, y)

if not len(sys.argv) == 7:
    print("You must provide the Xs and Ys of each point like this")
    print("python3 triangle_area_matrix.py 0 1 1 0 1 1")
else:
    A = (float(sys.argv[1]), float(sys.argv[2]))
    B = (float(sys.argv[3]), float(sys.argv[4]))
    C = (float(sys.argv[5]), float(sys.argv[6]))

    l1 = (B[0]-A[0], B[1]-A[1])
    l2 = (C[0]-A[0], C[1]-A[1])

    det = l1[0]*l2[1] - (l1[1]*l2[0])
    if det < 0:
        #There is no negative area, LOL
        det = det*-1

    print('The area of your triangle is : ', det*0.5)