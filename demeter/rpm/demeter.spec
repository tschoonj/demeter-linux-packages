Name: demeter
Version: 0.9.25	
Release: 1%{?dist}
Summary: Demeter is a comprehensive system for processing and analyzing X-ray Absorption Spectroscopy data.	

Group: Applications/Engineering and Scientific 
License: Perl artistic license
URL: http://bruceravel.github.io/demeter/
Source0: https://github.com/bruceravel/demeter/archive/0.9.25.tar.gz

BuildRequires: epel-release
BuildRequires: perl(Module::Build)
BuildRequires: perl(Capture::Tiny)
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(File::Slurper)
BuildRequires: perl(Pod::ProjectDocs)
BuildRequires: ifeffit
BuildRequires: perl(Archive::Zip)
BuildRequires: perl(Capture::Tiny)
BuildRequires: perl(Chemistry::Elements)
BuildRequires: perl(Config::INI)
BuildRequires: perl(Const::Fast)
BuildRequires: perl(DateTime)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Encoding::FixLatin)
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(File::CountLines)
BuildRequires: perl(File::Touch)
BuildRequires: perl(File::Which)
BuildRequires: perl(Graph)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(Heap)
BuildRequires: perl(JSON)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Math::Combinatorics)
BuildRequires: perl(Math::Derivative)
BuildRequires: perl(Math::Random)
BuildRequires: perl(Math::Round)
BuildRequires: perl(Math::Spline)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Aliases)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(MooseX::Types::LaxNum)
BuildRequires: perl(PDL)
BuildRequires: perl(Pod::POM)
BuildRequires: perl(Regexp::Assemble)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Spreadsheet::WriteExcel)
BuildRequires: perl(Statistics::Descriptive)
BuildRequires: perl(Text::Template)
BuildRequires: perl(Text::Unidecode)
BuildRequires: perl(Tree::Simple)
BuildRequires: perl(Want)
BuildRequires: perl(XMLRPC::Lite)
BuildRequires: perl(YAML::Tiny)
#optional
BuildRequires: perl(File::Monitor::Lite)
BuildRequires: perl(Graphics::GnuplotIF)
BuildRequires: perl(Term::Sk)
BuildRequires: perl(Term::Twiddle)
BuildRequires: perl(Wx)
Requires: ifeffit
Requires: perl(autodie)
Requires: perl(Archive::Zip)
Requires: perl(Capture::Tiny)
Requires: perl(Chemistry::Elements)
Requires: perl(Config::INI)
Requires: perl(Const::Fast)
Requires: perl(DateTime)
Requires: perl(Digest::SHA)
Requires: perl(Encoding::FixLatin)
Requires: perl(File::Copy::Recursive)
Requires: perl(File::CountLines)
Requires: perl(File::Touch)
Requires: perl(File::Which)
Requires: perl(Graph)
Requires: perl(HTML::Entities)
Requires: perl(Heap)
Requires: perl(JSON)
Requires: perl(List::MoreUtils)
Requires: perl(Math::Combinatorics)
Requires: perl(Math::Derivative)
Requires: perl(Math::Random)
Requires: perl(Math::Round)
Requires: perl(Math::Spline)
Requires: perl(Moose)
Requires: perl(MooseX::Aliases)
Requires: perl(MooseX::Types)
Requires: perl(MooseX::Types::LaxNum)
Requires: perl(PDL)
Requires: perl(Pod::POM)
Requires: perl(Regexp::Assemble)
Requires: perl(Regexp::Common)
Requires: perl(Spreadsheet::WriteExcel)
Requires: perl(Statistics::Descriptive)
Requires: perl(Text::Template)
Requires: perl(Text::Unidecode)
Requires: perl(Tree::Simple)
Requires: perl(Want)
Requires: perl(XMLRPC::Lite)
Requires: perl(YAML::Tiny)
#optional
Requires: perl(File::Monitor::Lite)
Requires: perl(Graphics::GnuplotIF)
Requires: perl(Term::Sk)
Requires: perl(Term::Twiddle)
Requires: perl(Wx)

Provides: perl(Demeter)

AutoReqProv: no

%description
Demeter is a comprehensive system for processing and analyzing X-ray Absorption Spectroscopy data.	


%prep
%setup -q


%build
%{__perl} Build.PL installdirs=vendor destdir=$RPM_BUILD_ROOT
./Build


%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
#./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{perl_vendorarch}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*


%changelog
* Thu Apr 06 2017 Tom Schoonjans 
- Initial version of the SPEC file 
