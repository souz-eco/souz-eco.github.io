#! /usr/bin/python3


import os


os.system('hg add *')
os.system('hg commit')
os.system('hg push git+ssh://git@github.com:souz-eco/souz-eco.github.io.git')
print("All operations done.")
