#
# Conditional build:
%bcond_without	tests		# don't perform "make check"
				# (note: tests need endoder-enabled szip)
#
Summary:	NetCDF C++ library (old API)
Summary(pl.UTF-8):	Biblioteka NetCDF dla języka C++ (stare API)
Name:		netcdf-cxx
Version:	4.2
Release:	5
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.unidata.ucar.edu/pub/netcdf/%{name}-%{version}.tar.gz
# Source0-md5:	d32b20c00f144ae6565d9e98d9f6204c
Patch0:		%{name}-info.patch
URL:		http://www.unidata.ucar.edu/packages/netcdf/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	netcdf-devel >= 4.2
BuildRequires:	texinfo
Requires:	netcdf >= 4.2
Obsoletes:	netcdf-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetCDF (network Common Data Form) is an interface for array-oriented
data access and a library that provides an implementation of the
interface. The netCDF library also defines a machine-independent
format for representing scientific data. Together, the interface,
library, and format support the creation, access, and sharing of
scientific data. The netCDF software was developed at the Unidata
Program Center in Boulder, Colorado.

This package contains C++ library with old API.

%description -l pl.UTF-8
NetCDF (Network Common Data Form) jest interfejsem dostępu do danych
zorganizowanych w tablice. Biblioteka netCDF definiuje niezależny od
maszyny format reprezentowania danych naukowych. Interfejs oraz
biblioteka pozwalają na tworzenie, dostęp i współdzielenie danych.
NetCDF powstał w Unidata Program Center w Boulder, Colorado.

Ten pakiet zawiera bibliotekę dla języka C++ ze starym API.

%package devel
Summary:	Header files for netCDF C++ old interface
Summary(pl.UTF-8):	Pliki nagłówkowe starego interfejsu netCDF dla języka C++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	netcdf-devel >= 4.2
Obsoletes:	netcdf-c++-devel

%description devel
Header files for netCDF - old C++ interface.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki netCDF - stary interfejs dla języka C++.

%package static
Summary:	NetCDF C++ static library (old API)
Summary(pl.UTF-8):	Biblioteka statyczna netCDF dla języka C++ (stare API)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	netcdf-c++-static

%description static
Static version of netCDF C++ library with old API.

%description static -l pl.UTF-8
Statyczna wersja biblioteki netCDF dla języka C++ ze starym API.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%if %{with tests}
%{__make} -j1 check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc COPYRIGHT
%attr(755,root,root) %{_libdir}/libnetcdf_c++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetcdf_c++.so.4

%files devel
%defattr(644,root,root,755)
%doc man4/netcdf-cxx.html
%attr(755,root,root) %{_libdir}/libnetcdf_c++.so
%{_libdir}/libnetcdf_c++.la
%{_includedir}/ncvalues.h
%{_includedir}/netcdf.hh
%{_includedir}/netcdfcpp.h
%{_infodir}/netcdf-cxx.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetcdf_c++.a
