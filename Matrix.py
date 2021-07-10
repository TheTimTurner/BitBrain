import numpy as np
import math
class Matrix:

    #local variables
    rows = 0
    cols = 0
    matrix = 0

    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    #constructor
    def __init__(r, c,*args) :
      #if rows and collumns are in the array
        if len(args) == 2:
            rows = r;
            cols = c;
            matrix = np.zeros(r,c);
        #constructor from 2D array
        if (len(args) == 1):
            matrix = np.array(m);
            cols = m.length;
            rows = m[0].length;
        else:
            print("Error, matrix type not supported")

    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    #print matrix
    def output() :
        for i in range(rows):#for (int i =0; i<rows; i++)
            for j in range(cols):#for (int j = 0; j<cols; j++) :
                print(matrix[i][j] + "  ", end=' ')
            print(" ")

    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    #multiply by scalar
    #void
    def multiply( n ) :
        matrix *= n

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #return a matrix which is this matrix dot product parameter matrix
    #n is a matrix
    def dot(n):
        return Matrix(np.dot(matrix,n))
#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #set the matrix to random ints between -1 and 1
    #void
    def randomize():
        matrix = p.random.uniform(low=-1, high=1, size=(row,cols))


#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #add a scalar to the matrix
    #void
    def Add( n ):
        matrix+=n

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #return a matrix which is this matrix + parameter matrix
    def add(n) :
        return Matrix(np.add(matrix,n))

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #return a matrix which is this matrix - parameter matrix
    def subtract(n):
        return Matrix(np.subtract(matrix,n))

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #return a matrix which is this matrix * parameter matrix (element wise multiplication)
    def multiply(n):
        return Matrix(np.multiply(matrix,n))

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#return a matrix which is the transpose of this matrix
    def transpose():
        return Matrix(matrix.transpose())

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#Creates a single column array from the parameter array
#return a matrix
    def singleColumnMatrixFromArray(arr):
        n = Matrix(len(arr), 1)
        for i in range(len(arr)):
            n.matrix[i][0] = arr[i]

        return n

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #sets this matrix from an array
    #void
    def fromArray(arr):
        for i in range(rows):#for (int i =0; i<rows; i++)
            for j in range(cols):#for (int j = 0; j<cols; j++) :
                matrix[i][j] =  arr[j+i*cols]



#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #returns an array which represents this matrix
    def toArray():
        arr = np.zeros(rows*cols)
        for i in range(rows):#for (int i =0; i<rows; i++)
            for j in range(cols):#for (int j = 0; j<cols; j++) :
                arr[j+i*cols] = matrix[i][j]
        return arr


#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #for ix1 matrixes adds one to the bottom
    def addBias():
        n = Matrix(rows+1, 1)
        for i in range(rows):#for (int i =0; i<rows; i++)
            n.matrix[i][0] = matrix[i][0];
        n.matrix[rows][0] = 1;
        return n

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #applies the activation function(sigmoid) to each element of the matrix
    def activate() :
        n = Matrix(rows, cols)
        for i in range(rows):#for (int i =0; i<rows; i++)
            for j in range(cols):#for (int j = 0; j<cols; j++) :
                n.matrix[i][j] = sigmoid(matrix[i][j])


        return n;


#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #sigmoid activation function
    def sigmoid(x) :
        y = 1 / (1 + pow(math.e, -x));
        return y

    #returns the matrix that is the derived sigmoid function of the current matrix
    def sigmoidDerived() :
        n = Matrix(rows, cols);
        for i in range(rows):#for (int i =0; i<rows; i++)
            for j in range(cols):#for (int j = 0; j<cols; j++) :
                n.matrix[i][j] = (matrix[i][j] * (1- matrix[i][j]))


        return n


#---------------------------------------------------------------------------------------------------------------------------------------------------------
  #returns the matrix which is this matrix with the bottom layer removed
    def removeBottomLayer() :
        n = Matrix(rows-1, cols)
        for i in range(rows):#for (int i =0; i<rows; i++)
            for j in range(cols):#for (int j = 0; j<cols; j++) :
                n.matrix[i][j] = matrix[i][j]


        return n

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #Mutation function for genetic algorithm
    #void
    def mutate(mutationRate):
        #for each element in the matrix
        for i in range(rows):#for (int i =0; i<rows; i++)
            for j in range(cols):#for (int j = 0; j<cols; j++) :
                rand = random.random()
                if (rand<mutationRate):#if chosen to be mutated
                    matrix[i][j] += randomGaussian()/5;#add a random value to it(can be negative)

                    #set the boundaries to 1 and -1
                    if (matrix[i][j]>1):
                        matrix[i][j] = 1;

                    if (matrix[i][j] <-1):
                        matrix[i][j] = -1;

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #returns a matrix which has a random number of values from this matrix and the rest from the parameter matrix
    def crossover(partner) :
        child = Matrix(rows, cols);

        #pick a random point in the matrix
        randC = random.randint(0,cols-1);
        randR = random.randint(0,rows-1);
        for i in range(rows):#for (int i =0; i<rows; i++)
            for j in range(cols):#for (int j = 0; j<cols; j++) :
                if ((i< randR) or (i==randR and j<=randC)): #if before the random point then copy from this matric
                    child.matrix[i][j] = matrix[i][j];
                else : #if after the random point then copy from the parameter array
                    child.matrix[i][j] = partner.matrix[i][j];

        return child;

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #return a copy of this matrix
    def clone() :
        clone = Matrix(rows, cols);
        for i in range(rows):#for (int i =0; i<rows; i++)
            for j in range(cols):#for (int j = 0; j<cols; j++) :
                clone.matrix[i][j] = matrix[i][j]


        return clone
