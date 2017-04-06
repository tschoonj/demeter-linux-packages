Name:           perl-Graphics-GnuplotIF
Version:        1.8
Release:        1%{?dist}
Summary:        Dynamic Perl interface to gnuplot
License:        CHECK(Distributable)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Graphics-GnuplotIF/
Source0:        http://www.cpan.org/authors/id/M/ME/MEHNER/Graphics-GnuplotIF-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version)
Requires:       perl(Test::More)
Requires:       gnuplot
Requires:       perl(version)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Graphics::GnuplotIF is a simple and easy to use dynamic Perl interface to
gnuplot. gnuplot is a freely available, command-driven graphical display
tool for Unix. It compiles and works quite well on a number of Unix
flavours as well as other operating systems, including Windows with
gnuplot.exe.

%prep
%setup -q -n Graphics-GnuplotIF-%{version}

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
%doc Changes META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Apr 06 2017 Tom Schoonjans 1.8-1
- Specfile autogenerated by cpanspec 1.78.
