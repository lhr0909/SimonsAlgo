require 'set'

total_configs = Hash.new
total_configs[1] = Set.new [Rational(1)]

max = 18

for i in 2..max
  total_configs[i] = Set.new
  for j in 1...i
    puts "#{i} #{j}"
    configs1 = total_configs[j]
    configs2 = total_configs[i-j]
    configs1.each do |c1|
      configs2.each do |c2|
      	total_configs[i].add(c1 + c2)
      	total_configs[i].add((c1 * c2) / (c1 + c2))
      end
    end
  end
end

values = Set.new
for i in 1..max
  values.merge(total_configs[i])
end

puts values.length