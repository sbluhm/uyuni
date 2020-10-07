#
# Copyright (c) 2019 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           susemanager-nodejs-sdk-devel
Version:        4.2.1
Release:        1%{?dist}

License:        Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT and CC-BY-3.0 and ISC and SUSE-Public-Domain and WTFPL

Summary:        Node.js software used by SUSE Manager at build time
Url:            https://www.suse.com/products/suse-manager
Group:          Development/Languages/Other

Source0:        https://github.com/uyuni-project/uyuni/archive/%{name}-%{version}-1.tar.gz
Source1:        susemanager-nodejs-modules.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  nodejs-packaging

# Converted bundle(nodejs-*) to npm(*) to show that this is included. This messy package is required for build only.
Provides:      npm(acorn) = 5.7.4
Provides:      npm(ajv) = 6.12.0
Provides:      npm(ajv) = 6.12.4
Provides:      npm(ajv-keywords) = 3.5.2
Provides:      npm(ansi-regex) = 4.1.0
Provides:      npm(braces) = 3.0.2
Provides:      npm(cacache) = 15.0.5
Provides:      npm(chownr) = 2.0.0
Provides:      npm(csstype) = 2.6.10
Provides:      npm(debug) = 4.1.1
Provides:      npm(define-property) = 0.2.5
Provides:      npm(define-property) = 1.0.0
Provides:      npm(doctrine) = 2.1.0
Provides:      npm(doctrine) = 3.0.0
Provides:      npm(dom-helpers) = 5.1.4
Provides:      npm(domelementtype) = 2.0.1
Provides:      npm(emojis-list) = 3.0.0
Provides:      npm(enhanced-resolve) = 4.1.1
Provides:      npm(entities) = 2.0.0
Provides:      npm(esprima) = 3.1.3
Provides:      npm(extend-shallow) = 2.0.1
Provides:      npm(extsprintf) = 1.4.0
Provides:      npm(fast-deep-equal) = 3.1.1
Provides:      npm(fill-range) = 7.0.1
Provides:      npm(find-cache-dir) = 0.1.1
Provides:      npm(find-cache-dir) = 3.3.1
Provides:      npm(find-up) = 1.1.2
Provides:      npm(find-up) = 3.0.0
Provides:      npm(find-up) = 4.1.0
Provides:      npm(glob-parent) = 3.1.0
Provides:      npm(global-modules) = 1.0.0
Provides:      npm(global-prefix) = 1.0.2
Provides:      npm(has-value) = 0.3.1
Provides:      npm(has-values) = 0.1.4
Provides:      npm(iconv-lite) = 0.4.24
Provides:      npm(ignore) = 5.1.8
Provides:      npm(inherits) = 2.0.1
Provides:      npm(inherits) = 2.0.3
Provides:      npm(is-accessor-descriptor) = 0.1.6
Provides:      npm(is-data-descriptor) = 0.1.4
Provides:      npm(is-descriptor) = 0.1.6
Provides:      npm(is-extendable) = 0.1.1
Provides:      npm(is-glob) = 3.1.0
Provides:      npm(is-number) = 7.0.0
Provides:      npm(isobject) = 2.1.0
Provides:      npm(jsesc) = 0.5.0
Provides:      npm(json5) = 1.0.1
Provides:      npm(json5) = 2.1.3
Provides:      npm(kind-of) = 3.2.2
Provides:      npm(kind-of) = 4.0.0
Provides:      npm(kind-of) = 5.1.0
Provides:      npm(load-json-file) = 4.0.0
Provides:      npm(loader-utils) = 2.0.0
Provides:      npm(locate-path) = 3.0.0
Provides:      npm(locate-path) = 5.0.0
Provides:      npm(lru-cache) = 6.0.0
Provides:      npm(make-dir) = 3.1.0
Provides:      npm(memory-fs) = 0.5.0
Provides:      npm(micromatch) = 4.0.2
Provides:      npm(mimic-fn) = 1.2.0
Provides:      npm(mkdirp) = 1.0.4
Provides:      npm(ms) = 2.1.2
Provides:      npm(normalize-path) = 2.1.1
Provides:      npm(p-limit) = 1.3.0
Provides:      npm(p-limit) = 2.2.1
Provides:      npm(p-locate) = 3.0.0
Provides:      npm(p-locate) = 4.1.0
Provides:      npm(p-try) = 1.0.0
Provides:      npm(parse-json) = 4.0.0
Provides:      npm(parse-json) = 5.0.0
Provides:      npm(path-browserify) = 0.0.1
Provides:      npm(path-exists) = 2.1.0
Provides:      npm(path-exists) = 4.0.0
Provides:      npm(path-type) = 3.0.0
Provides:      npm(path-type) = 4.0.0
Provides:      npm(pify) = 2.3.0
Provides:      npm(pify) = 3.0.0
Provides:      npm(pkg-dir) = 1.0.0
Provides:      npm(pkg-dir) = 3.0.0
Provides:      npm(pkg-dir) = 4.2.0
Provides:      npm(pump) = 2.0.1
Provides:      npm(punycode) = 1.3.2
Provides:      npm(punycode) = 2.1.1
Provides:      npm(react-transition-group) = 4.4.1
Provides:      npm(read-pkg) = 3.0.0
Provides:      npm(read-pkg-up) = 4.0.0
Provides:      npm(readable-stream) = 2.3.6
Provides:      npm(readable-stream) = 3.4.0
Provides:      npm(regenerator-runtime) = 0.11.1
Provides:      npm(regenerator-runtime) = 0.13.5
Provides:      npm(resolve) = 1.1.7
Provides:      npm(resolve-from) = 3.0.0
Provides:      npm(rimraf) = 2.6.3
Provides:      npm(rimraf) = 3.0.2
Provides:      npm(safe-buffer) = 5.1.2
Provides:      npm(safe-buffer) = 5.2.0
Provides:      npm(schema-utils) = 2.6.5
Provides:      npm(schema-utils) = 2.7.1
Provides:      npm(semver) = 6.3.0
Provides:      npm(semver) = 7.0.0
Provides:      npm(slash) = 3.0.0
Provides:      npm(source-map) = 0.6.1
Provides:      npm(source-map) = 0.7.3
Provides:      npm(spdx-expression-parse) = 3.0.0
Provides:      npm(ssri) = 8.0.0
Provides:      npm(string-width) = 3.1.0
Provides:      npm(string_decoder) = 1.1.1
Provides:      npm(strip-ansi) = 5.2.0
Provides:      npm(supports-color) = 5.5.0
Provides:      npm(to-regex-range) = 5.0.1
Provides:      npm(tough-cookie) = 2.4.3
Provides:      npm(util) = 0.10.3
Provides:      npm(whatwg-url) = 7.1.0
Provides:      npm(wrap-ansi) = 5.1.0
Provides:      npm(yallist) = 4.0.0
Provides:      npm(yargs) = 13.3.2


