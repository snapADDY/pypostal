#!/bin/bash

cd addresses/libpostal && 
./bootstrap.sh && 
./configure && 
sudo make && 
sudo make install && 
sudo ldconfig && 
pkg-config --cflags libpostal && 
pkg-config --libs libpostal && 
pkg-config --cflags --libs libpostal
