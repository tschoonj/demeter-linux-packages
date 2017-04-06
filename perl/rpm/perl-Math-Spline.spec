Name:           perl-Math-Spline
Version:        0.02
Release:        1%{?dist}
Summary:        Cubic Spline Interpolation of data
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Spline/
Source0:        http://www.cpan.org/authors/id/C/CH/CHORNY/Math-Spline-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::Derivative)
BuildRequires:  perl(Test::More)
Requires:       perl(Carp)
Requires:       perl(Exporter) >= 5.57
Requires:       perl(Math::Derivative)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This package provides cubic spline interpolation of numeric data. The data
is passed as references to two arrays containing the x and y ordinates. It
may be used as an exporter of the numerical functions or, more easily as a
class module.

%prep
%setup -q -n Math-Spline-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc META.json README Release
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Apr 06 2017 Tom Schoonjans 0.02-1
- Specfile autogenerated by cpanspec 1.78.