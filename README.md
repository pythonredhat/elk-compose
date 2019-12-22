# allow nginx to connect to kibana port if you're using selinux
```bash
semanage port -a -t http_port_t -p tcp 5601
```
