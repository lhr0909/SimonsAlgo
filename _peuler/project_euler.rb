require "benchmark"

n = 10
(1..n).each do |i|
  require File.expand_path(File.dirname(__FILE__) + '/p%03i' % i)
end

p = Hash.new

Benchmark.bm(3) do |x|
  (1..n).each do |i|
    problem_number = "%03i" % i
    x.report(problem_number + ":") {p[problem_number] = send("answer_" + problem_number)}
  end
end

puts
(1..n).each do |i|
  puts "Answer #{"%03i" % i}: #{p["%03i" % i]}"
end
