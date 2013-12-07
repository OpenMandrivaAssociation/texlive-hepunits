# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/hepunits
# catalog-date 2009-09-19 12:08:16 +0200
# catalog-license lppl
# catalog-version 1.1.1
Name:		texlive-hepunits
Version:	1.1.1
Release:	4
Summary:	A set of units useful in high energy physics applications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hepunits
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepunits.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepunits.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-2
+ Revision: 752543
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-1
+ Revision: 718612
- texlive-hepunits
- texlive-hepunits
- texlive-hepunits
- texlive-hepunits

