def bubbleSort(x):

   xLen = len(x)

   for i in xrange(xLen-1):

       for j in xrange(xLen -1-i):

           if x[j] > x[j+1]:

                t = x[j]

                x[j] = x[j+1]

                x[j+1] = t

   return x

