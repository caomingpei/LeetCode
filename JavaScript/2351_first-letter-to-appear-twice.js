/**
 * @param {string} s
 * @return {character}
 */
var repeatedCharacter = function(s) {
    let arr = Array(26).fill(0);
    for (let i=0; i<s.length;i++){
        let index = s[i].charCodeAt()-'a'.charCodeAt();
        arr[index] += 1;
        if (arr[index] >= 2){
            return s[i];
        }
    }
};


s = "abccbaacz"
console.log(repeatedCharacter(s))