# Manually adding versions as rpmbuild did not seem to pick those up as bundles:

Provides:       npm(@babel/plugin-transform-modules-amd) = 7.7.5
Provides:       npm(@babel/plugin-proposal-class-properties) = 7.7.4
Provides:       npm(@babel/plugin-transform-react-jsx) = 7.7.7
Provides:       npm(@babel/plugin-transform-exponentiation-operator) = 7.7.4
Provides:       npm(@babel/helper-regex) = 7.5.5
Provides:       npm(@babel/plugin-transform-for-of) = 7.7.4
Provides:       npm(@babel/plugin-transform-spread) = 7.7.4
Provides:       npm(@babel/plugin-syntax-optional-catch-binding) = 7.7.4
Provides:       npm(@babel/plugin-proposal-optional-catch-binding) = 7.7.4
Provides:       npm(@babel/types) = 7.7.4
Provides:       npm(@babel/plugin-transform-block-scoped-functions) = 7.7.4
Provides:       npm(@babel/plugin-transform-computed-properties) = 7.7.4
Provides:       npm(@babel/plugin-proposal-unicode-property-regex) = 7.7.7
Provides:       npm(@babel/helper-split-export-declaration) = 7.7.4
Provides:       npm(@babel/plugin-transform-typeof-symbol) = 7.7.4
Provides:       npm(@babel/plugin-syntax-json-strings) = 7.7.4
Provides:       npm(@babel/plugin-proposal-json-strings) = 7.7.4
Provides:       npm(@babel/helper-replace-supers) = 7.7.4
Provides:       npm(@babel/runtime) = 7.7.7
Provides:       npm(@babel/plugin-transform-modules-commonjs) = 7.7.5
Provides:       npm(@babel/plugin-transform-react-jsx-source) = 7.7.4
Provides:       npm(@babel/highlight) = 7.5.0
Provides:       npm(@babel/plugin-transform-classes) = 7.7.4
Provides:       npm(@babel/plugin-proposal-async-generator-functions) = 7.7.4
Provides:       npm(@babel/helper-call-delegate) = 7.7.4
Provides:       npm(@babel/plugin-syntax-jsx) = 7.7.4
Provides:       npm(@babel/parser) = 7.7.7
Provides:       npm(@babel/plugin-transform-sticky-regex) = 7.7.4
Provides:       npm(@babel/helpers) = 7.7.4
Provides:       npm(@babel/plugin-transform-duplicate-keys) = 7.7.4
Provides:       npm(@babel/runtime-corejs3) = 7.7.7
Provides:       npm(@babel/plugin-transform-named-capturing-groups-regex) = 7.7.4
Provides:       npm(@babel/template) = 7.7.4
Provides:       npm(@babel/polyfill) = 7.7.0
Provides:       npm(@babel/helper-simple-access) = 7.7.4
Provides:       npm(@babel/plugin-transform-dotall-regex) = 7.7.7
Provides:       npm(@babel/helper-plugin-utils) = 7.0.0
Provides:       npm(@babel/plugin-transform-flow-strip-types) = 7.7.4
Provides:       npm(@babel/plugin-syntax-async-generators) = 7.7.4
Provides:       npm(@babel/plugin-transform-new-target) = 7.7.4
Provides:       npm(@babel/plugin-transform-arrow-functions) = 7.7.4
Provides:       npm(@babel/plugin-proposal-object-rest-spread) = 7.7.7
Provides:       npm(@babel/preset-env) = 7.7.7
Provides:       npm(@babel/plugin-syntax-dynamic-import) = 7.7.4
Provides:       npm(@babel/plugin-proposal-dynamic-import) = 7.7.4
Provides:       npm(@babel/helper-module-imports) = 7.7.4
Provides:       npm(@babel/plugin-transform-react-display-name) = 7.7.4
Provides:       npm(@babel/plugin-transform-reserved-words) = 7.7.4
Provides:       npm(@babel/plugin-transform-literals) = 7.7.4
Provides:       npm(@babel/plugin-syntax-top-level-await) = 7.7.4
Provides:       npm(@babel/helper-module-transforms) = 7.7.5
Provides:       npm(@babel/plugin-transform-react-jsx-self) = 7.7.4
Provides:       npm(@babel/helper-optimise-call-expression) = 7.7.4
Provides:       npm(@babel/preset-react) = 7.7.4
Provides:       npm(@babel/plugin-transform-async-to-generator) = 7.7.4
Provides:       npm(@babel/helper-builder-binary-assignment-operator-visitor) = 7.7.4
Provides:       npm(@babel/plugin-transform-member-expression-literals) = 7.7.4
Provides:       npm(@babel/plugin-transform-destructuring) = 7.7.4
Provides:       npm(@babel/traverse/node_modules/ms) = 2.1.2
Provides:       npm(@babel/traverse/node_modules/debug) = 4.1.1
Provides:       npm(@babel/traverse) = 7.7.4
Provides:       npm(@babel/plugin-transform-unicode-regex) = 7.7.4
Provides:       npm(@babel/plugin-syntax-flow) = 7.7.4
Provides:       npm(@babel/plugin-transform-object-super) = 7.7.4
Provides:       npm(@babel/helper-define-map) = 7.7.4
Provides:       npm(@babel/helper-annotate-as-pure) = 7.7.4
Provides:       npm(@babel/helper-create-class-features-plugin) = 7.7.4
Provides:       npm(@babel/helper-remap-async-to-generator) = 7.7.4
Provides:       npm(@babel/helper-create-regexp-features-plugin) = 7.7.4
Provides:       npm(@babel/helper-hoist-variables) = 7.7.4
Provides:       npm(@babel/preset-flow) = 7.7.4
Provides:       npm(@babel/helper-member-expression-to-functions) = 7.7.4
Provides:       npm(@babel/plugin-transform-parameters) = 7.7.7
Provides:       npm(@babel/plugin-syntax-object-rest-spread) = 7.7.4
Provides:       npm(@babel/plugin-transform-template-literals) = 7.7.4
Provides:       npm(@babel/plugin-transform-function-name) = 7.7.4
Provides:       npm(@babel/generator) = 7.7.7
Provides:       npm(@babel/core/node_modules/ms) = 2.1.2
Provides:       npm(@babel/core/node_modules/debug) = 4.1.1
Provides:       npm(@babel/core) = 7.7.7
Provides:       npm(@babel/plugin-transform-modules-systemjs) = 7.7.4
Provides:       npm(@babel/plugin-transform-regenerator) = 7.7.5
Provides:       npm(@babel/helper-explode-assignable-expression) = 7.7.4
Provides:       npm(@babel/helper-wrap-function) = 7.7.4
Provides:       npm(@babel/helper-get-function-arity) = 7.7.4
Provides:       npm(@babel/helper-function-name) = 7.7.4
Provides:       npm(@babel/plugin-transform-property-literals) = 7.7.4
Provides:       npm(@babel/helper-builder-react-jsx) = 7.7.4
Provides:       npm(@babel/plugin-transform-modules-umd) = 7.7.4
Provides:       npm(@babel/code-frame) = 7.5.5
Provides:       npm(@babel/plugin-transform-shorthand-properties) = 7.7.4
Provides:       npm(@babel/plugin-transform-block-scoping) = 7.7.4

