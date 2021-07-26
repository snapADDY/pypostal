#!/bin/bash

cd addresses/libpostal && 
./bootstrap.sh && 
./configure && 
make && 
make install && 
ldconfig && 
pkg-config --cflags libpostal && 
pkg-config --libs libpostal && 
pkg-config --cflags --libs libpostal
