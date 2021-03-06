Name:           perl-Test-Simple
Version:        1.302078
Release:        1%{?dist}
Summary:        Basic utilities for writing tests
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Simple/
Source0:        http://www.cpan.org/authors/id/E/EX/EXODIST/Test-Simple-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008001
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util) >= 1.13
BuildRequires:  perl(Storable)
Requires:       perl(File::Spec)
Requires:       perl(File::Temp)
Requires:       perl(Scalar::Util) >= 1.13
Requires:       perl(Storable)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
** If you are unfamiliar with testing read Test::Tutorial first! **

%prep
%setup -q -n Test-Simple-%{version}

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
%doc appveyor.yml Changes cpanfile dist.ini examples LICENSE META.json README README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Apr 06 2017 Tom Schoonjans 1.302078-1
- Specfile autogenerated by cpanspec 1.78.
