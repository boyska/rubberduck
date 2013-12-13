from rubberduck import plug_register
print "Plugin %s imported" % __file__

def foo():
  '''evviva'''
  print "asd foo"

plug_register(['tag1', 'tag2'], foo)
