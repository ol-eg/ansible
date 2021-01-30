apt_file
========

Install and configure apt-file.

Requirements
------------

Debian OS, ansible.

Role Variables
--------------

*defaults are in* ```./defaults/main.yml```

- ```package_name```

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
        - { role: apt_file }

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
