from errbot import BotPlugin, botcmd, re_botcmd, arg_botcmd
from config import CONSUL_HOST
import consul

class ConsulPlugin(BotPlugin):
    @botcmd
    @arg_botcmd('key', type=str)
    @arg_botcmd('branch', type=str)
    def consul_get_value(self, msg, branch=None, key=None):
        """Get value for particular branch and key from Consul."""
        c = consul.Consul(host=CONSUL_HOST)
        key = 'versions/'+branch+'/'+key
        index, data = c.kv.get(key)
        v = data['Value']
        yield ('{} value is: {}'.format(key, v.decode("utf-8")))

    @botcmd
    @arg_botcmd('destination', type=str)
    @arg_botcmd('source', type=str)
    def consul_copy_branch(self, msg, source=None, destination=None):
        """Copy one Consul branch to another."""
        c = consul.Consul(host=CONSUL_HOST)
        key = 'versions/' + source + '/'
        index, data = c.kv.get(key, recurse=True)
        for d in data:
            key = d['Key']
            value = d['Value']
            key = key.replace(source, destination, 1)
            c.kv.put(key, value)

    @botcmd
    @arg_botcmd('branch', type=str)
    def consul_list_branch(self, msg, branch=None):
        """List values for particular branch in Consul."""
        c = consul.Consul(host=CONSUL_HOST)
        key = 'versions/' + branch + '/'
        index, data = c.kv.get(key, recurse=True)
        for a in data:
            yield ('{}/{}'.format(a['Key'], a['Value'].decode("utf-8")))

    @botcmd
    @arg_botcmd('value', type=str)
    @arg_botcmd('key', type=str)
    @arg_botcmd('branch', type=str)
    def consul_update_value(self, msg, branch=None, key=None, value=None):
        """Update value of particular key in Consul"""
        c = consul.Consul(host=CONSUL_HOST)
        key = 'versions/' + branch + '/' + key
        c.kv.put(key, value)