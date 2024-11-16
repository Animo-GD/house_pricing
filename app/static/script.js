const form = document.getElementById("data-form")
const resultDiv = document.getElementById('result')

form.addEventListener('submit',async (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries())
    const response = await fetch("http://127.0.0.1:8000/predict",{
        method:'POST',
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify(data)
    });
    const result = await response.json();
    console.log(result.predicted_house_price.toFixed(2));
    resultDiv.textContent = `Predicted House Price: $${result.predicted_house_price.toFixed(2)}`;
});