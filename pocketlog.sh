#!/bin/bash

cd /home/tfc_prod

cat /var/log/tfc_prod/gunicorn.err | grep "|logger|pocket|" >pocket.log

