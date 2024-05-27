#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 6fa3d52
#
Name     : nlohmann-json
Version  : 3.11.3
Release  : 1
URL      : https://github.com/nlohmann/json/archive/refs/tags/v3.11.3.tar.gz
Source0  : https://github.com/nlohmann/json/archive/refs/tags/v3.11.3.tar.gz
Source1  : https://github.com/nlohmann/json_test_data/archive/refs/tags/v3.1.0.tar.gz
Summary  : JSON for Modern C++
Group    : Development/Tools
License  : MIT
Requires: nlohmann-json-data = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : ninja
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![JSON for Modern C++](docs/json.gif)](https://github.com/nlohmann/json/releases)

%package data
Summary: data components for the nlohmann-json package.
Group: Data

%description data
data components for the nlohmann-json package.


%package dev
Summary: dev components for the nlohmann-json package.
Group: Development
Requires: nlohmann-json-data = %{version}-%{release}
Provides: nlohmann-json-devel = %{version}-%{release}
Requires: nlohmann-json = %{version}-%{release}

%description dev
dev components for the nlohmann-json package.


%prep
%setup -q -n json-3.11.3
cd %{_builddir}
tar xf %{_sourcedir}/v3.1.0.tar.gz
cd %{_builddir}/json-3.11.3
mkdir -p ./json_test_data
cp -r %{_builddir}/json_test_data-3.1.0/* %{_builddir}/json-3.11.3/./json_test_data

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716806840
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -G Ninja \
-DJSON_BuildTests:BOOL=ON \
-DJSON_Install:BOOL=ON \
-DJSON_MultipleHeaders:BOOL=ON \
-DJSON_TestDataDirectory:STRING=./json_test_data
ninja  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1716806840
rm -rf %{buildroot}
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%ninja_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*

%files dev
%defattr(-,root,root,-)
/usr/include/nlohmann/adl_serializer.hpp
/usr/include/nlohmann/byte_container_with_subtype.hpp
/usr/include/nlohmann/detail/abi_macros.hpp
/usr/include/nlohmann/detail/conversions/from_json.hpp
/usr/include/nlohmann/detail/conversions/to_chars.hpp
/usr/include/nlohmann/detail/conversions/to_json.hpp
/usr/include/nlohmann/detail/exceptions.hpp
/usr/include/nlohmann/detail/hash.hpp
/usr/include/nlohmann/detail/input/binary_reader.hpp
/usr/include/nlohmann/detail/input/input_adapters.hpp
/usr/include/nlohmann/detail/input/json_sax.hpp
/usr/include/nlohmann/detail/input/lexer.hpp
/usr/include/nlohmann/detail/input/parser.hpp
/usr/include/nlohmann/detail/input/position_t.hpp
/usr/include/nlohmann/detail/iterators/internal_iterator.hpp
/usr/include/nlohmann/detail/iterators/iter_impl.hpp
/usr/include/nlohmann/detail/iterators/iteration_proxy.hpp
/usr/include/nlohmann/detail/iterators/iterator_traits.hpp
/usr/include/nlohmann/detail/iterators/json_reverse_iterator.hpp
/usr/include/nlohmann/detail/iterators/primitive_iterator.hpp
/usr/include/nlohmann/detail/json_custom_base_class.hpp
/usr/include/nlohmann/detail/json_pointer.hpp
/usr/include/nlohmann/detail/json_ref.hpp
/usr/include/nlohmann/detail/macro_scope.hpp
/usr/include/nlohmann/detail/macro_unscope.hpp
/usr/include/nlohmann/detail/meta/call_std/begin.hpp
/usr/include/nlohmann/detail/meta/call_std/end.hpp
/usr/include/nlohmann/detail/meta/cpp_future.hpp
/usr/include/nlohmann/detail/meta/detected.hpp
/usr/include/nlohmann/detail/meta/identity_tag.hpp
/usr/include/nlohmann/detail/meta/is_sax.hpp
/usr/include/nlohmann/detail/meta/std_fs.hpp
/usr/include/nlohmann/detail/meta/type_traits.hpp
/usr/include/nlohmann/detail/meta/void_t.hpp
/usr/include/nlohmann/detail/output/binary_writer.hpp
/usr/include/nlohmann/detail/output/output_adapters.hpp
/usr/include/nlohmann/detail/output/serializer.hpp
/usr/include/nlohmann/detail/string_concat.hpp
/usr/include/nlohmann/detail/string_escape.hpp
/usr/include/nlohmann/detail/value_t.hpp
/usr/include/nlohmann/json.hpp
/usr/include/nlohmann/json_fwd.hpp
/usr/include/nlohmann/ordered_map.hpp
/usr/include/nlohmann/thirdparty/hedley/hedley.hpp
/usr/include/nlohmann/thirdparty/hedley/hedley_undef.hpp
/usr/lib64/pkgconfig/nlohmann_json.pc
