# revision 21298
# category Package
# catalog-ctan /macros/latex/contrib/everyhook
# catalog-date 2011-02-04 11:55:08 +0100
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-everyhook
Version:	1.1
Release:	1
Summary:	Hooks for standard TeX token lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/everyhook
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everyhook.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everyhook.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everyhook.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package takes control of the six TeX token registers
\everypar, \everymath, \everydisplay, \everyhbox, \everyvbox
and \everycr. Real hooks for each of the registers may be
installed using a stack like interface. For backwards
compatibility, each of the \everyX token lists can be set
without interfering with the hooks.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/everyhook/everyhook.sty
%doc %{_texmfdistdir}/doc/latex/everyhook/README
%doc %{_texmfdistdir}/doc/latex/everyhook/everyhook.pdf
#- source
%doc %{_texmfdistdir}/source/latex/everyhook/everyhook.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
