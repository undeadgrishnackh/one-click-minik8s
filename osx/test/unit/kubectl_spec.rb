control 'Kubectl' do

  describe file('/usr/local/bin/kubectl') do
    it { should exist }
  end

  describe bash('kubectl version --client') do
    its('exit_status') { should eq 0 }
  end

end