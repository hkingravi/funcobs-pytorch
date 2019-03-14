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

The goal of this package is to strike a balance between reproducibility of research
and speed. Due to the former requirement, a lot of the code is written in-house,
even though better implementations probably exist somewhere else (see e.g. GPyTorch,
a recent package for efficient training of Gaussian processes). To 
achieve fast performance, we use a PyTorch backend where possible, which allows
for the use of GPUs where available. I recommend installing all dependencies using
conda.


# Setup

To get this repo, and to install all of the dependencies, run the following commands on OSX or Ubuntu.

```bash
git clone https://github.com/hkingravi/funcobs-pytorch.git  # clone repo (https)
cd funcobs-pytorch
conda create --name fobsp  # create conda env
conda activate fobsp  # activate virtual environment and install deps
while read requirement; do conda install --yes $requirement; done < requirements.txt  
python setup.py develop  #  install funcobspy in a development environment
```

Now, when you run your python code, you can always either activate the virtualenv via the command line
with the command 
```bash
conda activate fobsp
```
in the same directory as funcenv, or you can configure your Python IDE to use this interpreter. That
way, all the library requirements will be met. Generally, the conda env can be found in
```bash
~/anaconda3/envs/fobsp/bin/python3
```

In Python 3.x on Ubuntu, sometimes you will need to fix the Tkinter module, as follows:
```bash
sudo apt-get install python3-tk
```

If you want to use GPUs, make sure your CUDA drivers are installed! A quick check for this is 
to open an ipython terminal, and type
```python
import torch
print(torch.cuda.is_available())
```
If this is False, then you'll have to go through the install process for CUDA carefully. 

# References
* Hassan A. Kingravi, Harshal Maske, and Girish Chowdhary.
  [Kernel Observers: Systems-Theoretic Modeling and Inference of Spatiotemporally Evolving Processes](https://papers.nips.cc/paper/6189-kernel-observers-systems-theoretic-modeling-and-inference-of-spatiotemporally-evolving-processes.pdf),
   Advances in Neural Information Processing Systems 29 (NeurIPS 2016).
* Hassan A. Kingravi, Harshal Maske, and Girish Chowdhary.
  [A Systems-Theoretic Approach for Data-Driven Modeling and Control
    of Spatiotemporally Evolving Processes](http://hassanakingravi.com/papers/2015/CDC_2015.pdf),
   IEEE Conference on Decision and Control (2015).