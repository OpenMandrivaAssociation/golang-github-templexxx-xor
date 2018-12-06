# https://github.com/templexxx/xor
%global goipath github.com/templexxx/xor
%global tag     0.1.2

Name:           golang-github-templexxx-xor
Version:        0.1.2
Release:        4%{?dist}
Summary:        XOR code engine in pure Go
License:        MIT

%gometa

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}

BuildRequires:  golang(github.com/templexxx/cpufeat)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-4
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Wed Sep 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- First package for Fedora

