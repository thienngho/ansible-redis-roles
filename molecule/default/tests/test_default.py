import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_redis_server_is_installed(host):
    redis = host.package('redis-server')

    assert redis.is_installed


def test_redis_is_running(host):
    redis = host.service('redis-server')

    assert redis.is_running
    assert redis.is_enabled


def test_redis_config_is_existed(host):
    redis = host.file("/etc/redis/redis.conf")
    assert redis.exists
