Name:		texlive-minim-mp
Version:	70885
Release:	1
Summary:	Low-level mplib integration for LuaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/minim-mp
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minim-mp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minim-mp.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers low-level mplib integration for plain
LuaTeX and is designed with the purpose of being easy to
extend. The use of multiple simultaneous MetaPost instances is
supported, as well as running TeX or lua code from within
MetaPost. With the included minim-mp format file, you can even
use LuaTeX as a stand-alone MetaPost compiler.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/minim-mp
%{_texmfdistdir}/metapost/minim-mp
%doc %{_texmfdistdir}/doc/luatex/minim-mp

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
