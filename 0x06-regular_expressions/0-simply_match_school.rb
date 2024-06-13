#!/usr/bin/env ruby
#Scripts that deals Regular Expression /School/ or Regex

if ARGV.empty?
  puts "NO Arguments Passed"
  exit
end

regex = /School/

input_string = ARGV[0]

theSame = input_string.match(regex)

if theSame
  puts theSame[0]
else
  puts ""
end
