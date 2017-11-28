# errbot-consul
Simple plugin for integration between Errbot and Consul KV Storage.

## Usage:
Let's say you have Consul KV Storage with the folowing structure:
*versions/master/key1*
*versions/master/key2*
*versions/develop/key1*
and so on.

### !consul_list_branch
*!consul_list_branch %branch%*
List values for particular branch.
Example: *!consul_list_branch develop*
This command will list all keys and their values in branch "develop".

### !consul_copy_branch
*!consul_copy_branch %source_branch% %destination_branch%*
Copy all keys and their values from source branch to destination branch.
Example: *!consul_copy_branch develop master*
This command will copy all keys and their values from "develop" branch to "master"

### !consul_get_value

### !consul_update_value

## Install:
