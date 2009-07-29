%define upstream_name    Net-CUPS
%define upstream_version 0.59

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Common Unix Printing System Interface
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: cups-devel
BuildRequires: perl(Test::More)
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Net::CUPS is an object oriented interface to the Common Unix Printing
System.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# those test requires a running cups server
# http://rt.cpan.org/Ticket/Display.html?id=38469
rm -f t/03_destination.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*
