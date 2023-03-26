# A manifest to kill a process `killmenow`
exec { 'kill process killmenow on all puppet-agents':
  command  => 'pkill killmenow',
  path     => '/bin:/usr/bin',
  onlyif   => 'pgrep killmenow',
  provider => 'shell'
}
