docker
=========

Install docker, default procedure as describe in https://docs.docker.com/engine/install/debian/

Requirements
------------

Debian OS, ansible user present.

Role Variables
--------------

- ```docker_users``` users to be added to docker group, default: [ansible]

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
         - { role: docker, docker_users: [ansible,mort] }

To Test
-------

requires:
- os packages: virtualbox, vagrant
- python packages: ansible, molecule-vagrant, python-vagrant

```(asible) $ mol test```

License
-------

MIT

Author Information
------------------

o-le-g@inbox.ru
