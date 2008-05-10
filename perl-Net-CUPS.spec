%define module   Net-CUPS
%define version    0.56
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Common Unix Printing System Interface
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: cups-devel
BuildRequires: perl(Test::More)
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Net::CUPS is an object oriented interface to the Common Unix Printing
System.

%prep
%setup -q -n %{module}-%{version} 

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

