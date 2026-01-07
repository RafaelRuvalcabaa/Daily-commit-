function burbleSort(arr){
    for(let i = 0; i<arr.length; i++){
        for(let j=0; j<arr.length;j++){
            if (arr[j] > arr[j+1]){
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            }
        }
    }
    return arr; 
}


console.log(burbleSort([2,3,5,7,9,7,4,2,1,4,6,8,9,7,4,2,3,5,7,6,55,4]))

//Iteracion 1 - Ordenó el 87 que es mayor que 7 
// temp = arr [j] = 89 
// arr [j] = 89 ---- arr[j+1] = 7
// arr[j+1] = 7 ----- temp = 7 
