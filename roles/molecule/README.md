molecule
=========

Install ansible molecule with docker and vagrant drivers support into python virtual env.

Requirements
------------

Debian OS, python3 virtual env with ansible in it.

Role Variables
--------------

- ```user```             User which installation is for, default: ansible
- ```home```             User home dir, default: lookup('env', 'HOME')
- ```venv_dir```         Directory under $HOME which holds python virtual envs, default: .virtualenvs
- ```venv_dir```         Python virtual env where molecule is to be installed, default: ansible
- ```os_prerequisites``` OS prerequisites, default [ansible-doc,libssl-dev,python3-venv]
- ```py_prerequisites``` Python prerequisites, default [molecule[docker,lint],molecule-vagrant,pytest,python-vagrant]

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: o.molecule, user: rico }

To Test
-------

*requires docker, ansible, molecule[docker,lint]*

```(ansible) $ mol test```

License
-------

MIT

Author Information
------------------

o-le-g@inbox.ru
