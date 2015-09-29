#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-guard-minitest
Version  : 2.4.4
Release  : 4
URL      : https://rubygems.org/downloads/guard-minitest-2.4.4.gem
Source0  : https://rubygems.org/downloads/guard-minitest-2.4.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rdoc

%description
# Guard::Minitest
[![Gem Version](https://badge.fury.io/rb/guard-minitest.png)](http://badge.fury.io/rb/guard-minitest) [![Build Status](https://travis-ci.org/guard/guard-minitest.png?branch=master)](https://travis-ci.org/guard/guard-minitest) [![Dependency Status](https://gemnasium.com/guard/guard-minitest.png)](https://gemnasium.com/guard/guard-minitest) [![Code Climate](https://codeclimate.com/github/guard/guard-minitest.png)](https://codeclimate.com/github/guard/guard-minitest) [![Coverage Status](https://coveralls.io/repos/guard/guard-minitest/badge.png?branch=master)](https://coveralls.io/r/guard/guard-minitest)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n guard-minitest-2.4.4
gem spec %{SOURCE0} -l --ruby > rubygem-guard-minitest.gemspec

%build
gem build rubygem-guard-minitest.gemspec

%install
gem_dir=$(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .${gem_dir} \
--bindir .%{_bindir} \
guard-minitest-2.4.4.gem

mkdir -p %{buildroot}${gem_dir}
cp -pa .${gem_dir}/* \
%{buildroot}${gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/guard-minitest-2.4.4.gem
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Inspector/_join_for_glob-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Inspector/_test_file%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Inspector/_test_files_for_paths-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Inspector/all_test_files-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Inspector/cdesc-Inspector.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Inspector/clean-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Inspector/clean_all-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Inspector/clear_memoized_test_files-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Inspector/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Inspector/test_file_patterns-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Inspector/test_folders-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Notifier/cdesc-Notifier.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Notifier/guard_image-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Notifier/guard_message-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Notifier/notify-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Reporter/cdesc-Reporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Reporter/report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/_commander-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/_run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/_run_possibly_bundled_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/all_after_pass%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/all_env-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/all_paths%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/autorun%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/base_env-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/bundler%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/cdesc-Runner.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/cli_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/drb%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/drb_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/generate_env-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/generate_includes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/include_folders-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/inspector-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/minitest_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/parse_deprecated_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/relative_paths-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/ruby_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/rubygems%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/run_all-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/run_on_additions-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/run_on_modifications-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/run_on_removals-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/spring%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/spring_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/test_file_patterns-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/test_folders-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/zeus%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Runner/zeus_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Utils/cdesc-Utils.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Utils/minitest_version-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Utils/minitest_version_gte_5%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/Utils/minitest_version_gte_5_0_4%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/cdesc-Minitest.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/reload-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/run_all-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/run_on_additions-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/run_on_modifications-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/run_on_removals-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/runner-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/stop-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/Minitest/throw_on_failed_tests-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/MinitestVersion/cdesc-MinitestVersion.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Guard/cdesc-Guard.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/MiniTest/MiniTest/MiniTest/Unit/_run_anything-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/MiniTest/MiniTest/MiniTest/Unit/cdesc-Unit.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/MiniTest/MiniTest/MiniTest/cdesc-MiniTest.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/MiniTest/MiniTest/cdesc-MiniTest.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/MiniTest/cdesc-MiniTest.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/Minitest/cdesc-Minitest.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-minitest-2.4.4/ri/lib/guard/minitest/templates/page-Guardfile.ri
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/README.md
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/lib/guard/minitest.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/lib/guard/minitest/inspector.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/lib/guard/minitest/notifier.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/lib/guard/minitest/reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/lib/guard/minitest/reporters/old_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/lib/guard/minitest/runner.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/lib/guard/minitest/runners/old_runner.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/lib/guard/minitest/templates/Guardfile
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/lib/guard/minitest/utils.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/lib/guard/minitest/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-minitest-2.4.4/lib/minitest/guard_minitest_plugin.rb
/usr/lib64/ruby/gems/2.2.0/specifications/guard-minitest-2.4.4.gemspec
