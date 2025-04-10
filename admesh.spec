Summary:	Diagnose and/or repair problems with STereo Lithography files
Summary(pl.UTF-8):	Diagnostyka i/lub naprawa plików STL (służących do stereolitografii)
Name:		admesh
Version:	0.98.5
Release:	1
License:	GPL v2+
Group:		Applications/Engineering
#Source0Download: https://github.com/admesh/admesh/releases
Source0:	https://github.com/admesh/admesh/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	36d6b13ee568f27501584b1259d6fe01
URL:		https://github.com/admesh/admesh/
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

%description -l pl.UTF-8
ADMesh to program do diagnostyki i/lub naprawy najczęściej
występujących problemów w plikach STL (STereo Lithography), służących
do stereolitografii. Potrafi usuwać zdegenerowane i niepołączone
ściany, łączyć bliskie ściany, wypełniać dziury przez dodanie ścian
oraz naprawiać normalne ścian. Obsługiwane są także proste
przekształcenia, takie jak skalowanie, przesunięcia i obroty. ADMesh
potrafi czytać pliki STL w formacii ASCII, jak i binarym, zaś wyjście
może być w formacie AutoCAD DXF, Geomview OFF, STL lub VRML.

%package libs
Summary:	Runtime library for the ADMesh application
Summary(pl.UTF-8):	Biblioteka uruchomieniowa aplikacji ADMesh
Group:		Libraries

%description libs
This package contains the ADMesh runtime library.

%description libs -l pl.UTF-8
Ten pakiet zawiera bibliotekę uruchomieniową ADMesh.

%package devel
Summary:	Development files for the ADMesh library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki ADMesh
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
ADMesh is a program for diagnosing and/or repairing commonly
encountered problems with STL (STereo Lithography) data files.

This package contains the development files needed for building new
applications that utilize the ADMesh library.

%description devel -l pl.UTF-8
ADMesh to program do diagnostyki i/lub naprawy najczęściej
występujących problemów w plikach STL (STereo Lithography), służących
do stereolitografii.

Ten pakiet zawiera pliki programistyczne, potrzebe do budowania nowych
aplikacji wykorzystujących bibliotekę ADMesh.

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

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libadmesh.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog ChangeLog.old README.md admesh-doc.txt block.stl
%attr(755,root,root) %{_bindir}/admesh
%{_mandir}/man1/admesh.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libadmesh.so.*.*.*
%ghost %{_libdir}/libadmesh.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libadmesh.so
%{_includedir}/admesh
%{_pkgconfigdir}/libadmesh.pc
