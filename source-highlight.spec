%define name	source-highlight
%define	version 2.11
%define release %mkrel 1

Summary: 	Produces a document with syntax highlighting
Name: 		%{name}
Version: 	%{version}
Release:	%{release}
Group: 		Development/Other
License: 	GPLv3+
Source: 	ftp://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz
URL: 		http://www.gnu.org/software/src-highlite/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	java2html
Obsoletes:	cpp2html
Provides:	java2html
Provides:	cpp2html

BuildRequires:	bison 
BuildRequires:  flex
BuildRequires:  boost-devel
BuildRequires:	ctags help2man
Requires:	ctags help2man

%description
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%prep
%setup -q

%build
%configure2_5x --disable-dependency-tracking
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
%doc AUTHORS README ChangeLog CREDITS NEWS TODO.txt THANKS
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*
%{_sysconfdir}/bash_completion.d/*
