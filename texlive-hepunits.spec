%global tl_name hepunits
%global tl_revision 54758

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.0
Release:	%{tl_revision}.1
Summary:	A set of units useful in high energy physics applications
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hepunits
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hepunits.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hepunits.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hepunits is a LaTeX package built on the SIunits package which adds a
collection of useful HEP units to the existing SIunits set. These
include the energy units \MeV, \GeV, \TeV and the derived momentum and
mass units \MeVoverc, \MeVovercsq and so on.

