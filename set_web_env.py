#!/usr/bin/env python3
import os

# Download mongodb
os.system('sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927')
os.system('echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list')
os.system('sudo apt-get update')
os.system('sudo apt-get install -y mongodb-org')

# Download pymongo
os.system('sudo pip install pymongo')

# Download Flask
os.system('sudo pip install Flask')