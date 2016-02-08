#!/bin/sh
git add *
echo "OK 1-3"
git commit -a -m 'добавил'
echo "OK 2-3"
git push
echo "OK 3-3"
exit