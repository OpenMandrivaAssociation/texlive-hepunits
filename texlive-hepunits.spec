Name:		texlive-hepunits
Version:	1.1.1
Release:	1
Summary:	A set of units useful in high energy physics applications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hepunits
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepunits.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepunits.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Hepunits is a LaTeX package built on the SIunits package which
adds a collection of useful HEP units to the existing SIunits
set. These include the energy units \MeV, \GeV, \TeV and the
derived momentum and mass units \MeVoverc, \MeVovercsq and so
on.

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
%{_texmfdistdir}/tex/latex/hepunits/hepunits.sty
%doc %{_texmfdistdir}/doc/latex/hepunits/ChangeLog
%doc %{_texmfdistdir}/doc/latex/hepunits/README
%doc %{_texmfdistdir}/doc/latex/hepunits/hepunits.pdf
%doc %{_texmfdistdir}/doc/latex/hepunits/hepunits.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
