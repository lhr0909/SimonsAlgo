require 'set'

module PEulerMath
  class Fibonacci
    attr_accessor :fibs

    def initialize
      @fibs = Hash.new
      @fibs[0] = 1
      @fibs[1] = 2
    end

    def fib(n)
      #Recursive implementation
      # if n < 0
      #   0
      # elsif n == 0
      #   1
      # elsif n == 1
      #   2
      # else
      #   fib(n-1) + fib(n-2)
      # end
      if n < 0
        0
      elsif @fibs.include?(n)
        fibs[n]
      else
        fibs[n] = fib(n-1) + fib(n-2)
        fibs[n]
      end
    end

    def fibs_not_exceeding(n)
      fibs = []
      i = 0
      while fib(i) <= n
        fibs <<= fib(i)
        i += 1
      end
      fibs
    end
  end
  
  class Prime
    attr_accessor :primes, :upper_limit

    def initialize(n)
      generate_primes(n)
    end
    
    def generate_primes(n)
      #Generates all primes under n
      #Sieve of Eratosthenes
      @primes = (0...n).to_a
      @primes[0] = @primes[1] = nil
      @primes.each do |p|
        next unless p
        break if p * p > n
        (p * p).step(n, p) {|m| @primes[m] = nil}
      end
      @primes = @primes.compact
      @upper_limit = n
    end

    def prime_factors(n)
      factors = []
      @primes.each do |i|
        while n % i == 0
          factors <<= i
          n /= i
        end
        if n == 1
          break
        end
      end
      factors
    end

    def prime_factor_set(n)
      prime_factors(n).to_set
    end
    
    def prime_factor_hash(n)
      factors = prime_factors(n)
      factor_set = factors.to_set
      fac_hash = Hash.new
      factor_set.each do |f|
        fac_hash[f] = factors.count(f)
      end
      fac_hash
    end
    
    def nth_prime(n)
      #If there aren't enough primes, re-make with 10 times the upper-limit
      while n > @primes.length
        generate_primes(10 * @upper_limit)
      end
      @primes[n-1]
    end

    def self.prime?(n)
      (2...Math.sqrt(n).to_i).each do |i|
        if n % i == 0
          return false
        end
      end
      true
    end
  end
end