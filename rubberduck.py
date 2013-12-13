import os
import imp

class PlugRegister(object):
    '''
    A generic store for "things".

    A thing has one or more tags, and can have multiple metadata (whose
    meaning is application-specific).
    '''
    def __init__(self):
        # each object in the list is a dict wit fields:
        #   "tags": [list,of,tags]
        #   "plug": the thing itself
        #   "metadata": a dict with extra data
        # plug itself
        self.plugins = []

    def add(self, thing, tags, metadata={}):
        self.plugins.append({ 'plug': thing,
            'tags': tags,
            'metadata': metadata
            })

    def get_by_tag(self, tag):
        return (p['plug'] for p in self.plugins if tag in p['tags'])

plugins = PlugRegister()

def plug_register(tags, thing, metadata={}):
    global plugins
    print 'adding to', plugins
    plugins.add(thing, tags, metadata)

def scan_dir(to_load, d):
    for candidate in to_load:
        path = os.path.join(d, candidate + '.py')
        if os.path.exists(path):
            yield (candidate, path)


def load_plugins(want_to_load, dirs):
    """
    want_to_load is a list of strings with the name of the plugins that we
        want to load
    dirs is a list of strings: each one is the name of a directory
    """
    for name in want_to_load:
        try:
            fd, pathname, description = imp.find_module(name, dirs)
            print "loaded " + pathname
            mod = imp.load_source(name, pathname)
        except Exception as exc:
            from traceback import print_exc
            print "Error while loading:", exc
            print_exc()
