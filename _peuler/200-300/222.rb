total_length = 0.0
for i in 30..49
    c = 2 * i + 1
    b = 100 - 3 * i - 1
    total_length += Math.sqrt(c**2 - b**2)
end

puts total_length * 1000