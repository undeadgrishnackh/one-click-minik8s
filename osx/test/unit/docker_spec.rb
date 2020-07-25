control 'Docker' do

  describe file('/usr/local/bin/docker') do
    it { should exist }
  end

  # Check the Docker engine is running
  describe bash('docker ps') do
    its('exit_status') { should eq 0 }
  end

  describe bash('docker run --name hello-world-test hello-world') do
    its('stdout') { should match /Hello from Docker/ }
    its('exit_status') { should eq 0 }
  end

  describe bash('docker container rm hello-world-test') do
    its('stdout') { should match /hello-world/ }
    its('exit_status') { should eq 0 }
  end

end