Name: nornet-ca
Version: 1.1.10
Release: 1
Summary: NorNet Root CA
Group: Applications/Internet
License: GPL-3+
Source: %{name}-%{version}.tar.gz

AutoReqProv:   on
BuildRequires: cmake
BuildRequires: gcc
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
Requires:      ca-certificates


%description
This package installs the NorNet Root CA certificate.

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr .
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}/usr/share/pki/ca-trust-source/anchors
mv %{buildroot}/usr/share/ca-certificates/nornet/NorNet-CA-Level1.crt %{buildroot}/usr/share/pki/ca-trust-source/anchors/

%post
update-ca-trust

%files
%{_datadir}/pki/ca-trust-source/anchors/NorNet-CA-Level1.crt


%changelog
* Tue Oct 19 2021 Thomas Dreibholz <dreibh@simula.no> - 1.1.10
- New upstream release.
* Fri Aug 27 2021 Thomas Dreibholz <dreibh@simula.no> - 1.1.9
- New upstream release.
* Fri Nov 13 2020 Thomas Dreibholz <dreibh@simula.no> - 1.1.8
- New upstream release.
* Thu Nov 07 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.7
- New upstream release.
* Fri Aug 23 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.6
- New upstream release.
* Wed Aug 07 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.5
- New upstream release.
* Wed Aug 07 2019 Thomas Dreibholz <dreibh@simula.no> - 1.1.4
- New upstream release.
* Wed Aug 07 2019 Thomas Dreibholz <dreibh@simula.no> - 1.1.3
- New upstream release.
* Thu Jun 27 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.2
- New upstream release.
* Wed Jun 19 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.1
- New upstream release.
* Wed Jun 19 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.0
- New upstream release.
* Wed Dec 16 2015 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.0
- Created RPM package.
