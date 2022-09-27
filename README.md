# ansible

## Install (debian 11 host assumed).
*create ansible user, add it to the sudo group and make sudo passwordless*
```bash
# adduser ansible
# usermod -a -G sudo ansible
# echo 'ansible ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/ansible
# apt install pipenv
```
*logout -> login for sudo group to propogate*
```bash
$ sudo su - ansible
$ pipenv --python 3.9
$ pipenv shell --fancy
$ pipenv run install --upgrade pip setuptools wheel
$ pipenv install ansible
```
### Install collection from this repo.

*ssh public key needs to be uploaded to git hub via web-frontend (settings -> SSH and GPG keys)*

```
$ sudo apt install git
$ ansible-galaxy collection install git@github.com:ol-eg/ansible.git
```

### Play examples.

```
$ ln -v ~/.ansible/collections/ansible_collections/oppa/all/ansible.cfg ~/ansible.cfg
$ ln -v ~/.ansible/collections/ansible_collections/oppa/all/hosts ~/hosts
# provision new laptop after freshly instatlled debian
$ ansible-playbook ~/ansible/playbooks/debian-laptop.yaml
```
