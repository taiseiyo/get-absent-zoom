#!/bin/bash

scrot '%Y-%m-%d_$wx$h.png' -e 'mv $f ~/***'
env python3 get-absent.py
rm ~/*png
