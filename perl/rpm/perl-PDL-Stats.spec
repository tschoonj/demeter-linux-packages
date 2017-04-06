Name:           perl-PDL-Stats
Version:        0.75
Release:        1%{?dist}
Summary:        Collection of statistics modules in Perl Data Language, with a quick-start guide for non-PDL people
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/PDL-Stats/
Source0:        http://www.cpan.org/authors/id/E/ET/ETJ/PDL-Stats-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(PDL::Core) >= 2.008
BuildRequires:  perl(PDL::Graphics::PGPLOT)
BuildRequires:  perl(PDL::Slatec)
BuildRequires:  perl(Test::More)
Requires:       perl(PDL::Core) >= 2.008
Requires:       perl(PDL::Graphics::PGPLOT)
Requires:       perl(PDL::Slatec)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Loads modules named below, making the functions available in the current
namespace.

%prep
%setup -q -n PDL-Stats-%{version}
#patch
sed -i -e "s/propagate/propogate/g" GLM/glm.pd

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
%doc Changes META.json README.md
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
* Thu Apr 06 2017 Tom Schoonjans 0.75-1
- Specfile autogenerated by cpanspec 1.78.
