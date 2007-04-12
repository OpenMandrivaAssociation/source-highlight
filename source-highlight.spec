%define name	source-highlight
%define	version 2.5
%define release %mkrel 1

Summary: 	Produces a document with syntax highlighting
Name: 		%{name}
Version: 	%{version}
Release:	%{release}
Group: 		Development/Other
License: 	GPL
Source: 	ftp://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.bz2
URL: 		http://www.gnu.org/software/src-highlite/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	java2html
Obsoletes:	cpp2html
Provides:	java2html
Provides:	cpp2html

BuildRequires:	bison 
BuildRequires:  flex
BuildRequires:  boost-devel

%description
This program, given a source file, produces a document with syntax 
highlighting. At the moment this package can handle :
* Java
* C/C++
* Prolog
* Perl
* Php3 new
as source languages, and HTML as output format.
NOTICE: now the name of the program is source-highlight: there are no two 
separate programs, namely java2html and cpp2html, anymore.  However there 
are two shell scripts with the same name in order to facilitate the 
migration (however their use is not advised). 


%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -fr $RPM_BUILD_ROOT%{_datadir}/doc/

%post
%_install_info %{name}.info

%postun
%_remove_install_info %{name}.info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*


