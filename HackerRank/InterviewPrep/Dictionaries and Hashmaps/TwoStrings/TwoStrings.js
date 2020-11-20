function twoStrings(s1, s2) {
  if(s1.length <= s2.length){
      for(let i=0; i<s1.length; i++){
          if (s2.includes(s1[i])){
              return "YES"
          }
      }
  }else{
      for(let i=0; i<s2.length; i++){
          if (s1.includes(s2[i])){
              return "YES"
          }
      }
  }
  return "NO"
}
