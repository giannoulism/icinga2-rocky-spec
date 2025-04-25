Name:           icinga2
Version:        2.14.5
Release:        1%{?dist}
Summary:        Open Source Monitoring System

License:        GPLv2+
URL:            https://www.icinga.com/
Source0:        https://github.com/Icinga/icinga2/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  libedit-devel
BuildRequires:  openssl-devel
BuildRequires:  ncurses-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libxml2-devel
BuildRequires:  libcurl-devel
BuildRequires:  jansson-devel
BuildRequires:  mailx
BuildRequires:  systemd-devel
BuildRequires:  git

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Icinga 2 is a monitoring system that checks the availability of your network resources, notifies users of outages, and generates performance data.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir -p build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr \
         -DCMAKE_BUILD_TYPE=RelWithDebInfo \
         -DENABLE_LTO=ON
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install

%post
%systemd_post icinga2.service

%preun
%systemd_preun icinga2.service

%postun
%systemd_postun_with_restart icinga2.service

%files
%license LICENSE
%doc README.md
%{_sbindir}/icinga2
%{_bindir}/icinga2
%{_unitdir}/icinga2.service
%{_libdir}/icinga2
%{_sysconfdir}/icinga2
%{_datadir}/icinga2
%{_localstatedir}/lib/icinga2
%{_mandir}/man8/icinga2.8*

%changelog
* Wed Apr 24 2025 Michail Giannoulis giannoulis.m@gmail.com - 2.14.5-1
- Initial RPM build for Rocky Linux 9
