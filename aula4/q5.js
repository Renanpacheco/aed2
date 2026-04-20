//let vector=[5,7,10,4,9]
let vector=[5,7,2,4,9]
let ten= 0
let sum= 0
console.log(vector[0])
console.log(vector[4])

for (let i= 0; i< vector.length; i++){
    if (vector[i] == 10){
        ten=i
    }
    sum= sum+ vector[i]
}

console.log(sum)
if (ten>0){
    console.log("the 10 is on the position: ", ten+1)
}else{
    console.log("the value 10 is not found")
}
