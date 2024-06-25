# Helm 💾

#### What is Helm?

Helm is a package manager for Kubernetes that allows you to define, install, and upgrade even the most complex Kubernetes applications. It can be looked as the apt, yum or brew for Kubernetes.

#### Short Example

Say you have a Kubernetes cluster running and you want to deploy the Elastic Stack (Elasticsearch, Kibana, Logstash) on it.
In order to deploy the Elastic Stack on Kubernetes, you would need to create a bunch of Kubernetes resources (deployments, services, etc.) and manage them. This is where Helm comes in.
Helm allows you to define the Elastic Stack as a chart, so called Helm Charts (a collection of files that describe a related set of Kubernetes resources) and then install that chart on your Kubernetes cluster.
This way, you can deploy the Elastic Stack on Kubernetes with a single command.
