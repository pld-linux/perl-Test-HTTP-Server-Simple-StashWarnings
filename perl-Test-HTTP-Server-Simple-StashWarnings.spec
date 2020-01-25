#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%define		pdir	Test
%define		pnam	HTTP-Server-Simple-StashWarnings
Summary:	Test::HTTP-Server-Simple-StashWarnings Perl module - catch your forked server's warnings
Name:		perl-Test-HTTP-Server-Simple-StashWarnings
Version:	0.03
Release:	2
Source0:	http://search.cpan.org/CPAN/authors/id/S/SA/SARTAK/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:  0a63b8f45217f05611717292b7ec02e5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
URL:		http://search.cpan.org/dist/Test-HTTP-Server-Simple-StashWarnings/
BuildRequires:	perl-HTTP-Server-Simple
BuildRequires:	perl-Test-HTTP-Server-Simple
BuildRequires:	perl-WWW-Mechanize
BuildRequires:	perl-devel >= 1:5.8.7
%if %{with tests}
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::HTTP-Server-Simple-StashWarnings - catch your forked server's
warnings.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
# %{perl_vendorlib}/Test/HTTP/Server/Simple/StashWarnings.pm
%{perl_vendorlib}/Test/HTTP
%{_mandir}/man3/*
