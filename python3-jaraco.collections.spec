#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	tests	# unit tests

Summary:	Models and classes to supplement the stdlib "collections" module
Summary(pl.UTF-8):	Modele i klasy uzupełniające moduł stdlib "collections"
Name:		python3-jaraco.collections
Version:	5.2.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jaraco.collections/
Source0:	https://files.pythonhosted.org/packages/source/j/jaraco.collections/jaraco_collections-%{version}.tar.gz
# Source0-md5:	57529f8464fb77efaf0398c4395dfca9
URL:		https://pypi.org/project/jaraco.collections/
BuildRequires:	python3-build
BuildRequires:	python3-coherent.licensed
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 1:77
BuildRequires:	python3-setuptools_scm >= 3.4.1
%if %{with tests}
BuildRequires:	python3-jaraco.text
BuildRequires:	python3-pytest >= 6
# lint only
#BuildRequires:	python3-pytest-checkdocs >= 2.4
#BuildRequires:	python3-pytest-cov
#BuildRequires:	python3-pytest-enabler >= 2.2
#BuildRequires:	python3-pytest-ruff >= 0.2.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	python3-furo
BuildRequires:	python3-jaraco.packaging >= 9.3
BuildRequires:	python3-jaraco.text
BuildRequires:	python3-jaraco.tidelift >= 1.4
BuildRequires:	python3-rst.linker >= 1.9
#BuildRequires:	python3-sphinx-lint
BuildRequires:	sphinx-pdg-3 >= 3.5
%endif
Requires:	python3-jaraco
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Models and classes to supplement the stdlib "collections" module.

%description -l pl.UTF-8
Modele i klasy uzupełniające moduł biblioteki standardowej
"collections".

%package apidocs
Summary:	API documentation for Python jaraco.collections module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona jaraco.collections
Group:		Documentation

%description apidocs
API documentation for Python jaraco.collections module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona jaraco.collections.

%prep
%setup -q -n jaraco_collections-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
sphinx-build-3 -b html docs docs/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS.rst README.rst SECURITY.md
%{py3_sitescriptdir}/jaraco/collections
%{py3_sitescriptdir}/jaraco_collections-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,*.html,*.js}
%endif
