# errbot-consul
Simple plugin for integration between Errbot and Consul KV Storage.

## Usage:
Let's say you have Consul KV Storage with the following structure:
- *master/key1*
- *master/key2*
- *develop/key1*

and so on.

### !consul_list_branch
*!consul_list_branch %branch%*
List values for particular branch.
Example: *!consul_list_branch develop*
This command will list all keys and their values in "develop" branch.

### !consul_copy_branch
*!consul_copy_branch %source_branch% %destination_branch%*
Copy all keys and their values from source branch to destination branch.
Example: *!consul_copy_branch develop master*
This command will copy all keys and their values from "develop" branch to "master" branch.

### !consul_get_value
*!consul_get_value %key%
Get value of particular key.
Example: *!consul_get_value develop/key2*
This command will return value of key2 in "develop" branch.

### !consul_update_value
*!consul_update_value %branch% %key% %value%
Update value of particular key with given value.
Example: *!consul_update_value master key1 foo
This command will update value of key1 in "master" branch to "foo" value.

## Install:
1. Copy *consul-plugin* directory to Errbot's *plugins* directory.
2. Add the address of your Consul KV in Errbot's *config.py* file as CONSUL_HOST variable.
