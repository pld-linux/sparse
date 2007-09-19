Summary:	Sparse - a semantic parser of source files
Summary(pl.UTF-8):	Sparse - analizator semantyczny plików źródlowych
Name:		sparse
Version:	0.4
Release:	1
License:	GPL
Group:		Development/Debuggers
Source0:	http://kernel.org/pub/software/devel/sparse/dist/%{name}-%{version}.tar.gz
# Source0-md5:	dedd6043e7665ab134c20a45ecbc030c
URL:		http://kernel.org/pub/software/devel/sparse/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sparse is a semantic parser of source files: it's neither a compiler
(although it could be used as a front-end for one) nor is it a
preprocessor (although it contains as a part of it a preprocessing
phase).

It is meant to be a small - and simple - library. Scanty and meager,
and partly because of that easy to use. It has one mission in life:
create a semantic parse tree for some arbitrary user for further
analysis. It's not a tokenizer, nor is it some generic context-free
parser. In fact, context (semantics) is what it's all about - figuring
out not just what the grouping of tokens are, but what the _types_ are
that the grouping implies.

%description -l pl.UTF-8
Sparse to analizator semantyczny plików źródłowych - nie jest to ani
kompilator (choć mógłby być używany jako frontend dla niego) ani
preprocesor (choć zawiera jako część fazę preprocesingu).

Sparse ma być małą i prostą biblioteką. Ledwie wystarczającą i
niewielką, i po części dlatego łatwą w użyciu. Ma jedno zadanie:
utworzyć drzewo semantyczne analizy do dowolnego późniejszego
wykorzystania. Nie jest to tokenizer ani żaden ogólny analizator
bezkontekstowy. Właściwie kontekst (semantyka) to wszystko co
istotne - przedstawianie nie tylko czym są grupowane tokeny, ale tego,
czym są _typy_ obejmowane przez grupowanie.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fpic" \
	LDFLAGS="%{rpmldflags}" \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ LICENSE README
%attr(755,root,root) %{_bindir}/*
%{_includedir}/%{name}
%{_libdir}/*.a
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/*
