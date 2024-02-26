#Executing some command in puppet

exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}
