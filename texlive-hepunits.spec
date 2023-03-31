Name:		texlive-hepunits
Version:	54758
Release:	2
Summary:	A set of units useful in high energy physics applications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hepunits
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepunits.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepunits.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Hepunits is a LaTeX package built on the SIunits package which
adds a collection of useful HEP units to the existing SIunits
set. These include the energy units \MeV, \GeV, \TeV and the
derived momentum and mass units \MeVoverc, \MeVovercsq and so
on.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
