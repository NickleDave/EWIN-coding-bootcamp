# EWIN-coding-bootcamp
Files for coding bootcamp sponsored by Emory Women In Neuroscience

We will be using Anaconda, an open platform for data science that makes it much easier to install scientific computing packages used with Python, R, and other open-source languages.

**Please install Anaconda with the current version of Python, 3.6**
* Windows: repo.continuum.io/archive/Anaconda3-4.3.0.1-Windows-x86_64.exe
* OSX (Mac): repo.continuum.io/archive/Anaconda3-4.3.0-MacOSX-x86_64.pkg
* Linux: repo.continuum.io/archive/Anaconda3-4.3.0-Linux-x86_64.sh

**If you already have Anaconda installed, you don't have to install a newer version. Just make sure you have a conda environment that uses some version of Python 3.**

Like so:

1. Open up an Anaconda terminal and type

`> conda create -n bootcamp python=3.5`

2. Then do

(Mac)
`> source activate bootcamp`

(Windows)
`> activate bootcamp`

3. lastly

`> conda install jupyter pandas numpy pip`

and say `y`es when it asks you about all the dependencies

To deactivate you just enter deactivate (for Windows) or source deactivate (for Mac)

You'll want to activate that conda environment again so you can use the Jupyter notebooks. To do so, you'll either go to the directory with the cloned repo in the terminal and enter '>jupyter notebook' or if Anaconda installed it for you, you can click the handy-dandy red icon under Anaconda in your programs (this might only work on Windows, sorry Mac people).
