function checkMagazine(magazine, note) {
  for(let i=0; i<note.length; i++){
      if(magazine.includes(note[i])){
         let index = magazine.indexOf(note[i]);
         magazine.splice(index, 1);
      }else{
          return console.log("No");
      }
  }
  return console.log("Yes");
}
