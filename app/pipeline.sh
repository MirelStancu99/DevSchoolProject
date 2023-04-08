#!/bin/bash

#-h, --help
 #         Display a help message.

  # COMMAND
   #       Specifies the action to perform. The available commands are:

    #      build   Build a Docker image from a Dockerfile.

     #     push    Push a Docker image to a remote repository.

      #    deploy  Deploy a Docker container using Kubernetes or Minikube.

       #   test    Test a URL by sending a GET request and checking the response status code.

 #  ARGUMENTS
  #        The arguments for each command are as follows:

   #       build   ARG1: path to the directory containing the Dockerfile.
    #              ARG2: name of the Docker image.
     #             ARG3: version of the Docker image.

      #    push    ARG1: Docker image name.
       #           ARG2: Docker registry URL.
        #          ARG3: Docker image version.

         # deploy  ARG1: deployment type (either "docker" or "kubernetes").
          #        ARG2: path to the deployment configuration file.
           #       ARG3: Docker image name.
            #      ARG4: Docker image version (only for Kubernetes deployments).
             #     ARG5: (optional) Kubernetes namespace (only for Kubernetes deployments).

         # test    ARG1: URL to test.

cmd=$1

if [[ $# -lt 3 ]]; then
        arg1=$(echo $2| cut -d'=' -f2)
else
        arg1=$(echo $2 | cut -d'=' -f2)
        arg2=$(echo $3 | cut -d'=' -f2)
        arg3=$(echo $4 | cut -d'=' -f2)
fi


case $cmd in
    build)
        docker build -t $arg2:$arg3 $arg1
        ;;
    push)
        docker tag $arg2 $arg1/$arg2:$arg3
        docker push $arg1/$arg2:$arg3
        ;;
    deploy)
        if [[ $arg1 == "docker" ]]; then
            docker container run -dp 5000:5000 $arg2:$arg3
    	elif echo "$arg2" | grep -q "deployment"; then
		arg4=$(echo $5 | cut -d'=' -f2)
		arg5="${arg3}:${arg4}"
		sed -i "s@image:.*@image: $arg5@" $arg2 2> /dev/null
           	kubectl apply -f $arg2
	    else
		kubectl apply -f $arg2
		minikube tunnel
		
        fi
        ;;
    test)
        response=$(curl -s -o /dev/null -w "%{http_code}" $arg1)
	    echo "Command: $response"
        if [[ $response -eq 200 ]]; then
            echo "Test passed: received 200 response"
        else
            echo "Test failed: received $response response"
            exit 1
        fi
        ;;
    man)
	    cat manual.txt
	;;
esac

exit 0
