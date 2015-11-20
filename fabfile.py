from fabric.api import *
from fabric.contrib.console import confirm
from fabric.decorators import task

ADMIN_USER = 'michael'
ADMIN_PASSWORD = 'password'
ADMIN_EMAIL = 'meshores1@gmail.com'

@task
def wordpress():

    """
    Install a local version of Wordpress in MAMP htdocs/.

    What it does:
        - Create a directory in htdocs/
        - Creates a MySQL database
        - Download Worpress to new directory
        - Config Wordpress in wp-config.php
        - Install the database
        - Clean plugins/ of Akismet
        - Remove default post, terms, and comments
    """

    print "ENTER SITE DETAILS:"
    dir_name = prompt('Enter htdoc/ folder name:', default='wordpress')
    db_name = prompt('Enter database name:')
    db_user = prompt('Enter database user:', default='michael')
    db_password = prompt('Enter database password:', default='password')
    wp_version = prompt('Wordpress version:', default='latest')

    blog_title = prompt('Blog Title:', default='Site Name')
    blog_description = prompt('Blog Description:', default='Just Another Wordpress Site')

    # Make the directory
    local('mkdir {0}'.format(dir_name))
    with lcd(dir_name):

        # Make MySQL database for MAMP
        # https://dev.mysql.com/doc/refman/5.0/en/connecting.html
        local('mysqladmin --user=michael --password=password create {0}'.format(db_name))

        # Download wordpress
        if wp_version != 'latest':
            local('wp core download --version={0}'.format(wp_version))
        else:
            local('wp core download')

        # Make wp-config.php
        wpcli = "wp core config --dbname={0} --dbuser={1} --dbpass={2}".format(db_name, db_user, db_password)
        local(wpcli)

        # Install WP database
        wpcli = 'wp core install --url=http://localhost/{0} --title="{1}" --admin_user={2} \
                --admin_password={3} --admin_email={4}'.format(dir_name, blog_title,
                                            ADMIN_USER, ADMIN_PASSWORD, ADMIN_EMAIL)
        local(wpcli)

        # TODO: add "define('WP_DEBUG', false);" to generated config file


        # Change description
        local("wp option update blogdescription '{0}'".format(blog_description))

        # Cleanup install for my preferences
        local("wp option update permalink_structure '/%postname%/'") # set permalink structure
        local("wp site empty --yes") # remove default posts, terms, comments

        # Clean plugins/ folder
        local("rm wp-content/plugins/hello.php")
        local("rm -rf wp-content/plugins/akismet/")

    # Clone htdocs/_themes to new wp-content/themes/ folder
    local("rsync -a --exclude 'READEME.md' _themes/ {0}/wp-content/themes/".format(dir_name))

    # Clone htdocs/_wpplugins to new wp-content/plugins/ folder
    local("rsync -a --exclude 'READEME.md' _wpplugins/ {0}/wp-content/plugins/".format(dir_name))

    # Open site in Chrome
    local('open http://localhost/{0}/'.format(dir_name))