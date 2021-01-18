# Your code here
=begin
Example of what the method should return:

> serial_average('002-10.00-20.00')
"002-15.00"

We can choose to use interpolation like so:
> tmp = 123
> "Hello #{tmp}"
Hello 123

=end
def serial_average(string)
    #input has format SSS-XX.XX-YY.YY
    #output should have format SSS-ZZ.ZZ
    # ZZ.ZZ is the average of XX.XX and YY.YY
    #puts string
    sss = string[0,3]
    a = string[4,5]
    b = string[10,5]
    #puts a
    #puts b
    a = a.to_f
    b = b.to_f
    c = (a + b)/2.00
    c = c.round(2)
    #puts c
    string = "#{sss}-#{c}"
    #puts string
end
