# A puppet script to increase the limit of concurrent tasks in an nginx server
file {'/etc/default/nginx':
  ensure	=> file,
  content	=> "ULIMIT -n 4096\n",
}
