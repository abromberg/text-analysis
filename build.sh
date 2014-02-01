#!/bin/sh

if [ "$1" = "clean" ]; then
    rm *.db
else
    python create_test_db.py
fi
