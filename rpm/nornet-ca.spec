Name:          nornet-ca
Version:       1.0.0
Release:       1
Summary:       NorNet Root CA
Group:         Applications/Internet
License:       GPLv3
Source:        %{name}-%{version}.tar.gz

AutoReqProv:   on
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-build

%description
This package installs the NorNet Root CA certificate.

%prep 
%setup -q

%build 

#%configure 
#true

%install
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
cp src/ca/NorNet-CA-Level1.crt          "$RPM_BUILD_ROOT"/usr/share/pki/ca-trust-source/anchors/

%post
update-ca-trust

%prerun

%clean
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/ca/NorNet-CA-Level1.crt

%doc

%changelog
* Thu Dec 16 2015 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.0
- Created RPM package.
