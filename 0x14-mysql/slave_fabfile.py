#!/usr/bin/env python3
"""Download the master SQL configuration from remote host"""
from fabric.api import get, env
env.user = 'ubuntu'
env.hosts = ['34.227.101.79']

def slave_cnf():
    result = get('/etc/mysql/mysql.conf.d/mysqld.cnf', './4-mysql_configuration_replica')
    print(result.succeeded)
