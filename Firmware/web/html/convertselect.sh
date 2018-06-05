#!/bin/sh
OUTDIR=out

mkdir -p $OUTDIR

./convert.sh  404.html    > $OUTDIR/o_404.html 
./convert.sh  index.html  > $OUTDIR/o_index.html
./convert.sh  overall.js  > $OUTDIR/o_overall.js
./convert.sh  styles.css  > $OUTDIR/o_styles.css
