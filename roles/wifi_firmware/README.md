wifi_firmware
=============

Install wifi firmware.
I have this separate as I believe it is good to reboot at the end,
and I will be playng this locally most of the time.

*I have been lucky that Debian falks packaged drivers for atheros.*

To see what wifi hardware you've been sold :)

```$ lspci | grep -i net```

To see if you're lucky :)

```$ sudo apt-cache search firmware-```

*Most of the firmware lives in non-free repos...*

Requirements
------------

Debian OS, ansible.

Role Variables
--------------

*defaults are in* ```./defaults/main.yml```

- ```firmware```: firmware package name, default: ```firmware-atheros```.

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
        - { role: wifi_firmware }

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
