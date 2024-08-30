// Example POST method implementation:
async function postData(url = "", data = {}) {
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    });
    return response.json();
}



sendButton.addEventListener("click",async ()=>{
    alert("Hey you click me! sweet")
    questionInput = document.getElementById("input_question").value;
    document.getElementById("input_question").value = "";
    document.querySelector(".right2").style.display = "block"
    document.querySelector(".right1").style.display = "none"

    question1.innerHTML = questionInput;
    question2.innerHTML = questionInput;

    //get the question from the user and populate the answer here.
    let result = await postData("/api", {"question": questionInput})
    solution.innerHTML = result.result

})