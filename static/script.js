const form = document.querySelector('#form');

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const jsonObject = Object.fromEntries(formData);
    const jsonString = JSON.stringify(jsonObject);
    //console.log(jsonString);
    
    const url = 'http://localhost:8000';

    const response = await fetch(url, {
        method: 'POST',
        body: jsonString,
        headers: {
            'Content-Type': "application/json; charset=UTF8",
            Accept: "application/json",
        }
    })
        .then(response => response.json())
        .then(json => console.log(json))
        .then(json => appendData(json))
        .catch(err => console.log(err));    

    function appendData(data){
        var mainContainer = document.getElementById("answer");
        var div = document.createElement("div");
        div.innerHTML = 'RESULT : ' + data[0].result;
        mainContainer.appendChild(div);
    }
      
});