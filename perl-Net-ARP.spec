#
# Conditional build:
%bcond_with	tests		# perform "make test" (requires uid 0)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	ARP
Summary:	Perl extension for creating ARP packets
Summary(pl.UTF-8):	Rozszerzenie Perla do tworzenia pakietów ARP
Name:		perl-Net-ARP
Version:	1.0.6
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	1b71124347f23f951b96e86826af8562
URL:		http://search.cpan.org/dist/Net-ARP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-Pcap
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can be used to create and send ARP packets and to get the
MAC address of an ethernet interface or IP address.

%description -l pl.UTF-8
Ten moduł może być użyty do tworzenia i wysłania pakietów ARP oraz do
uzyskiwania adresu MAC interfejsu sieciowego lub adresu IP.

%prep
%setup -q -n %{pdir}-%{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Net/*.pm
%dir %{perl_vendorarch}/auto/Net/ARP
%attr(755,root,root) %{perl_vendorarch}/auto/Net/ARP/ARP.so
%{_mandir}/man3/*
