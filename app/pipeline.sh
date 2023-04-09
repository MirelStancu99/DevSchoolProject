#!/bin/bash

bool=0
if [[ $# -lt 1 ]]; then
        echo "Please provide a command for this script. To see all the commands available, try "help" command."
        bool=1
else
        cmd=$1
fi

if [[ $# -lt 3 ]]; then
        arg1=$(echo $2| cut -d'=' -f2)
else
        arg1=$(echo $2 | cut -d'=' -f2)
        arg2=$(echo $3 | cut -d'=' -f2)
        arg3=$(echo $4 | cut -d'=' -f2)
fi

case $cmd in
    build)
        #output=$(docker build -t $arg2:$arg3 $arg1)
        #if echo "$output" | grep -q "error"; then
        #       echo "Wrong arguments for the command $cmd. To see the right use, try "help" command."
        #fi
        docker build -t $arg2:$arg3 $arg1
        ;;
    push)
        docker tag $arg2 $arg1/$arg2:$arg3
        docker push $arg1/$arg2:$arg3
        ;;
    pushacr)
        az login
        ACR_NAME=$arg1
        az acr login --name $ACR_NAME
        docker tag $arg2 $ACR_NAME.azurecr.io/$arg2:$arg3
        docker push $ACR_NAME.azurecr.io/$arg2:$arg3
        ;;
    deploy)
        if [[ $arg1 == "docker" ]]; then
            docker container run -dp 5000:5000 $arg2:$arg3
        elif echo "$arg2" | grep -q "deployment"; then
                arg4=$(echo $5 | cut -d'=' -f2)
                arg5="${arg3}:${arg4}"
                sed -i "s@image:.*@image: $arg5@" $arg2 2> /dev/null
                minikube start
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
    help)
        cat manual.txt
        ;;
    *)
        if [[ $bool -eq 0 ]]; then
                echo "Invalid command: $cmd. To see all the commands available, try "help" command."
        fi
        ;;
esac

exit 0
