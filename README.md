# ansible

## Install (debian host assumed).
*create ansible user, add it to the sudo group and make sudo passwordless*
```bash
# adduser ansible
# usermod -a -G sudo ansible
# echo 'ansible ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/ansible
```
```bash
$ sudo apt install python3-venv python3-virtualenv git
$ sudo su - ansible
$ mkdir -v ~/.virtualenvs
$ python3 -m venv ~/.virtualenvs/ansible
$ source ~/.virtualenvs/ansible/bin/activate
(ansible) $ pip install --upgrade pip setuptools wheel
(ansible) $ pip install ansible
```
### Install collection from this repo.

ssh public key needs to be uploaded to git hub via web-frontend (settings -> SSH and GPG keys)

```(ansible) $ ansible-galaxy collection install git@github.com:ol-eg/ansible.git```

### Play examples.

```
$ cp -v ~/.ansible/collections/ansible_collections/oppa/all/ansible.cfg ~/.ansible.cfg
$ cp -v ~/.ansible/collections/ansible_collections/oppa/all/hosts ~/hosts
(ansible) $ ansible-playbook ~/ansible/playbooks/debian-laptop.yaml
```
