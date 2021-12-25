%define		ver	2021-03-27
Summary:	QuickJS Javascript Engine
Summary(pl.UTF-8):	Silnik Javascriptu QuickJS
Name:		quickjs
Version:	20210327
Release:	2
License:	MIT
Group:		Libraries
Source0:	https://bellard.org/%{name}/%{name}-%{ver}.tar.xz 
# Source0-md5:	135182a626aa0c87a49aa2bf58fd39bf
Patch0:		rpmpldcflags.patch
Patch1:		q.diff
URL:		https://bellard.org/quickjs/
BuildRequires:	make
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	rpmbuild(macros) >= 1.583

%description
QuickJS is a small and embeddable Javascript engine. It supports the
ES2020 specification including modules, asynchronous generators, proxies and BigInt.
It supports mathematical extensions such as big decimal float float
numbers (BigDecimal), big binary floating point numbers (BigFloat),
and operator overloading.

%description -l pl.UTF-8
QuickJS jest małym osadzalnym silnikiem Javascriptu. Wspiera specyfikację
ES2020, w tym moduły, asynchroniczne generatory, proxy i BigInt.
Wspiera też rozszerzenia matematyczne, takie jak liczby BigDecimal, BigFloat
i przeciążenia operatorów.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q -n %{name}-%{ver}
%patch0 -p1
%patch1 -p1

%build
%{__make} RPMPLDCFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	prefix="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/%{name}

%files devel
%defattr(644,root,root,755)
%doc doc
%{_includedir}/%{name}
