Summary:	Sparse is a semantic parser of source files
Name:		sparse
Version:	0.3
Release:	1
License:	GPL
Group:		Development/Debuggers
Source0:	http://kernel.org/pub/software/devel/sparse/dist/%{name}-%{version}.tar.gz
# Source0-md5:	daa548bb52f64f00498ad646e5786c0a
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

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fpic" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX="%{_prefix}" \
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
