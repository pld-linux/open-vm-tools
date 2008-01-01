%define		_date	2007.11.21
%define		_rel	64693
%define		_ver	%{_date}-%{_rel}
Summary:	VMWare guest utilities
Summary(pl.UTF-8):	-
Name:		open-vm-tools
Version:	%{_date}_%{_rel}
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{_ver}.tar.gz
# Source0-md5:	1cc034f14769375f41f6410d709dacbc
#Patch0:		%{name}-DESTDIR.patch
URL:		http://open-vm-tools.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
#BuildArch:	%{ix86,amd64}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q -n %{name}-%{_ver}

%build
##%{__aclocal}
##%{__autoconf}
##%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
