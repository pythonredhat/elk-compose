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


# Build instuctions:
1) tar up repo
2) place in SOURCES of rpm build tree
3) 


