Name: metacafe-dl
Version: 2008.07.23
Release: 1
Summary: Download videos from Metacafe
License: MIT
Group: Networking/File transfer
Url: https://github.com/glixx/metacafe-dl
Source0: metacafe-dl
BuildArch: noarch

%description
Metacafe-dl is a small command-line program to download videos 
from MetaCafe.com.

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
