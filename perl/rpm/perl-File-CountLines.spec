Name:           perl-File-CountLines
Version:        0.0.3
Release:        1%{?dist}
Summary:        Efficiently count the number of line breaks in a file
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-CountLines/
Source0:        http://www.cpan.org/authors/id/M/MO/MORITZ/File-CountLines-v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Module::Build)
Requires:       perl(Carp)
Requires:       perl(Exporter) >= 5.57
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
perlfaq5 answers the question on how to count the number of lines in a
file. This module is a convenient wrapper around that method, with
additional options.

%prep
%setup -q -n File-CountLines-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Apr 06 2017 Tom Schoonjans 0.0.3-1
- Specfile autogenerated by cpanspec 1.78.
