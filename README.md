[![Build Status](https://travis-ci.org/thienngho/ansible-redis-roles.svg?branch=master)](https://travis-ci.org/thienngho/ansible-redis-roles)

Role Name
=========

Install redis server.

Requirements
------------

An install Ubuntu server.

Role Variables
--------------

Listen ip:port

    redis_port: 6379
    redis_address: 127.0.0.1

Connection timeout

    redis_timeout: 300

Logging

    redis_loglevel: "notice"
    redis_logfile: /var/log/redis/redis-server.log

Database count

    redis_databases: 16
  
Dependencies
------------

- Molecule
- Docker

Example Playbook
----------------

    - hosts: servers
      - import_role:
          name: redis
        vars:
            redis_address: "{{ hostvars[groups['redisservers'][0]]['ansible_default_ipv4']['address'] }}"

Test role with Molecule
```
molecule test
```
