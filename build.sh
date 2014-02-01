#!/bin/sh

##################################################
# Usage: ./build.sh [-f] test/clean              #
#        -f will silently force following action #
##################################################

case "$1" in 
    "-f") FORCE=1; shift;;
esac

if [ "$1" = "clean" ]; then
    if [ "$FORCE" = 1 ]; then
	rm *.db
    else
	rm -i *.db
    fi
elif [ "$1" = "test" ]; then
    if [ "$FORCE" = 1 ]; then
	./build.sh -f clean
	python create_test_db.py
    else
	python create_test_db.py
    fi
else
    echo "Try passing either 'clean' or 'test' to the script."
fi
