#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v12
# autospec commit: 381dfd8
#
Name     : R-nloptr
Version  : 2.1.1
Release  : 91
URL      : https://cran.r-project.org/src/contrib/nloptr_2.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/nloptr_2.1.1.tar.gz
Summary  : R Interface to NLopt
Group    : Development/Tools
License  : LGPL-3.0+
Requires: R-nloptr-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : nlopt-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n nloptr
pushd ..
cp -a nloptr buildavx2
popd
pushd ..
cp -a nloptr buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719331649

%install
export SOURCE_DATE_EPOCH=1719331649
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/nloptr/NEWS.md
/usr/lib64/R/library/nloptr/R/nloptr
/usr/lib64/R/library/nloptr/R/nloptr.rdb
/usr/lib64/R/library/nloptr/R/nloptr.rdx
/usr/lib64/R/library/nloptr/doc/index.html
/usr/lib64/R/library/nloptr/doc/nloptr.R
/usr/lib64/R/library/nloptr/doc/nloptr.Rmd
/usr/lib64/R/library/nloptr/doc/nloptr.html
/usr/lib64/R/library/nloptr/help/AnIndex
/usr/lib64/R/library/nloptr/help/aliases.rds
/usr/lib64/R/library/nloptr/help/figures/logo.png
/usr/lib64/R/library/nloptr/help/nloptr.rdb
/usr/lib64/R/library/nloptr/help/nloptr.rdx
/usr/lib64/R/library/nloptr/help/paths.rds
/usr/lib64/R/library/nloptr/html/00Index.html
/usr/lib64/R/library/nloptr/html/R.css
/usr/lib64/R/library/nloptr/include/nlopt.f
/usr/lib64/R/library/nloptr/include/nlopt.h
/usr/lib64/R/library/nloptr/include/nlopt.hpp
/usr/lib64/R/library/nloptr/include/nloptrAPI.h
/usr/lib64/R/library/nloptr/tests/tinytest.R
/usr/lib64/R/library/nloptr/tinytest/test-banana-global.R
/usr/lib64/R/library/nloptr/tinytest/test-banana.R
/usr/lib64/R/library/nloptr/tinytest/test-check.derivatives.R
/usr/lib64/R/library/nloptr/tinytest/test-derivative-checker.R
/usr/lib64/R/library/nloptr/tinytest/test-example.R
/usr/lib64/R/library/nloptr/tinytest/test-gradients.R
/usr/lib64/R/library/nloptr/tinytest/test-hs023.R
/usr/lib64/R/library/nloptr/tinytest/test-hs071.R
/usr/lib64/R/library/nloptr/tinytest/test-is.nloptr.R
/usr/lib64/R/library/nloptr/tinytest/test-nloptions.R
/usr/lib64/R/library/nloptr/tinytest/test-nloptr.R
/usr/lib64/R/library/nloptr/tinytest/test-nloptr.add.default.options.R
/usr/lib64/R/library/nloptr/tinytest/test-nloptr.print.options.R
/usr/lib64/R/library/nloptr/tinytest/test-options-maxtime.R
/usr/lib64/R/library/nloptr/tinytest/test-parameters.R
/usr/lib64/R/library/nloptr/tinytest/test-print.nloptr.R
/usr/lib64/R/library/nloptr/tinytest/test-simple.R
/usr/lib64/R/library/nloptr/tinytest/test-systemofeq.R
/usr/lib64/R/library/nloptr/tinytest/test-wrapper-auglag.R
/usr/lib64/R/library/nloptr/tinytest/test-wrapper-ccsaq.R
/usr/lib64/R/library/nloptr/tinytest/test-wrapper-cobyla.R
/usr/lib64/R/library/nloptr/tinytest/test-wrapper-direct.R
/usr/lib64/R/library/nloptr/tinytest/test-wrapper-global.R
/usr/lib64/R/library/nloptr/tinytest/test-wrapper-lbgfs.R
/usr/lib64/R/library/nloptr/tinytest/test-wrapper-mlsl.R
/usr/lib64/R/library/nloptr/tinytest/test-wrapper-mma.R
/usr/lib64/R/library/nloptr/tinytest/test-wrapper-nm.R
/usr/lib64/R/library/nloptr/tinytest/test-wrapper-slsqp.R
/usr/lib64/R/library/nloptr/tinytest/test-wrapper-tnewton.R
/usr/lib64/R/library/nloptr/tinytest/test-wrapper-varmetric.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/nloptr/libs/nloptr.so
/V4/usr/lib64/R/library/nloptr/libs/nloptr.so
/usr/lib64/R/library/nloptr/libs/nloptr.so
