ansible_modules
===============

Install prerequisites and set up environemtnt for ansible modules development.
https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html#prerequisites-via-apt-ubuntu

Requirements
------------

Debian OS, ansible.

Role Variables
--------------

- ```prerequisites```    OS packages, default: [build-essential,libssl-dev,libffi-dev,python3-dev,python3-setuptools,python3-setuptools-git]
- ```user```             Target user, default: ansible
- ```home```             Target user home dir, default: ```"{{ lookup('env', 'HOME') }}"```
- ```ansible_repo_dir``` Destination dir for official Ansible repo clone, default: ansible-dev

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
        - ansible_modules

To Test
-------

requires:
- os packages: docker
- python packages: ansible, molecule.

```(asible) $ mol test```

License
-------

MIT

Author Information
------------------

o-le-g@inbox.ru
