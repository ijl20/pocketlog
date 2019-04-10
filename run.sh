#!/bin/bash

ssh tfc_prod@smartcambridge.org /home/tfc_prod/pocketlog.sh

sftp tfc_prod@smartcambridge.org:/home/tfc_prod/pocket.log pocket.log

