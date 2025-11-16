

const checkout = (e) => {
    e.preventDefault();

    const phoneNumber = document.getElementById('phone-number').value;
    const email = document.getElementById('email').value;
    const fullName = document.getElementById('full-name').value;
    const address = document.getElementById('address').value;
    const instructions = document.getElementById('instructions').value || 'No Instruction';


    const paymentMethod = document.querySelector('input[name="payment-method"]:checked');
    const currency = paymentMethod && paymentMethod.value === 'usd' ? 'usd' : 'kmr';


    console.log(phoneNumber);
    console.log(email);
    console.log(fullName);
    console.log(address);
    console.log(instructions);
    console.log(currency);
};