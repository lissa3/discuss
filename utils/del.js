
function lookLike(addr,psw){
//     const head = addr.split('@',1)[0];    
//     if ( psw.indexOf(head) >= 0){
//       console.log("found match")
//       return true
//     }else{
//       console.log("match not found");
//       return false
//     }
//   }
function lookLike2(addr,psw){
    const head = addr.split('@',1)[0];    
    if ( psw.includes(head) >= 0){
      console.log("found match")
      return true
    }else{
      console.log("match not found");
      return false
    }
  }


 console.log("starting looklike");
 console.log(lookLike2("do@mail.vb","doty"));

// is_numeric:helpers.regex("alpha",/^(?=.*?[^0-9])/,)
// const allowerdChars = helpers.regex('allowedChars',/^[a-zA-Z]*$/)
// v-if="!/(?=.*[A-Z])/.test(this.password)"

//valid: function(value) {
//       const containsUppercase = /[A-Z]/.test(value)
//       const containsLowercase = /[a-z]/.test(value)
//       const containsNumber = /[0-9]/.test(value)
//       const containsSpecial = /[#?!@$%^&*-]/.test(value)
//       return !containsUppercase || !containsLowercase || !containsNumber || !containsSpecial