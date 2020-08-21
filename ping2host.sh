#!/bin/bash
if ping -c 1 192.168.1.1 &> /dev/null
then
  echo "The host is alive"
else
  python3 post_message.py
  echo "The host is dead"
fi
