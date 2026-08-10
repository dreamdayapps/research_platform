#!/bin/bash
#rm -f venv
python -m venv venv
source venv/bin/activate
pip cache purge
pip install -r requirements.txt
