# Fabric Wordpress Env

Launch a new Wordpress development area in 45sec with Fabric + Wordpress CLI.

## Requirements

* Python 2.7
* [Fabric](http://fabric.readthedocs.org/) 1.8.0 (may work in older versions as well)
* [WP-CLI, Wordpress Command Line Interface](http://wp-cli.org/)

### Configuration

Currently configured with MAMP and uses `mysqladmin` bash command.

### Running the Script

1. Make sure PHP server is running via MAMP
2. `cd path/to/mamp/htdocs/`
3. `fab wordpress`
4. Follow prompts…

## TODO

1. Add boilerplate configuration file to hold the prompt configurations like *Blog Title*, *Database Name*, etc.