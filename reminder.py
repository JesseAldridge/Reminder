import time, os, sys

meta_path = os.path.expanduser('~/reminder.txt')

if os.path.exists(meta_path):
  sys.exit()
else:
  with open(meta_path, 'w') as f:
    pass

  try:
    while True:
      print "don't fuck up"
      time.sleep(60 * 60)
  finally:
    os.remove(meta_path)
