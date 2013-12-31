%define major 4
%define libname %mklibname %name %major
%define develname %mklibname -d %name
%define staticname %mklibname -s -d %name

Summary:	Produces a document with syntax highlighting
Name:		source-highlight
Version:	3.1.7
Release:	8
Group:		Development/Other
License:	GPLv3+
Source:		ftp://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/src-highlite/
%rename	java2html
%rename cpp2html

BuildRequires:	bison 
BuildRequires:	flex
BuildRequires:	boost-devel
BuildRequires:	ctags
BuildRequires:	help2man
Requires:	ctags
Requires:	help2man

%description
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%package -n %{libname}
Group:		System/Libraries
Summary:	Produces a document with syntax highlighting

%description -n %{libname}
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%package -n %{develname}
Group:		Development/C
Summary:	Produces a document with syntax highlighting
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%package -n %{staticname}
Group:		Development/C
Summary:	Produces a document with syntax highlighting
Provides:	lib%name-static-devel = %{version}-%{release}
Requires:	%{develname} = %{version}-%{release}

%description -n %{staticname}
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
%configure2_5x \
	--disable-dependency-tracking \
	--with-boost-libdir=%{_libdir} \
    --enable-static

%make

%install
%makeinstall_std

rm -fr %{buildroot}%{_datadir}/doc/

%files
%doc AUTHORS README CREDITS NEWS TODO.txt THANKS
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*
%{_sysconfdir}/bash_completion.d/*

%files -n %{libname}
%_libdir/lib%{name}.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%_libdir/lib%{name}.so
%_libdir/pkgconfig/*.pc
%_includedir/srchilite/

%files -n %{staticname}
%_libdir/lib%{name}.a


