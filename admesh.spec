Summary:	Diagnose and/or repair problems with STereo Lithography files
Name:		admesh
Version:	0.98.2
Release:	1
License:	GPL v2+
Group:		Applications/Engineering
URL:		http://github.com/admesh/admesh/
Source0:	http://github.com/admesh/admesh/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a90692eb6dc5289e95949bbbca3e37e9
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description
ADMesh is a program for diagnosing and/or repairing commonly
encountered problems with STL (STereo Lithography) data files. It can
remove degenerate and unconnected facets, connect nearby facets, fill
holes by adding facets, and repair facet normals. Simple
transformations such as scaling, translation and rotation are also
supported. ADMesh can read both ASCII and binary format STL files,
while the output can be in AutoCAD DXF, Geomview OFF, STL, or VRML
format.

%package devel
Summary:	Development files for the %{name} library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
ADMesh is a program for diagnosing and/or repairing commonly
encountered problems with STL (STereo Lithography) data files.

This package contains the development files needed for building new
applications that utilize the %{name} library.

%package libs
Summary:	Runtime library for the %{name} application
Group:		Development/Libraries

%description libs
This package contains the %{name} runtime library.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{name}.la

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog ChangeLog.old README.md AUTHORS
%doc %{name}-doc.txt block.stl
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/admesh.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/admesh
%{_pkgconfigdir}/libadmesh.pc
%attr(755,root,root) %{_libdir}/lib%{name}.so

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib%{name}.so.1
%attr(755,root,root) %{_libdir}/lib%{name}.so.*.*
