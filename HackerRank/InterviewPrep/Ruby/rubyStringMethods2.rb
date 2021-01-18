# Enter your code here
def mask_article(string, arr)
    #puts string
    #puts arr
    arr.each {|element| 
        if string.include? element
            strikeText = strike(element)
            string = string.gsub(element, strikeText)
        end
    }
    #puts string
    return string
end

def strike(string)
    string = "<strike>#{string}</strike>"
    return string
end
