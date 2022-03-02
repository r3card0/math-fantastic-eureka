# create a function to determine the second bigger number from a list

# function secondLargestNumber(numbers) {
#     let first = numbers[0];
#     let second = 0;
#     for (let i = 0; i < numbers.length; i++) {
#         if (numbers[i] > first) {
#             second = first;
#             first = numbers[i]
#         }
#         if (numbers[i] > second && numbers[i] < first) {
#             second = numbers[i];
#         }
#     }
#     return second
# }
# let nums = [8,4,6,10,9,11]
# secondLargestNumber(nums);
# console.log(secondLargestNumber(nums));

def secondLargestNumber(list_number):
    
    first = list_number[0]
    second = 0
    # print(first)
    for i in list_number:
        if list_number[i] > first:
            i += 1
            second = first
            first = list_number[i]
        elif list_number[i] > second and list_number[i] < first:
            second = list_number[i]


if __name__=="__main__":
    secondLargestNumber([8,4,6,10,9,11])
   