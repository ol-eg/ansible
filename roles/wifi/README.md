wifi
====

Install GNU Network Manager and attempt to connect to wifi network.
Connection is attempted using
[custom module](../../plugins/modules/readme.md).

Requirements
------------

Debian OS, ansible.

*[wifi_firmware](../wifi_firmware/README.md) must be played prio to this role.*

Role Variables
--------------

*[defaults](./defaults/main.yml)*

- ```nm_package```: GNU Network Manager package. 

Example Playbook
----------------

    - hosts: localhost
      become: yes
      vars_prompt:
         - name: wifi_password
           prompt: wifi password?
           private: yes
      roles:
         - { role: wifi, password: '{{ wifi_password }}' }

To Test
-------

requires:
- os packages: virtualbox, vagrant
- python packages: ansible, molecule-vagrant, python-vagrant

*comment out last [task](./tasks/main.yml)*

```(asible) $ mol test```

License
-------

MIT

Author Information
------------------

o-le-g@inbox.ru
