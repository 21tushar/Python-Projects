import sys

sys.stderr.write('This is strderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

print(sys.argv)