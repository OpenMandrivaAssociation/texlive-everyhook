Name:		texlive-everyhook
Version:	35675
Release:	1
Summary:	Hooks for standard TeX token lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/everyhook
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everyhook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everyhook.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everyhook.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package takes control of the six TeX token registers
\everypar, \everymath, \everydisplay, \everyhbox, \everyvbox
and \everycr. Real hooks for each of the registers may be
installed using a stack like interface. For backwards
compatibility, each of the \everyX token lists can be set
without interfering with the hooks.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/everyhook
%doc %{_texmfdistdir}/doc/latex/everyhook
#- source
%doc %{_texmfdistdir}/source/latex/everyhook

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
