# django_to_deployment

1. Run test
    ```
    python manage.py test
    ```

2. Build conatiner
    ```
    docker build -f Dockerfile \
        -t registry.digitalocean.com/deeptest/prostore:latest \
        -t registry.digitalocean.com/deeptest/prostore:v1 \
        .
    ```
3. Push this container to DO Container registry
    ```
    docker push registry.digitalocean.com/deeptest/prostore --all-tags
    ```
4. Update secrets

    ```
    kubectl delete secret deep-test-prod-env
    kubectl create secret generic deep-test-prod-env --from-env-file=pro_store/.env.prod
    ```
5. Update deployment

    ```
    kubectl apply -f deep-test-ks.yaml
    ```
6. Wait for Rollout to finish
    ```
    kubectl rollout status 
    ```
7. Migrate Database
    export SINGLE_POD_NAME=$(kubectl get pod -l app=deeptest-deployment -o jsonpath="{.items[0].metadata.name}")
    ```
    kubectl exec -it $SINGLE_POD_NAME -- bash /app/migrate.sh




https://www.kubegres.io/doc/getting-started.html
https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nginx-ingress-on-digitalocean-kubernetes-using-helm

