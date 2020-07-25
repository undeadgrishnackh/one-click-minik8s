control 'Brew' do
  describe file('/usr/local/bin/brew') do
    it { should exist }
  end

  #describe bash('brew update') do
  #  its('stdout') { should match /Already up-to-date./ }
  #  its('stderr') { should eq '' }
  #  its('exit_status') { should eq 0 }
  #end

  describe bash('brew doctor') do
    its('stdout') { should match /Your system is ready to brew./ }
    its('exit_status') { should eq 0 }
  end

end