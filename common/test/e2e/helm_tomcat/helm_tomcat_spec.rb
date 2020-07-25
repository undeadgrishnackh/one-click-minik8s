control 'E2E tests - install Tomcat with dedicated persistance volume via Helm' do

  # Create a dedicated pre existing persisted volume for the Tomcat Pod
  describe bash('minikube ssh \'sudo mkdir /mnt/data/\'') do
    its('exit_status') { should eq 0 }
  end
  describe bash('kubectl create -f ../common/test/e2e/helm_tomcat/persistanceVolume.yml') do
    its('exit_status') { should eq 0 }
  end

  # Add the bitnami Helm repo; install Tomcat and wait to display it in the browser
  describe bash('helm repo add bitnami https://charts.bitnami.com/bitnami') do
    its('exit_status') { should eq 0 }
  end
  describe bash('helm install --name e2e-test-tomcat --set tomcatUser=admin,tomcatPassword=admin bitnami/tomcat') do
    its('exit_status') { should eq 0 }
  end
  describe bash('minikube service e2e-test-tomcat-tomcat') do #This command loop until the Pod is available!
    its('exit_status') { should eq 0 }
  end

  # Check deeply in the system what in case was wrong
  describe bash('helm list | grep e2e-test-tomcat | grep DEPLOYED') do
    its('exit_status') { should eq 0 }
  end
  describe bash('kubectl get services | grep e2e-test-tomcat-tomcat') do
    its('stdout') { should match '80:'}
    its('exit_status') { should eq 0 }
  end
  describe bash('minikube ssh \'docker ps | grep e2e-test-tomcat-tomcat\'') do
    its('stdout') { should match /app-entrypoint/}
    its('exit_status') { should eq 0 }
  end

  describe bash('helm delete --purge e2e-test-tomcat') do
    its('stdout') { should match 'release "e2e-test-tomcat" deleted' }
    its('exit_status') { should eq 0 }
  end

end