Name: nornet-ca
Version: 1.1.1~rc1
Release: 1
Summary: NorNet Root CA
Group: Applications/Internet
License: GPLv3
Source: %{name}-%{version}.tar.gz

AutoReqProv:   on
BuildRequires: cmake
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
Requires:      ca-certificates


%description
This package installs the NorNet Root CA certificate.

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/usr/share/pki/ca-trust-source/anchors
mv %{buildroot}/usr/share/ca-certificates/nornet/NorNet-CA-Level1.crt %{buildroot}/usr/share/pki/ca-trust-source/anchors/

%post
update-ca-trust

%files
%{_datadir}/pki/ca-trust-source/anchors/NorNet-CA-Level1.crt


%changelog
* Wed Jun 19 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.0
- New upstream release.
* Wed Dec 16 2015 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.0
- Created RPM package.
