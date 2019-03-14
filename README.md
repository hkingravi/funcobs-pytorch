# Function Observers
This is a Python toolbox for code pertaining to function observers.
The prototypical example of a functional observer is the
kernel observer and controller paradigm. The primary goal of these methods is the 
modeling and control of spatiotemporally varying processes (i.e. stochastic 
phenomena that vary over space AND time). Practical applications of these 
types of methods include ocean temperature modeling and monitoring, control 
of diffusive processes in power plants, optimal decision-making in contested 
areas with a patrolling enemy, disease propagation in urban population centers, 
and so on. This repository will add code where the generator for the function 
space will be generalized, and will include deep neural networks.

To achieve fast performance, we use a PyTorch backend where possible, which allows
for the use of GPUs where available.  


# Setup

To get this repo, and to install all of the dependencies, run the following commands on OSX or Ubuntu.

```bash
git clone git@github.com:hkingravi/funcobs-pytorch.git  # clone repo (ssh)
cd funcobspy
virtualenv -p python3 funcenv  # create virtual environment with all the of dependencies required
source funcenv/bin/activate  # activate virtual environment
pip install -U virtualenv  # upgrade virtualenv
pip install -U pip  # upgrade pip: these upgrades are to avoid weird bugs in some installs
chmod +x install_dependencies.sh  # make install script an executable
./install_dependencies.sh  # install all reqs using pip, fix matplotlib backend issue
python setup.py develop  #  install funcobspy in a development environment
```

Ensure that your Keras library is using the Theano backend by typing
```bash
nano ~/.keras/keras.json
```
and changing the "backend" field to "theano".

Now, when you run your python code, you can either activate the virtualenv via the command line
with the command 
```bash
source funcenv/bin/activate
```
in the same directory as funcenv, or you can configure your Python IDE to use this interpreter. That
way, all the library requirements will be met. If you want to roll your own version, just look at the
requirements.txt file. 

In Python 3.x on Ubuntu, sometimes you will need to fix the Tkinter module, as follows:
```bash
sudo apt-get install python3-tk
```


