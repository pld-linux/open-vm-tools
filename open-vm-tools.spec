%define		snap	2007.11.21
%define		rev	64693
Summary:	VMWare guest utilities
Summary(pl.UTF-8):	Narzędzia dla systemu-gościa dla VMware
Name:		open-vm-tools
Version:	%{snap}_%{rev}
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/open-vm-tools/%{name}-%{snap}-%{rev}.tar.gz
# Source0-md5:	1cc034f14769375f41f6410d709dacbc
URL:		http://open-vm-tools.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VMWare guest utilities.

%description -l pl.UTF-8
Narzędzia dla systemu-gościa dla VMware.

%prep
%setup -q -n %{name}-%{snap}-%{rev}

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
