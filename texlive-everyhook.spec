%global tl_name everyhook
%global tl_revision 35675

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Hooks for standard TeX token lists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/everyhook
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/everyhook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/everyhook.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/everyhook.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package takes control of the six TeX token registers \everypar,
\everymath, \everydisplay, \everyhbox, \everyvbox and \everycr. Real
hooks for each of the registers may be installed using a stack like
interface. For backwards compatibility, each of the \everyX token lists
can be set without interfering with the hooks.

