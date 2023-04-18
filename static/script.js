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
        .then(data => {
            const resultDiv = document.querySelector('#result');
            resultDiv.innerHTML = `<pre>${JSON.stringify(data.CalcResult.result, null, 2)}</pre>`;
        })
        .catch(err => console.log(err));    
      
});
