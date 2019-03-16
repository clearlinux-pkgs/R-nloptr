#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-nloptr
Version  : 1.2.1
Release  : 54
URL      : https://cran.r-project.org/src/contrib/nloptr_1.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/nloptr_1.2.1.tar.gz
Summary  : R Interface to NLopt
Group    : Development/Tools
License  : LGPL-2.1 LGPL-3.0 MIT zlib-acknowledgement
Requires: R-nloptr-lib = %{version}-%{release}
Requires: R-assertthat
Requires: R-inline
BuildRequires : R-assertthat
BuildRequires : R-inline
BuildRequires : buildreq-R
BuildRequires : nlopt-dev

%description
Solve optimization problems using an R interface to NLopt. NLopt is a 
    free/open-source library for nonlinear optimization, providing a common
    interface for a number of different free optimization routines available
    online as well as original implementations of various other algorithms.

%package lib
Summary: lib components for the R-nloptr package.
Group: Libraries

%description lib
lib components for the R-nloptr package.


%prep
%setup -q -c -n nloptr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538560108

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1538560108
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nloptr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nloptr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nloptr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library nloptr|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/nloptr/CITATION
/usr/lib64/R/library/nloptr/DESCRIPTION
/usr/lib64/R/library/nloptr/INDEX
/usr/lib64/R/library/nloptr/Meta/Rd.rds
/usr/lib64/R/library/nloptr/Meta/features.rds
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
/usr/lib64/R/library/nloptr/doc/nloptr.Rmd
/usr/lib64/R/library/nloptr/doc/nloptr.pdf
/usr/lib64/R/library/nloptr/help/AnIndex
/usr/lib64/R/library/nloptr/help/aliases.rds
/usr/lib64/R/library/nloptr/help/nloptr.rdb
/usr/lib64/R/library/nloptr/help/nloptr.rdx
/usr/lib64/R/library/nloptr/help/paths.rds
/usr/lib64/R/library/nloptr/html/00Index.html
/usr/lib64/R/library/nloptr/html/R.css
/usr/lib64/R/library/nloptr/include/nlopt.h
/usr/lib64/R/library/nloptr/include/nlopt.hpp
/usr/lib64/R/library/nloptr/include/nloptrAPI.h
/usr/lib64/R/library/nloptr/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/nloptr/libs/nloptr.so
/usr/lib64/R/library/nloptr/libs/nloptr.so.avx2
/usr/lib64/R/library/nloptr/libs/nloptr.so.avx512