Provides:      npm(@emotion/cache) = 10.0.27
Provides:      npm(@emotion/core) = 10.0.27
Provides:      npm(@emotion/css) = 10.0.27
Provides:      npm(@emotion/hash) = 0.7.4
Provides:      npm(@emotion/memoize) = 0.7.4
Provides:      npm(@emotion/serialize) = 0.11.15
Provides:      npm(@emotion/sheet) = 0.9.4
Provides:      npm(@emotion/stylis) = 0.8.5
Provides:      npm(@emotion/unitless) = 0.7.5
Provides:      npm(@emotion/utils) = 0.11.3
Provides:      npm(@emotion/weak-memoize) = 0.2.5

Provides:      npm(@types/babel__core) = 7.1.3
Provides:      npm(@types/babel__generator) = 7.6.1
Provides:      npm(@types/babel__template) = 7.0.2
Provides:      npm(@types/babel__traverse) = 7.0.8
Provides:      npm(@types/domhandler) = 2.4.1
Provides:      npm(@types/istanbul-lib-coverage) = 2.0.1
Provides:      npm(@types/istanbul-lib-report) = 1.1.1
Provides:      npm(@types/istanbul-reports) = 1.1.1
Provides:      npm(@types/json-schema) = 7.0.6
Provides:      npm(@types/parse-json) = 4.0.0
Provides:      npm(@types/stack-utils) = 1.0.1
Provides:      npm(@types/yargs) = 13.0.4
Provides:      npm(@types/yargs-parser) = 13.1.0


