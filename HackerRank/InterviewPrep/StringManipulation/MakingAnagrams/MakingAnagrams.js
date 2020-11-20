function makeAnagram(a, b) {
  let aArr = a.split("");
  let bArr = b.split("");
  let deleted = [];
  if (aArr.length <= bArr.length) {
    for (let i = 0; i < aArr.length; i++) {
      if (bArr.includes(aArr[0])) {
        bArr.splice(bArr.indexOf(aArr[0]), 1);
        aArr.shift();
      }
    }
  } else {
    for (let i = 0; i < bArr.length; i++) {
      if (bArr.includes(aArr[0])) {
        bArr.splice(bArr.indexOf(aArr[0]), 1);
        aArr.shift();
      }
    }
  }
}
