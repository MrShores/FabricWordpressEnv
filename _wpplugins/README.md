# Fabric Wordpress Env

Add default plugins here.

Plugins in this folder will be copied to the new Wordpress dev area via `rsync`:

`local("rsync -a _wpplugins/ {0}/wp-content/plugins/".format(dir_name))`