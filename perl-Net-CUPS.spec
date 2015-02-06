%define upstream_name    Net-CUPS
%define upstream_version 0.61

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.610.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.610.0-1mdv2010.0
+ Revision: 418545
- update to 0.61

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.600.0-1mdv2010.0
+ Revision: 408837
- update to 0.60

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.590.0-1mdv2010.0
+ Revision: 404065
- rebuild using %%perl_convert_version

* Fri Sep 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.59-1mdv2009.0
+ Revision: 281111
- update to new version 0.59

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.58-1mdv2009.0
+ Revision: 277954
- update to new version 0.58

* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.57-1mdv2009.0
+ Revision: 272041
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdv2009.0
+ Revision: 194693
- import perl-Net-CUPS


* Wed Apr 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdv2008.1
- initial mdv import
