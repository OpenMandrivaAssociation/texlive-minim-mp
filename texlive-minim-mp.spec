%global tl_name minim-mp
%global tl_revision 78415

Name:		texlive-%{tl_name}
Epoch:		1
Version:	20251.7
Release:	%{tl_revision}.1
Summary:	Low-level mplib integration for LuaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/minim-mp
License:	eupl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minim-mp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minim-mp.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers low-level mplib integration for LuaLaTeX and plain
LuaTeX. It is designed with the purpose of being easy to extend. The use
of multiple simultaneous MetaPost instances is supported, as well as
running TeX or Lua code from within MetaPost. With the included minim-mp
and minim-lamp format files, you can even use Lua(La)TeX as a stand-
alone MetaPost compiler.

