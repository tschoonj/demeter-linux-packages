Name: ifeffit
Version: 1.2.final	
Release: 1%{?dist}
Summary: XAFS analysis programs

Group: Applications/Engineering and Scientific 
License: BSD
URL: https://github.com/newville/ifeffit	
Source0: https://github.com/newville/ifeffit/archive/1.2.final.tar.gz

BuildRequires:	readline-devel gcc-gfortran
Requires: libgfortran

%description
FEFFIT is a suite of interactive programs for XAFS analysis, combining high-quality and well-tested XAFS analysis algorithms, tools for general data manipulation, and graphical display of data. 

%prep
%setup -q


%build
%configure FFLAGS="-fPIC"
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%defattr(-,root,root)
%{_bindir}/autobk
%{_bindir}/diffkk
%{_bindir}/feff6
%{_bindir}/feffit
%{_bindir}/ifeffit
%{_includedir}/ifeffit.h
%{_libdir}/*.a
%{_datadir}/ifeffit/*



%changelog
* Wed Apr 5 2017 Tom Schoonjans <Tom.Schoonjans@diamond.ac.uk>
- Initial version

