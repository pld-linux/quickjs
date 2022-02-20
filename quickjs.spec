%define		ver	2021-03-27
Summary:	QuickJS Javascript Engine
Summary(pl.UTF-8):	Silnik Javascriptu QuickJS
Name:		quickjs
Version:	20210327
Release:	3
License:	MIT
Group:		Libraries
Source0:	https://bellard.org/quickjs/%{name}-%{ver}.tar.xz
# Source0-md5:	135182a626aa0c87a49aa2bf58fd39bf
Patch0:		rpmpldcflags.patch
Patch1:		q.diff
URL:		https://bellard.org/quickjs/
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.583
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
	prefix="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	STRIP=true \
	prefix="%{_prefix}"

%{__mv} $RPM_BUILD_ROOT/{%{_prefix}/lib,%{_libdir}}/%{name}

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
