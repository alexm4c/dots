#!/bin/bash

tmpbg='/tmp/screen.png'

(( $# ))

scrot "$tmpbg"
convert "$tmpbg" -scale 10% -scale 1000% "$tmpbg"
playerctl pause
i3lock -e -i "$tmpbg"
rm "$tmpbg"