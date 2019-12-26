# allow nginx to connect to kibana port if you're using selinux
```bash
semanage port -a -t http_port_t -p tcp 5601
```

# rhel rpm build guide
```bash
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/rpm_packaging_guide/index?extIdCarryOver=true&sc_cid=701f2000001OH6pAAG
```

# fedora official rpm packaging guide
```bash
https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/index.html
```


# Build instuctions (doing local for now but later port to Gitlab with version control):
1) install dev tools:
```bash
yum install rpm-build rpmdevtools -y
```

2) setup build directory structure:
```bash
#running command from from /root/
rpmdev-setuptree
```

3) tar up source code and place in SOURCES of rpm build tree:
```bash
tar czvf elk-compose-1.0.0.tar.gz elk-compose-1.0.0
cp elk-compose-1.0.0.tar.gz /root/rpmbuild/SOURCES 
```

4) copy spec file to SPECS of rpm build tree:
```bash
cp elk-compose.spec /root/rpmbuild/SPECS
```
5) build the rpm
```bash
cd /root/rpmbuild
rpmbuild -ba SPECS/elk-compose.spec
```
6) install the rpm on CentOS:
```bash
rpm -ivh /root/rpmbuild/RPMS/noarch/elk-compose-1.0.0-1.noarch.rpm
```

