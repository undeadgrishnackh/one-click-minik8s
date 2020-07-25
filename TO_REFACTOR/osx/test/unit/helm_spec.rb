control 'Helm' do

  describe file('/usr/local/bin/helm') do
    it { should exist }
  end

  describe bash('helm version --client') do
    its('exit_status') { should eq 0 }
  end
end