---
title:"about"
output:"html_document"
---
# Basic code for Git

## create a new repository on the command line
```console
echo "# test" >> README.md
git init
git add README.md (or git add . -> add all files that has been added or updated)
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/jhkoh17/python_basic
git push -u origin main
```
## push an existing repository from the command line
```console
git remote add origin https://github.com/jhkoh17/test.git
git branch -M main
git push -u origin main
```