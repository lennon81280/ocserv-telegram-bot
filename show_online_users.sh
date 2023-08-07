#!/bin/bash

occtl show users | awk {'print $2'} | tail -n +2
echo "Online Count: " `occtl show users | awk {'print $2'} | tail -n +2 | wc -l`
