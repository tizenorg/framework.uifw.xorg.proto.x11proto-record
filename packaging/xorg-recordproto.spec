Name:           xorg-recordproto
Version:        1.14.1
Release:        0
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          Development/System
Source0:        http://xorg.freedesktop.org/releases/individual/proto/recordproto-%{version}.tar.gz
Source1001:     packaging/xorg-recordproto.manifest
BuildRequires:  pkgconfig(xorg-macros)
Provides:       recordproto

%description
Description: %{summary}

%prep
%setup -q -n recordproto-%{version}

%build
cp %{SOURCE1001} .

%reconfigure --disable-shared

make %{?_smp_mflags}

%install
%make_install


%files
%manifest xorg-recordproto.manifest
%{_libdir}/pkgconfig/recordproto.pc
%{_includedir}/X11/extensions/recordstr.h
%{_includedir}/X11/extensions/recordconst.h
%{_includedir}/X11/extensions/recordproto.h
%{_docdir}/recordproto

