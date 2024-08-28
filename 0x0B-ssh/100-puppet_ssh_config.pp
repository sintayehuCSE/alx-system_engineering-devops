# Configure client-side ssh configuration file

file_line { 'Turn off password auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}

file_line { 'Add Identity Key':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}