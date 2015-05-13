import sys

all = ''
for arg in sys.argv[1:]:
    all += arg 

print 'that\'s all what they say: %s.' %all 
