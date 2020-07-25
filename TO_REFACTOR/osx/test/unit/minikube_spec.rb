control 'MiniKube' do

  describe file('/usr/local/bin/minikube') do
    it { should exist }
  end

  describe bash('minikube version') do
    its('exit_status') { should eq 0 }
  end

end
