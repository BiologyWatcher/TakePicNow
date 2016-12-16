#!/bin/bash
tmux new -d -s picnow1 'sudo python takepicnow.py'
tmux detach -s picnow1
