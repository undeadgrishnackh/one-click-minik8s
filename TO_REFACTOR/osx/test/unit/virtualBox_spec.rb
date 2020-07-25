# Test Case to understand if VirtualBox is working properly

control 'VirtualBox' do

  describe file('/usr/local/bin/VirtualBox') do
    it { should exist }
  end

  describe file('/usr/local/bin/VBoxManage') do
    it { should exist }
  end

  describe bash('VBoxManage list vms') do
    its('exit_status') { should eq 0 }
  end
end