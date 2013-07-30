Automated Load Balancing with Amazon EC2 and RightScale
#######################################################
:date: 2012-04-29 01:49
:author: Josh
:category: Articles
:tags: BASH, CentOS, EC2, RightScale
:slug: automated-load-balancing-with-amazon-ec2-and-rightscale

If you have a scalable infrastructure on Amazon, you are probably using
Elastic Load Balancers on Amazon's AWS to manage mulitple EC2 instances.
Scaling by hand is soooooo last decade! We have added 3 scripts to our
servers to allow them to add themselves and remove themselves our load
balancer. These machines are usually web servers or other application
servers. You can use RightScale to manage the expansion with auto
scaling, or you can have a custom server monitoring your cluster's load.
With these boot and decommission scripts, the servers will automatically
add and take themselves out of the cluster when they are told to
start/stop.

The first Rightscript installs the Amazon EC2 API tools and passes all
your credentials into the AMI through RightScale's platform. You can
fill in the inputs on a server by simply selecting the drop down next to
them, selecting "Cred" and then changing the next drop down to match the
label for that input. For example, match "AWS\_ACCESS\_KEY\_ID" with
"AWS\_ACCESS\_KEY\_ID". This script was originally from the RightScale
documentation. This script should be assigned as a boot script to your
server template as the 2nd to last script (with the ELB Registration
script as the last).

.. code-block:: bash

	#!/bin/bash
	# installs ec2inst script that allows running ec2commands from the shell

    echo "$AWS\_X509\_CERT" > /root/cert.pem
	echo "$AWS\_X509\_KEY" > /root/key.pem

    echo 'export AWS\_ACCESS\_KEY\_ID='$AWS\_ACCESS\_KEY\_ID > /root/ec2inst
	echo 'export AWS\_SECRET\_ACCESS\_KEY='$AWS\_SECRET\_ACCESS\_KEY >> /root/ec2inst
	echo 'export AWS\_ACCOUNT\_NUMBER='$AWS\_ACCOUNT\_NUMBER >> /root/ec2inst
	echo 'export EC2\_CERT=/root/cert.pem' >> /root/ec2inst
	echo 'export EC2\_PRIVATE\_KEY=/root/key.pem' >> /root/ec2inst
	echo 'export EC2\_HOME=/root/ec2' >> /root/ec2inst
	echo 'export JAVA\_HOME=/usr/java/default' >> /root/ec2inst

    chmod 700 /root/ec2inst

    cd /root
	wget http://s3.amazonaws.com/ec2-downloads/ec2-api-tools.zip
	unzip ec2-api-tools.zip
	chmod +x ec2-api-tools-1.3-46266/bin/\*
	ln -s ec2-api-tools-1.3-46266 ec2



The next script should be assigned as a boot script for your server
template as the last script. It need to have the previous script run
before it can run. It installs the AWS ELB API tools, saves the
pertinent data to files for the decommission script, and then notifies
the ELB there is a new instance available. Its sole input is the name of
the Elastic Load Balancer you want it assigned to.

.. code-block:: bash

	#!/bin/bash
	echo "Beginning ELB Registration for load balancer $LOAD\_BALANCER."
	source /root/ec2inst
	export EC2\_INSTANCE\_ID="$( wget -q -O - http://169.254.169.254/latest/meta-data/instance-id )"

    wget -O /root/ElasticLoadBalancing.zip http://ec2-downloads.s3.amazonaws.com/ElasticLoadBalancing.zip
	unzip -o /root/ElasticLoadBalancing.zip -d /root
	export AWS\_ELB\_HOME=~/ElasticLoadBalancing-1.0.15.1
	echo 'export EC2\_INSTANCE\_ID='$EC2\_INSTANCE\_ID > /root/ec2elb
	echo 'export AWS\_ELB\_HOME='$AWS\_ELB\_HOME >> /root/ec2elb

    $AWS\_ELB\_HOME/bin/elb-register-instances-with-lb $LOAD\_BALANCER --instances $EC2\_INSTANCE\_ID
	echo "ELB Registration for load balancer $LOAD\_BALANCER finished with exit code $?"


The final script should be added as one of the first decommission
scripts in your server template. It will notify the load balancer to
stop sending requests to this instance. Its sole input is the name of
the Elastic Load Balancer you want it assigned to.

.. code-block:: bash

	#!/bin/bash
	echo "Starting ELB Deregistering."
	source /root/ec2inst
	source /root/ec2elb

    $AWS\_ELB\_HOME/bin/elb-deregister-instances-from-lb $LOAD\_BALANCER --instance $EC2\_INSTANCE\_ID
	echo "ELB Deregistration finished with exit code $?"


