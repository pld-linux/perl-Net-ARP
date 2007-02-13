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
Version:	0.8
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	47214ca439a339ab405d65c7790d5b68
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
Ten moduł może być użyty do stworzenia i wysłania pakietów ARP oraz do
pobrania adresu MAC interfejsu sieciowego lub adresu IP.

%prep
%setup -q -n %{pdir}-%{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/auto/Net/ARP/ARP.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/ARP/ARP.so
%{_mandir}/man3/*
