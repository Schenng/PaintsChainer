ls -v1 ../images/original/ | parallel -j 8  'echo {}; python resize.py -i {} -o ../images/color/{}'
ls -v1 ../images/original/  | parallel -j 8  'echo {}; python image2line.py -i {} -o ../images/line/{}'
ls -v1 ../images/original/  | parallel -j 8  'echo {}; python resizex2.py -i {} -o ../images/colorx2/{}'
ls -v1 ../images/original/  | parallel -j 8  'echo {}; python image2line.py -i {} -o ../images/linex2/{}'
