%define name elk-compose 
%define version 1.0.0
%define unmangled_version 1.0.0
%define unmangled_version 1.0.0
%define release 1

Summary: Elk Compose  
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz  
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Turbo Python <office@realpython.com>
Url: https://github.com/pythonredhat/python-backup-tool

#BuildRequires: pyinstaller
#Requires: rh-python3

%description
Elk stack as docker compose file 

%prep
%setup -q
%build 
%install
mkdir -p /opt/elk-service 
install -m 0755 -d $RPM_BUILD_ROOT/opt/elk-service
install -m 0755 docker-compose.yml $RPM_BUILD_ROOT/opt/elk-service/docker-compose.yml
install -m 0755 -d $RPM_BUILD_ROOT/opt/elk-service/nginx
install -m 0755 default.conf $RPM_BUILD_ROOT/opt/elk-service/nginx/default.conf

#%clean
#rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)