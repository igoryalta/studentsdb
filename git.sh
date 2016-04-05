#!/bin/sh
git status
echo "OK 1-4 status"
git add *
echo "OK 2-4 add"
git commit -a -m 'добавил'
echo "OK 3-4 commit"
git push
echo "OK 4-4 push"
exit