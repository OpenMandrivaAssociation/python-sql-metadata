Name:		python-sql-metadata
Version:	3.0.1
Release:	1
Summary:	Uses sqlglot to parse SQL queries and extract metadata
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/sql-metadata/
Source0:	sql_metadata-3.0.1.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(sqlglot)
BuildArch:	noarch
%description
Uses sqlglot to parse SQL queries and extract metadata.

%files
%{py_sitedir}/*