%{!?nodejs_sitelib:%define nodejs_sitelib %{_prefix}/lib/node_modules}
%{!?nodejs_modulesdir:%define nodejs_modulesdir %{nodejs_sitelib}}


%description
This package contains Node.js software needed by SUSE Manager at build time.

%global debug_package %{nil}

%prep
%setup -q -n uyuni-%{name}-%{version}-1
tar xfv %{S:1}

%build
find . -type f -exec sed -i -e 's/#!\/usr\/bin\/env node/#!\/usr\/bin\/node/g' {} \;

%install
mkdir -p %{buildroot}%{nodejs_sitelib}
mkdir -p %{buildroot}%{_bindir}
cp -pr node_modules/* %{buildroot}%{nodejs_sitelib}

chmod +x %{buildroot}%{nodejs_sitelib}/webpack/bin/*
ln -sf %{nodejs_sitelib}/webpack/bin/webpack.js %{buildroot}%{_bindir}/webpack

find %{buildroot}%{nodejs_sitelib} -name "*~" -delete
find %{buildroot}%{nodejs_sitelib} -name ".*" -type d -exec rm -rf {} +
find %{buildroot}%{nodejs_sitelib} -name ".*" -delete
%fdupes %{buildroot}%{nodejs_sitelib}

%files
%defattr(-,root,root,-)
%dir %{nodejs_modulesdir}
%{nodejs_sitelib}/*
%{_bindir}/*

%changelog
