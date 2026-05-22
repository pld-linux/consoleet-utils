Summary:	Consoleet utilities
Summary(pl.UTF-8):	Narzędzia Consoleet
Name:		consoleet-utils
Version:	1.11
Release:	1
License:	GPL v3+
Group:		Applications/Console
Source0:	https://inai.de/files/consoleet/%{name}-%{version}.tar.zst
# Source0-md5:	f5677f4288eeaf28543e2843c7626fa9
URL:		https://inai.de/projects/consoleet/
BuildRequires:	babl-devel >= 0.1
BuildRequires:	eigen3 >= 3
BuildRequires:	libHX-devel >= 4.28
# -std=gnu++20
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.31
BuildRequires:	zstd
Requires:	libHX >= 4.28
Conflicts:	hxtools < 20221120
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Consoleet is an umbrella name for endeavours surrounding text-oriented
consoles, bitmap fonts and otherwise, color considerations, and
generally retro look-and-feel.

%description -l pl.UTF-8
Consoleet to ogólna nazwa skupiająca prace związane z konsolami
tekstowymi, fontami bitmapowymi oraz, z innej strony, kolorami oraz
wyglądem i zachowaniem retro.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cp437table
%attr(755,root,root) %{_bindir}/palcomp
%attr(755,root,root) %{_bindir}/unicode_table
%attr(755,root,root) %{_bindir}/vfontas
%{_datadir}/consoleet-utils
%{_mandir}/man1/palcomp.1*
%{_mandir}/man1/vfontas.1*
