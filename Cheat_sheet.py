# set up your ssh key (will go into C:\Users\username/.ssh/id_rsa.pub)
ssh-keygen

# copy files from your computer to the google server
# scp filename user@external_ip_address:  
# example:
scp cloud_setup_tutorial ahino@34.72.21.219:  

# copy files from the google server to your computer 
scp ahino@34.72.21.219:filename.txt .

#let your files run without stopping when you go to sleep and the terminal dies
nohup python multi_thread_problem.py &

# make a folder
mkdir foldername

# remove a folder and all its contents
rm -r results/

# move to a folder
cd foldername

# activate the python3 virtual enviroment
python3 -m venv venv
source venv/bin/activate

# open your session in jupyterlab
#1. install jupyterlab on cluster
pip install jupyterlab
#2. run jupyter lab without a browser and send to a port
jupyter notebook --no-browser --port=8080
#3. access and forward that port info to your local computer
ssh -L 8080:localhost:8080 ahino@34.72.21.219

# replace windows file format into unix format
sed -i -e 's/\r\+$//' cloud_setup_tutorial
# run the bash file
source cloud_setup_tutorial

# if you have some fingerprint type errors when using ssh --> you may need to clear your known hosts
rm ~/.ssh/known_hosts

# change the reading/writing/executing permissions for a file
chmod 777 program.exe

# delete files selectively 
find . -type f -name 'fileprefix_*' -delete

# see all running python commands
ps -ef | grep python

# kill all running python commands
pkill -f "python"

# check the space a certain folder is taking
df -h /home/ahino/results