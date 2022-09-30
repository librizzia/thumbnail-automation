#!/bin/bash
echo "Moving file with app.py..."
python3 move.py
sleep 1
echo "Opening app.py..."
sleep 1
python3 app.py
sleep 1
echo "Opening website..."
sleep 3
firefox ./index.html </dev/null >/dev/null 2>&1 & disown ./index.html
