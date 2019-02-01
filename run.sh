#!/bin/bash

ssh tfc_prod@tfc-app1.cl.cam.ac.uk /home/tfc_prod/pocketlog.sh

sftp tfc_prod@tfc-app1.cl.cam.ac.uk:/home/tfc_prod/pocket.log pocket.log

