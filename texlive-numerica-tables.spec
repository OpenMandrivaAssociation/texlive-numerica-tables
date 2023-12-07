Name:		texlive-numerica-tables
Version:	68193
Release:	1
Summary:	Create multi-column tables of mathematical functions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/numerica-tables
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numerica-tables.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numerica-tables.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a command to create possibly multi-column
tables of mathematical function values. Key = value settings
produce a wide variety of table styles consistent with the
booktabs package (required). Also required are the packages
numerica(v.2), l3kernel, l3packages, amsmath and mathtools.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/numerica-tables
%doc %{_texmfdistdir}/doc/latex/numerica-tables

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
