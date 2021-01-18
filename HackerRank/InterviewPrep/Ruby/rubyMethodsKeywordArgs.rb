# Your code here
def convert_temp(temp, **options)
    temp = temp.to_f
    if options[:input_scale] == 'kelvin' && options[:output_scale] == 'fahrenheit'
        temp = (temp - 273.15) * (9.0/5.0) + 32.0
        return temp
    elsif options[:input_scale] == 'kelvin' && options[:output_scale] == 'celsius'
        temp = temp - 273.15
        return temp
    elsif options[:input_scale] == 'fahrenheit' && options[:output_scale] == 'kelvin'
        temp = ((temp - 32.0) * (5.0/9.0)) + 273.15
        return temp
    elsif options[:input_scale] == 'fahrenheit' && options[:output_scale] == 'celsius'
        temp = ((temp - 32.0) * (5.0/9.0))
        return temp
    elsif options[:input_scale] == 'celsius' && options[:output_scale] == 'fahrenheit'
        temp = (temp * (9.0/5.0)) + 32.0
        return temp
    elsif options[:input_scale] == 'celsius' && options[:output_scale] == 'kelvin'
        temp = temp + 273.15
        return temp
    end
end
