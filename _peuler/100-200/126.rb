@C = {}

@max = 20000

@value = 1000

def time_diff(start, finish)
   (finish - start)
end

def surface_area (a, b, c)
    2 * a * b + 2 * b * c + 2 * c * a
end

def cubes_used (a, b, c, layer)
	surface_area(a, b, c) + (layer-1) * 4 * (a + b + c) + ((layer-2)*(layer-1) / 2) * 8
end

def main()
    i = 1
    while cubes_used(i, 1, 1, 1) < @max
        # puts i
        # t2 = Time.now
        # puts time_diff @t1, t2
        j = i
        while cubes_used(i, j, 1, 1) < @max
            k = j
            while cubes_used(i, j, k, 1) < @max
                #puts "#{i} #{j} #{k}"
                l = 1
                while cubes_used(i, j, k, l) < @max
                    cu = cubes_used(i, j, k, l)
                    if @C.include? cu
                        @C[cu] += 1
                    else
                        @C[cu] = 1
                    end
                    l += 1
                end
                k += 1
            end
            j += 1
        end
        i += 1
    end

    min = @max ** 3
    puts min
    @C.each do |key, value|
        if value == @value
            if key < min
                min = key
            end
        end
    end
    puts min
end

@t1 = Time.now
main
t2 = Time.now
puts time_diff @t1, t2