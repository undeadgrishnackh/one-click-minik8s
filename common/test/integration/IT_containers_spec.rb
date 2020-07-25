control 'Integration test to check the conteiner engine' do

  #FIXME: where is this cxommand in linux??
  describe file('/Applications/Docker.app/Contents/MacOS/com.docker.diagnose') do
    it { should exist }
  end
 
  describe bash('/Applications/Docker.app/Contents/MacOS/com.docker.diagnose gather') do
    its('exit_status') { should eq 0 }
  end

end