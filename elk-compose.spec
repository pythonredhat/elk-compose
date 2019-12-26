%define name elk-stack
%define version 1.0.0
%define unmangled_version 1.0.0
%define unmangled_version 1.0.0
%define release 1

Summary: Elk Stack 
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
mkdir -p /opt/elk-compose
install -m 0755 -d $RPM_BUILD_ROOT/opt/elk-compose
install -m 0755 $RPM_BUILD_ROOT/opt/elk-compose/docker-compose.yml
install -m 0755 -d $RPM_BUILD_ROOT/opt/elk-compose/nginx
install -m 0755 $RPM_BUILD_ROOT/opt/elk-compose/nginx/default.conf

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)