%bcond_without	dist_kernel	# without distribution kernel

%define		snap	2008.12.23
%define		rev	137496
%define		modsrc	modules/linux
%define		rel	0.1
%{expand:%%global	ccver	%(%{__cc} -dumpversion)}

Summary:	VMWare guest utilities
Summary(pl.UTF-8):	Narzędzia dla systemu-gościa dla VMware
Name:		open-vm-tools
Version:	%{snap}_%{rev}
Release:	%{rel}
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/sourceforge/open-vm-tools/%{name}-%{snap}-%{rev}.tar.gz
# Source0-md5:	2c457c9bcee711140ec137a6829525eb
Source1:	%{name}-packaging
URL:		http://open-vm-tools.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libdnet-devel
BuildRequires:	libicu-devel
BuildRequires:	libtool
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.16}
BuildRequires:	pkgconfig
BuildRequires:	uriparser-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VMWare guest utilities.

%description -l pl.UTF-8
Narzędzia dla systemu-gościa dla VMware.

%package -n kernel%{_alt_kernel}-misc-pvscsi
Summary:	VMware pvscsi module
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-pvscsi
VMware pvscsi module.

%package -n kernel%{_alt_kernel}-misc-vmblock
Summary:	VMware vmblock module
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmblock
VMware vmblock module.

%package -n kernel%{_alt_kernel}-misc-vmci
Summary:	VMware vmci module
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmci
VMware vmci module.

%package -n kernel%{_alt_kernel}-misc-vmhgfs
Summary:	VMware vmhgfs module
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmhgfs
VMware vmhgfs module.

%package -n kernel%{_alt_kernel}-misc-vmmemctl
Summary:	VMware vmmemctl module
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmmemctl
VMware vmmemctl module.

%package -n kernel%{_alt_kernel}-misc-vmsync
Summary:	VMware vmsync module
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmsync
VMware vmsync module.

%package -n kernel%{_alt_kernel}-misc-vmxnet
Summary:	VMware vmxnet module
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmxnet
VMware vmxnet module.

%package -n kernel%{_alt_kernel}-misc-vmxnet3
Summary:	VMware vmxnet3 module
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmxnet3
VMware vmxnet3 module.

%package -n kernel%{_alt_kernel}-misc-vsock
Summary:	VMware vsock module
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vsock
VMware vsock module.

%prep
%setup -q -n %{name}-%{snap}-%{rev}
cp %{SOURCE1} packaging

%build
%build_kernel_modules -C %{modsrc}/pvscsi	-m pvscsi	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{ccver}
%build_kernel_modules -C %{modsrc}/vmblock	-m vmblock	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{ccver}
%build_kernel_modules -C %{modsrc}/vmci		-m vmci		SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{ccver}
%build_kernel_modules -C %{modsrc}/vmhgfs	-m vmhgfs	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{ccver}
%build_kernel_modules -C %{modsrc}/vmmemctl	-m vmmemctl	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{ccver}
%build_kernel_modules -C %{modsrc}/vmsync	-m vmsync	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{ccver}
%build_kernel_modules -C %{modsrc}/vmxnet	-m vmxnet	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{ccver}
%build_kernel_modules -C %{modsrc}/vmxnet3	-m vmxnet3	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{ccver}
%build_kernel_modules -C %{modsrc}/vsock	-m vsock	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{ccver}

%configure2_13 \
	--without-kernel-modules
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%install_kernel_modules -m %{modsrc}/pvscsi/pvscsi	-d misc
%install_kernel_modules -m %{modsrc}/vmblock/vmblock	-d misc
%install_kernel_modules -m %{modsrc}/vmci/vmci		-d misc
%install_kernel_modules -m %{modsrc}/vmhgfs/vmhgfs	-d misc
%install_kernel_modules -m %{modsrc}/vmmemctl/vmmemctl	-d misc
%install_kernel_modules -m %{modsrc}/vmsync/vmsync	-d misc
%install_kernel_modules -m %{modsrc}/vmxnet/vmxnet	-d misc
%install_kernel_modules -m %{modsrc}/vmxnet3/vmxnet3	-d misc
%install_kernel_modules -m %{modsrc}/vsock/vsock	-d misc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/sbin/mount.vmhgfs
ln -sf %{_sbindir}/mount.vmhgfs $RPM_BUILD_ROOT/sbin/mount.vmhgfs
mv $RPM_BUILD_ROOT/etc/pam.d/{vmware-guestd*,vmware-guestd}
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n kernel%{_alt_kernel}-misc-pvscsi
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmblock
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmci
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmhgfs
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmmemctl
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmsync
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmxnet
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmxnet3
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vsock
%depmod %{_kernel_ver}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README packaging
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/vmware-guestd
%dir /etc/vmware-tools
%attr(755,root,root) /etc/vmware-tools/*vm-*
%config(noreplace) %verify(not md5 mtime size) /etc/vmware-tools/tools.conf
/sbin/mount.vmhgfs
%attr(755,root,root) %{_bindir}/vmware-checkvm
%attr(755,root,root) %{_bindir}/vmware-hgfsclient
%attr(755,root,root) %{_bindir}/vmware-toolbox
%attr(755,root,root) %{_bindir}/vmware-toolbox-cmd
%attr(755,root,root) %{_bindir}/vmware-user
%attr(4755,root,root) %{_bindir}/vmware-user-suid-wrapper
%attr(755,root,root) %{_bindir}/vmware-xferlogs
%attr(755,root,root) %{_sbindir}/mount.vmhgfs
%attr(755,root,root) %{_sbindir}/vmware-guestd
%{_libdir}/lib*.so*
%{_desktopdir}/vmware-user.desktop

%files -n kernel%{_alt_kernel}-misc-pvscsi
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/pvscsi.ko*

%files -n kernel%{_alt_kernel}-misc-vmblock
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmblock.ko*

%files -n kernel%{_alt_kernel}-misc-vmci
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmci.ko*

%files -n kernel%{_alt_kernel}-misc-vmhgfs
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmhgfs.ko*

%files -n kernel%{_alt_kernel}-misc-vmmemctl
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmmemctl.ko*

%files -n kernel%{_alt_kernel}-misc-vmsync
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmsync.ko*

%files -n kernel%{_alt_kernel}-misc-vmxnet
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmxnet.ko*

%files -n kernel%{_alt_kernel}-misc-vmxnet3
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmxnet3.ko*

%files -n kernel%{_alt_kernel}-misc-vsock
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vsock.ko*
