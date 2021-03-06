Name:           perl-Alien-wxWidgets
Version:        0.67
Release:        1%{?dist}
Summary:        Building, finding and using wxWidgets binaries
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Alien-wxWidgets/
Source0:        http://www.cpan.org/authors/id/M/MD/MDOOTSON/Alien-wxWidgets-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 0:5.006
BuildRequires:  wxGTK-devel
BuildRequires:  perl-core
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.24
BuildRequires:  perl(File::Spec) >= 1.50
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Pluggable) >= 2.6
Requires:       perl(Module::Pluggable) >= 2.6
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       wxGTK

%description
Please see Alien for the manifesto of the Alien namespace.

%prep
%setup -q -n Alien-wxWidgets-%{version}

%build
export WX_CONFIG=/usr/bin/wx-config
%{__perl} Build.PL installdirs=vendor destdir=$RPM_BUILD_ROOT --wxWidgets-build=0
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes META.json patches README.txt script
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
* Thu Apr 06 2017 Tom Schoonjans 0.67-1
- Specfile autogenerated by cpanspec 1.78.
