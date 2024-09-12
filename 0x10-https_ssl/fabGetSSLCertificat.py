#!/usr/bin/python3
"""Get a SSL termination certificate from a remote loadbalancer machine to local machine"""
from fabric.api import env, get
env.user = 'ubuntu'
env.hosts = ['100.26.241.9']

def download_cert():
    res = get('/etc/haproxy/haproxy.cfg', '~/alx-system_engineering-devops/0x10-https_ssl/')
    print(res.succeeded)
    
