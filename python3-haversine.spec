%global srcname haversine-2.7.0
%global debug_package ${nil}

%define __python3 /usr/bin/python3.8

Name:           python3-haversine
Version:        2.7.0
Release:        0
Summary:        cmake package
Group:          Application/Network
License:        GPL
URL:            https://github.com/mapado/haversine
Vendor:         mapado
Source:         https://github.com/mapado/haversine/archive/refs/tags/v2.7.0.tar.gz
Prefix:         %{_prefix}
Packager:       Dragonfly
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:      x86_64
BuildRequires:  python38-devel, python38
Requires:       python38

%description
cmake middleware

%prep
%setup -n %{srcname}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --root %{buildroot}

%files
%{python3_sitelib}/*

%changelog
* Wed Jul 06 2022 Dragonfly <dragonfly@upnext.com> - 2.7.0-0
- First package cmake