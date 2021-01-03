import os
import sys
cwd = os.getcwd() 
installString = ''' apt-get update ; apt-get install gfortran libblas-dev liblapack-dev -y ; pip install cython ; python /root/shared/setup.py bdist_wheel '''

 
pythonVersions = ["3.7","3.9"]

for pyVersion in pythonVersions:
    os.system("docker run -itd --name numpy-builder -v {}:/root/shared python:{}-buster ".format(cwd,pyVersion))
    os.system('docker exec numpy-builder  bash -c "{}"'.format(installString))
    os.system("docker stop numpy-builder")
    os.system("docker rm numpy-builder")
