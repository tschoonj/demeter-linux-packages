# Demeter packages for Linux

This project is an attempt at creating linux packages for the acclaimed [Demeter](https://github.com/bruceravel/demeter) package for XAFS analysis.
Included are the necessary configuration files to create the packages yourself, but also includes instructions (see below) to install the prepackaged binaries
using the default package manager of the distribution.

Currently only one Linux distribution (RHEL 7 and derivatives) is supported, but I plan on adding more in the future (Ubuntu!).

## RHEL 7

To install Demeter on your RHEL 7 (or CentOS, Scientific Linux and other derivatives), execute the following commands, as root:

````bash
sudo yum install epel-release
sudo rpm -Uvh http://xmi-yum.tomschoonjans.eu/xmi-repo-key-7.0-1.el7.noarch.rpm
sudo yum install demeter
````

