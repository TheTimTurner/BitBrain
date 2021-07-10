class Population:

    Snake[] snakes;#all the snakes in the population

    gen = 1;#which generation we are up to
    globalBest = 4;# the best score ever achieved by this population
    globalBestFitness = 0; # the best fitness ever achieved by this population
    currentBest = 4;#the current best score
    currentBestSnake = 0; #the position of the current best snake (highest score) in the array

    globalBestSnake; #a clone of the best snake this population has ever seen

    populationID = floor(random(10000)); # a random number to identify the population, used for saving snakes
#---------------------------------------------------------------------------------------------------------------------------------------------------------

    #used to help improve legends
    def __init__(size, best, *args):

        if (len(args) ==2):
            snakes = new Snake[size];

            #set all the snakes as mutated clones of the legend snake
            for i in range(len(snakes)):#(int i =0; i<snakes.length; i++):
                snakes[i] = best.clone();
                snakes[i].mutate(globalMutationRate);

            globalBestSnake = best.clone();

        elif (isinstance(size, int)):
            snakes = new Snake[size];
            #initiate all the snakes
            for i in range(len(snakes)):#(int i =0; i<snakes.length; i++):
                snakes[i] = new Snake();

            globalBestSnake = snakes[0].clone();

        #snake type
        else:
            snakes = new Snake[2000];

            #set all the snakes as  the legend snake
            for i in range(len(snakes)):#(int i =0; i<snakes.length; i++):
                snakes[i] = best.clone();
                snakes[i].test = true;

            #globalBestSnake = best.clone();

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #updates all the snakes in the population which are currently alive
    #void
    def updateAlive():
        for i in range(len(snakes)):#(int i =0; i<snakes.length; i++):
            if (snakes[i].alive):
                snakes[i].look(); #get inputs for brain
                snakes[i].setVelocity();  #get outputs from the neural net
                snakes[i].move(); #move the snake in the direction indicated by the neural net
                if (snakes[i].alive && (showAll || (i == currentBestSnake))):#if still alive show the snake
                    snakes[i].show();

        setCurrentBest(); #after updating every snake renew the best snake

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #test if all the snakes in this population are dead
    def done():
        for i in range(len(snakes)):#(int i =0; i<snakes.length; i++):
            if (snakes[i].alive):
                return false;

        return true;

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #calculates fitness of every snake
    #void
    def calcFitness() :
        for i in range(len(snakes)):#(int i =0; i<snakes.length; i++):
            snakes[i].calcFitness();



 #---------------------------------------------------------------------------------------------------------------------------------------------------------
    #creates the next generation of snakes by natural selection
    #void
    def naturalSelection() :

        newSnakes = Snake[snakes.length]; #next generation of snakes

        #set the first snake as the best snake without crossover or mutation
        setBestSnake();
        newSnakes[0] = globalBestSnake.clone();
        for i in range(len(newSnakes)):#(int i =0; i<newSnakes.length; i++):

            #select 2 parents based on fitness
            parent1 = selectSnake();
            parent2 = selectSnake();

            #crossover the 2 snakes to create the child
            child = parent1.crossover(parent2);
            #mutate the child (weird thing to type)
            child.mutate(globalMutationRate);
            #add the child to the next generation
            newSnakes[i] = child;

            #newSnakes[i] = selectSnake().clone().mutate(globalMutationRate); //uncomment this line to do natural selection without crossover

        snakes = newSnakes.clone();#set the current generation to the next generation


        gen+=1;
        currentBest = 4;
    }
#---------------------------------------------------------------------------------------------------------------------------------------------------------
  #chooses snake from the population to return randomly(considering fitness)
  Snake selectSnake() {
    #this function works by randomly choosing a value between 0 and the sum of all the fitnesses
    #then go through all the snakes and add their fitness to a running sum and if that sum is greater than the random value generated that snake is chosen
    #since snakes with a higher fitness function add more to the running sum then they have a higher chance of being chosen


    #calculate the sum of all the fitnesses
    long fitnessSum = 0;
    for (int i =0; i<snakes.length; i++) {
      fitnessSum += snakes[i].fitness;
    }


    //set random value
    long rand = floor(random(fitnessSum));

    //initialise the running sum
    long runningSum = 0;

    for (int i = 0; i< snakes.length; i++) {
      runningSum += snakes[i].fitness;
      if (runningSum > rand) {
        return snakes[i];
      }
    }
    //unreachable code to make the parser happy
    return snakes[0];
  }
//---------------------------------------------------------------------------------------------------------------------------------------------------------
  //sets the best snakes globally and for this gen
  void setBestSnake() {
    //calculate max fitness
    long max =0;
    int maxIndex = 0;
    for (int i =0; i<snakes.length; i++) {
      if (snakes[i].fitness > max) {
        max = snakes[i].fitness;
        maxIndex = i;
      }
    }
    //if best this gen is better than the global best then set the global best as the best this gen
    if(max > globalBestFitness){
      globalBestFitness = max;
      globalBestSnake = snakes[maxIndex].clone();
    }


  }

 //---------------------------------------------------------------------------------------------------------------------------------------------------------
  //mutates all the snakes
  void mutate() {
    for (int i =1; i<snakes.length; i++) {
      snakes[i].mutate(globalMutationRate);
    }
  }
//---------------------------------------------------------------------------------------------------------------------------------------------------------
  //sets the current best snake, used when just showing one snake at a time
  void setCurrentBest() {
    if (!done()) {//if any snakes alive
      float max =0;
      int maxIndex = 0;
      for (int i =0; i<snakes.length; i++) {
        if (snakes[i].alive && snakes[i].len > max) {
          max = snakes[i].len;
          maxIndex = i;
        }
      }

      if (max > currentBest) {
        currentBest = floor(max);
      }

      //if the best length is more than 1 greater than the 5 stored in currentBest snake then set it;
      //the + 5 is to stop the current best snake from jumping from snake to snake
      if (!snakes[currentBestSnake].alive || max > snakes[currentBestSnake].len +5   ) {

        currentBestSnake  = maxIndex;
      }


      if (currentBest > globalBest) {
        globalBest = currentBest;
      }
    }
  }
}
