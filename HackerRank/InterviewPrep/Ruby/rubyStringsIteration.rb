# Your code here
def count_multibyte_char(string)
    #puts string.length
    count = 0
    string.each_char {|char| 
        if char.bytesize > 1
            count+=1
        end
        }
    #puts count
    return count
end
