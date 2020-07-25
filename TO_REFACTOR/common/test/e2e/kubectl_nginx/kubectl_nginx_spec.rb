control('E2E tests') do

  # Create the docker image of nginx + test site
  describe bash('eval $(minikube docker-env) && docker build -t ironmike:v1 ../common/test/e2e/kubectl_nginx') do
    its('stdout') { should match 'Successfully built' }
    its('exit_status') { should eq 0 }
  end

  # deploy the container
  describe bash('kubectl run ironmike --image=ironmike:v1 --port=80') do
    its('stdout') { should match 'created' }
    its('exit_status') { should eq 0 }
  end
  describe bash('kubectl get deployments') do
    its('stdout') { should match 'ironmike' }
    its('exit_status') { should eq 0 }
  end

  # expose the container
  describe bash('kubectl expose deployment ironmike --type=LoadBalancer') do
    its('stdout') { should match 'exposed' }
    its('exit_status') { should eq 0 }
  end
  
  # wait the service and show the page in the browser
  describe bash('minikube service ironmike') do #This command loop until the Pod is available!
    its('exit_status') { should eq 0 }
  end

  # Check it also via CURL: get the minikube IP and the port and then CURL to check the content
  describe bash('minikube ip > /tmp/e2e-test-kubectl.ip') do
    its('exit_status') { should eq 0 }
  end
  describe file('/tmp/e2e-test-kubectl.ip') do
    it { should exist }
  end
  describe bash("kubectl get services | grep ironmike | awk '{print $5}' | sed -e 's/:/\\ /g'| sed -e 's/,/\\ /g'| sed -e 's/\\//\\ /g' | awk '{print $2}' > /tmp/e2e-test-kubectl.port") do
    its('exit_status') { should eq 0 }
  end
  describe file('/tmp/e2e-test-kubectl.port') do
    it { should exist }
  end
  describe bash('curl http://`cat /tmp/e2e-test-kubectl.ip`:`cat /tmp/e2e-test-kubectl.port`') do
    its('stdout') { should match 'IronMike Test Site' }
    its('exit_status') { should eq 0 }
  end

  # purge
  describe bash('kubectl delete services ironmike') do
    its('stdout') { should match 'service "ironmike" deleted' }
    its('exit_status') { should eq 0 }
  end
  describe bash('kubectl delete deployments ironmike') do
    its('stdout') { should match 'deployment.extensions "ironmike" deleted' }
    its('exit_status') { should eq 0 }
  end

  #TODO: delete also pods!

end