Name: terraform
Version: 0.11.8
Release: 1%{?dist}
Summary: Terraform is a tool for building, changing, and combining infrastructure safely and efficiently.
Group: Development/Tools
License: MPLv2.0
URL: https://www.terraform.io/

Source0: https://releases.hashicorp.com/terraform/%{version}/terraform_%{version}_linux_amd64.zip

%description
Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions.

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
unzip -o %{SOURCE0} -d %{buildroot}%{_bindir}

%files
%{_bindir}/*

%changelog
* Mon Aug 27 2018 Eduardo Minguez <edu@redhat.com> - 0.11.8-1
- Bump to version 0.11.8

* Tue Dec 19 2017 Eduardo Minguez <edu@redhat.com> - 0.11.1-1
- First version
