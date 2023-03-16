let userInfo = {
    email: '',
    password: ''
};
let go = document.querySelector('#spam-button');
let results = document.querySelector('#lower-wrapper');


go.addEventListener('click', () => {
    getUserData();
});

function getUserData() {
    userInfo.email = document.querySelector('input#email_').value;
    userInfo.password = document.querySelector('input#password_').value;
    document.querySelector('input#email_').value = "";
    document.querySelector('input#password_').value = "";


    console.log('email: ', userInfo.email);
    console.log('password: ', userInfo.password);

    results.classList.remove('hide_');
    sendRequest(userInfo);
}

function sendRequest(data) {
    // send a POST request to the user-data endpoint
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/user-data/', true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", document.getElementsByName("csrfmiddlewaretoken")[0].value);
    console.log("data: ", JSON.stringify(data))
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            // handle response from Django Views modules
            console.log('xhr.responseText: ', xhr.responseText);
        }
    };
    xhr.send(JSON.stringify(data))
}