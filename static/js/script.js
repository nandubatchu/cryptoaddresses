const address_field = document.getElementById('address')
const currency_field = document.getElementById('currency')
const validation_response = document.getElementById('validation_response')

let validate = () => {
    currency = currency_field.value
    address = address_field.value

    fetch(`/api/validate-address/${currency}/${address}`)
        .then(res => res.json())
        .then((res) => {
            validation_response.innerHTML = JSON.stringify(res.result);
        })
        .catch(err => console.log(err))
}

document.getElementById('validate').addEventListener('click', validate)


