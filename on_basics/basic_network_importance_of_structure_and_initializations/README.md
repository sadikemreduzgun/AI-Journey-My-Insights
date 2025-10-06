# Here is a basic experiment on a basic neural network with 1 neuron no hidden layer, 1 neuron in hidden layer 1 neuron in output layer, 4 neurons in hidden layer and 1 in output layer and with different weight initializations and using different activation functions(reLU[activation='relu'] and linear[activation=None]) and comparing them.
# ❗ You will be amazed to see the results. The neural network can't even learn f(x)=x in some cases ❗❗❗
# my comment here:
### *"So some weight initializations lead to best gradiant some leads to local minima i guess"*
# Role of weight initialization
* Neural networks are sensitive to starting weights, especially with ReLU activations.
* Some initial weights:

  * Activate neurons well for all parts of the input → gradients flow → fast convergence → good predictions.

  * Activate neurons poorly for some inputs (dead ReLUs) → gradients are small or zero → slow convergence or stuck in a local minimum → bad predictions.


RandomUniform between -1 and 1 gives a wide range of starting points.

* Depending on how many neurons are “active” for early batches, Adam sees good or bad gradients:
  * Run 1 → mostly good initial activations → predictions reasonable
  * Run 3 → unlucky initialization → some neurons mostly dead → predictions terrible

# Related Concepts
* Dead neurons problem (ReLU): if pre-activation ≤ 0, output = 0, gradient = 0
* Local minima / saddle points: bad initializations can push optimization toward flat or suboptimal regions
* Variance of initialization matters: too high → exploding activations, too low → vanishing activations


### ❗Shuffle training data → ensures all neurons get diverse gradients early was a solution but it ultimately didn't work out can you understand why? 
### I guess Problem: Bad initial weights kill ReLU neurons before training even starts but IDK maybe u understand. 
### ❗ When initialization was sucks, even increasing epoch to 1000 didn't work out. So epochs ≠ fix when initialization already ruins gradient flow.
