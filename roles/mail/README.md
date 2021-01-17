mail
====

By default debian has exim4 installed, and configured
to handle local mail only (mail addressed to sys admin (root)).
Here we install mutt, and make sure mail addressed to root is
redirected to a user account.

Requirements
------------

Debian OS, ansible.

Role Variables
--------------

*[defaults](./defaults/main.yml)*

- ```aliases```: Mail aliases config file.
- ```homedir_prefix```: Default: /home.
- ```prerequisites```: Packages to be present in the system.
- ```user```: User used for reading mail addressed to root.

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
         - { role: mail }

To Test
-------

requires:
- os packages: docker.
- python packages: ansible, molecule.

```(asible) $ mol test```

License
-------

MIT

Author Information
------------------

o-le-g@inbox.ru
