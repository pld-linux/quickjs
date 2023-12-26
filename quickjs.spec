%define		ver	2023-12-09
Summary:	QuickJS Javascript Engine
Summary(pl.UTF-8):	Silnik Javascriptu QuickJS
Name:		quickjs
Version:	20231209
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://bellard.org/quickjs/%{name}-%{ver}.tar.xz
# Source0-md5:	c8d37b54826a11b893c3f5357636ee7d
Patch0:		rpmpldcflags.patch
Patch1:		q.diff
URL:		https://bellard.org/quickjs/
%ifnarch %arch_with_atomics64
BuildRequires:	libatomic-devel
%endif
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 2.025
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QuickJS is a small and embeddable Javascript engine. It supports the
ES2020 specification including modules, asynchronous generators,
proxies and BigInt. It supports mathematical extensions such as big
decimal float float numbers (BigDecimal), big binary floating point
numbers (BigFloat), and operator overloading.

%description -l pl.UTF-8
QuickJS jest małym osadzalnym silnikiem Javascriptu. Wspiera
specyfikację ES2020, w tym moduły, asynchroniczne generatory, proxy i
BigInt. Wspiera też rozszerzenia matematyczne, takie jak liczby
BigDecimal, BigFloat i przeciążenia operatorów.

%package devel
Summary:	Header files for QuickJS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki QuickJS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for QuickJS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki QuickJS.

%prep
%setup -q -n %{name}-%{ver}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	RPMPLDCFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags} %{rpmcflags}" \
%ifnarch %arch_with_atomics64
	EXTRA_LIBS="-latomic" \
%endif
	prefix="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	STRIP=true \
	prefix="%{_prefix}"

%if "%{_lib}" != "lib"
%{__mv} $RPM_BUILD_ROOT{%{_prefix}/lib,%{_libdir}}/%{name}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qjs
%attr(755,root,root) %{_bindir}/qjsc
%attr(755,root,root) %{_bindir}/qjscalc

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libquickjs.a
%{_libdir}/%{name}/libquickjs.lto.a
%{_includedir}/%{name}
