#!/usr/bin/env python3
"""Download the master SQL configuration from remote host"""
from fabric.api import get, env
env.user = 'ubuntu'
env.hosts = ['100.25.33.79']

def master_cnf():
    result = get('/etc/mysql/mysql.conf.d/mysqld.cnf', './4-mysql_configuration_primary')
    print(result.succeeded)
