def process_text(arr)
    #puts arr.length
    newString = ""
    arr.each {|string|
        #p string
        #string = string.chomp
        #p string
        string = string.strip
        #p string
        newString += " #{string}"
        #p newString
        }
    newString = newString.strip
    #puts newString
    return newString
end
