@echo off
git add .
git reset test.log
git reset __pycache__
git commit -m "first commit"
git push -u origin main

@REM echo "# Stocktool" >> README.md
@REM git init
@REM git add README.md
@REM git commit -m "first commit"
@REM git branch -M main
@REM git remote add origin https://github.com/rrobciorr/Stocktool.git
@REM git push -u origin main