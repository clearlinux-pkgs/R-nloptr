#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-nloptr
Version  : 1.0.4
Release  : 25
URL      : http://cran.r-project.org/src/contrib/nloptr_1.0.4.tar.gz
Source0  : http://cran.r-project.org/src/contrib/nloptr_1.0.4.tar.gz
Summary  : R interface to NLopt
Group    : Development/Tools
License  : LGPL-3.0
Requires: R-nloptr-lib
BuildRequires : clr-R-helpers
BuildRequires : nlopt-dev

%description
# nloptr
[![Build Status](https://travis-ci.org/jyypma/nloptr.svg?branch=master)](https://travis-ci.org/jyypma/nloptr)

%package lib
Summary: lib components for the R-nloptr package.
Group: Libraries

%description lib
lib components for the R-nloptr package.


%prep
%setup -q -c -n nloptr

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library nloptr
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library nloptr


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/nloptr/CITATION
/usr/lib64/R/library/nloptr/DESCRIPTION
/usr/lib64/R/library/nloptr/INDEX
/usr/lib64/R/library/nloptr/Meta/Rd.rds
/usr/lib64/R/library/nloptr/Meta/hsearch.rds
/usr/lib64/R/library/nloptr/Meta/links.rds
/usr/lib64/R/library/nloptr/Meta/nsInfo.rds
/usr/lib64/R/library/nloptr/Meta/package.rds
/usr/lib64/R/library/nloptr/Meta/vignette.rds
/usr/lib64/R/library/nloptr/NAMESPACE
/usr/lib64/R/library/nloptr/R/nloptr
/usr/lib64/R/library/nloptr/R/nloptr.rdb
/usr/lib64/R/library/nloptr/R/nloptr.rdx
/usr/lib64/R/library/nloptr/doc/index.html
/usr/lib64/R/library/nloptr/doc/nloptr.R
/usr/lib64/R/library/nloptr/doc/nloptr.Rnw
/usr/lib64/R/library/nloptr/doc/nloptr.pdf
/usr/lib64/R/library/nloptr/help/AnIndex
/usr/lib64/R/library/nloptr/help/aliases.rds
/usr/lib64/R/library/nloptr/help/nloptr.rdb
/usr/lib64/R/library/nloptr/help/nloptr.rdx
/usr/lib64/R/library/nloptr/help/paths.rds
/usr/lib64/R/library/nloptr/html/00Index.html
/usr/lib64/R/library/nloptr/html/R.css
/usr/lib64/R/library/nloptr/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/nloptr/libs/nloptr.so
