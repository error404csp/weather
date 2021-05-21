from flask import Flask, render_template, request, jsonify

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [5, 4, 16, 8, 9]
sort(nums)

bubble = print(nums)

@kaila_bp.route('/kailaData2', methods=['POST'])
def numbers():
    if request.method == "POST":
        return render_template("kaila2.html", bubble2=bubble)