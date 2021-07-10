class NeuralNet :

    iNodes =0 #No. of input nodes
    hNodes =0 #No. of hidden nodes
    oNodes =0#No. of output nodes

    whi = []#matrix containing weights between the input nodes and the hidden nodes
    whh = []#matrix containing weights between the hidden nodes and the second layer hidden nodes
    woh = []#matrix containing weights between the second hidden layer nodes and the output nodes
#---------------------------------------------------------------------------------------------------------------------------------------------------------

    #constructor
    def __init__(inputs, hiddenNo, outputNo):
        #set dimensions from parameters
        iNodes = inputs
        oNodes = outputNo
        hNodes = hiddenNo

        #create first layer weights
        #included bias weight
        whi = Matrix(hNodes, iNodes +1);

        #create second layer weights
        #include bias weight
        whh = Matrix(hNodes, hNodes +1);

        #create second layer weights
        #include bias weight
        woh = Matrix(oNodes, hNodes +1);

        #set the matricies to random values
        whi.randomize();
        whh.randomize();
        woh.randomize();

    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    #mutation function for genetic algorithm
    def mutate(mr):
        #mutates each weight matrix
        whi.mutate(mr);
        whh.mutate(mr);
        woh.mutate(mr);


#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #calculate the output values by feeding forward through the neural network
    def output(inputsArr):

        #convert array to matrix
        #Note woh has nothing to do with it its just a function in the Matrix class
        inputs = woh.singleColumnMatrixFromArray(inputsArr);

        #add bias
        inputsBias = inputs.addBias();

        #-----------------------calculate the guessed output
        #apply layer one weights to the inputs
        hiddenInputs = whi.dot(inputsBias);

        #pass through activation function(sigmoid)
        hiddenOutputs = hiddenInputs.activate();

        #add bias
        hiddenOutputsBias = hiddenOutputs.addBias();

        #apply layer two weights
        hiddenInputs2 = whh.dot(hiddenOutputsBias);
        hiddenOutputs2 = hiddenInputs2.activate();
        hiddenOutputsBias2 = hiddenOutputs2.addBias();

        #apply level three weights
        outputInputs = woh.dot(hiddenOutputsBias2);
        #pass through activation function(sigmoid)
        outputs = outputInputs.activate();

        #convert to an array and return
        return outputs.toArray();

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #crossover function for genetic algorithm
    def crossover(partner) :

        #creates a new child with layer matrices from both parents
        child = NeuralNet(iNodes, hNodes, oNodes)
        child.whi = whi.crossover(partner.whi);
        child.whh = whh.crossover(partner.whh);
        child.woh = woh.crossover(partner.woh);
        return child

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #return a neural net which is a clone of this Neural net
    def clone():
        clone  = NeuralNet(iNodes, hNodes, oNodes)
        clone.whi = whi.clone();
        clone.whh = whh.clone();
        clone.woh = woh.clone();

        return clone;

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #converts the weights matrices to a single table
    #used for storing the snakes brain in a file
    def NetToTable():

        #create table
        t = Table();


        #convert the matricies to an array
        whiArr = whi.toArray();
        whhArr = whh.toArray();
        wohArr = woh.toArray();

        #set the amount of columns in the table
        for i in range(max([len(whiArr), len(whhArr), len(wohArr)])):
                t.addColumn();


        #set the first row as whi
        tr = t.addRow();

        for i in range(len(whiArr)):#(int i = 0; i< whiArr.length; i++) {
                tr.setFloat(i, whiArr[i]);



        #set the second row as whh
        tr = t.addRow();

        for i in range(len(whhArr)):#(int i = 0; i< whhArr.length; i++) {
                tr.setFloat(i, whhArr[i]);


        #set the third row as woh
        tr = t.addRow();

        for i in range(len(wohArr)):#(int i = 0; i< wohArr.length; i++) {
                tr.setFloat(i, wohArr[i]);


        #return table
        return t;


#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #takes in table as parameter and overwrites the matrices data for this neural network
    #used to load snakes from file
    def TableToNet(t) :

        #create arrays to tempurarily store the data for each matrix
        whiArr = np.zeros(whi.rows * whi.cols);
        whhArr = np.zeros(whh.rows * whh.cols);
        wohArr = np.zeros(woh.rows * woh.cols);

        #set the whi array as the first row of the table
        tr = t.getRow(0);

        for i in range(len(whiArr)):
            whiArr[i] = tr.getFloat(i);

        #set the whh array as the second row of the table
        tr = t.getRow(1);

        for i in range(len(whhArr)):#(int i = 0; i< whhArr.length; i++) {
            whhArr[i] = tr.getFloat(i);


        #set the woh array as the third row of the table

        tr = t.getRow(2);

        for i in range(len(wohArr)):
            wohArr[i] = tr.getFloat(i);



        #convert the arrays to matrices and set them as the layer matrices
        whi.fromArray(whiArr);
        whh.fromArray(whhArr);
        woh.fromArray(wohArr);
