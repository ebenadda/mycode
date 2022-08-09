#!/bin/bash

#prompt for username and user group
echo "Please enter your name!"
read name

echo "What about your group!"
read group1

#go into the root and new add user
sudo useradd $name

#create group
sudo groupadd $group1

#add user to group
sudo usermod -aG $group1 $name
