# File: 2-puppet_custom_http_response_header.pp

# Ensure Nginx is installed and running
class { 'nginx':
  ensure => 'running',
}

# Define a custom fact to retrieve the hostname
Facter.add('custom_served_by') do
  setcode do
    Facter.value(:hostname)
  end
end

# Define the custom HTTP header in the Nginx configuration
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => "server_tokens off;\nadd_header X-Served-By $::custom_served_by;",
  notify  => Service['nginx'],
}
