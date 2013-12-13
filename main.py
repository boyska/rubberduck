import rubberduck

rubberduck.load_plugins(['pl1', 'pl2'], ['plugins', 'otherplugs'])
print rubberduck.plugins.plugins

print 'tag1:', list(rubberduck.plugins.get_by_tag("tag1"))
print 'tag2:', list(rubberduck.plugins.get_by_tag("tag2"))
