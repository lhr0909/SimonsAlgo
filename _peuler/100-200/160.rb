def f(n)
  x = 1
  for i in 2..n
    if i % 100000 == 0
      puts i
    end
    x = x * i
    while x % 10 == 0
      x /= 10
    end
    x = x % 100000
  end
  x
end


def ff(n)
  x = (1..n).to_a.reduce(:*)
  while x % 10 == 0
    x /= 10
  end
  x % 100000
end

puts f(1000000000000)