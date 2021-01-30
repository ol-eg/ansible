dropbox
=======

Install dropbox GUI installer.

Requirements
------------

Debian OS, ansible.

Role Variables
--------------

*defaults are in* ```./defaults/main.yml```

- **prerequisites**:   os packages to be installed.
- **deb_name**:        name of the dropbox installer package.
- **dropbox_deb_url**: download url.

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
        - { role: dropbox }

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
