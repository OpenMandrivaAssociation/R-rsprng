%global packname  rsprng
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.4
Release:          1
Summary:          R interface to SPRNG (Scalable Parallel Random Number Generators)
Group:            Sciences/Mathematics
License:          GPL version 2 or newer
URL:              None
Source0:          http://cran.r-project.org/src/contrib/Archive/rsprng/rsprng_0.4.tar.gz
BuildRequires:    R-devel texlive-collection-latex 
BuildRequires:    sprng-devel

%description
Provides interface to SPRNG 2.0 APIs, and examples and documentation for
its use.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
