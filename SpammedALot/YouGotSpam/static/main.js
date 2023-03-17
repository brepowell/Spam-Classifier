let userInfo = {
    user: '',
    name: '',
    email: '',
    password: ''
};

let go = document.querySelector('#spam-button');
let getFull = document.querySelector('#spam-button-full')
let results = document.querySelector('#results');
let directions = document.querySelector('#gmail-imap');


go.addEventListener('click', () => {
    getUserData();
});

// Sync with template to get user input
function getUserData() {
    userInfo.user = document.querySelector('input#user_').value;
    userInfo.name = document.querySelector('input#name_').value;
    userInfo.email = document.querySelector('input#email_').value;
    userInfo.password = document.querySelector('input#password_').value;

    // clear after storage
    document.querySelector('input#user_').value = '';
    document.querySelector('input#name_').value = '';
    document.querySelector('input#email_').value = '';
    document.querySelector('input#password_').value = '';

    results.classList.remove('hide_');
    directions.classList.add('hide_');
    sendRequest(userInfo);
}

// Give data to Python View
function sendRequest(data) {
    // send a POST request to the user-data endpoint
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/user-data/', true);    
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", document.getElementsByName("csrfmiddlewaretoken")[0].value);

    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            // handle response from Django Views modules
            console.log('xhr.responseText: ', xhr.responseText);
        }
    };

    console.log("sending data to View: ", JSON.stringify(data))
    xhr.send(JSON.stringify(data))
    // after sending user input, get what View processed
    getResponse();
}

// Get processed data from Python View
function getResponse() {
    fetch('user-data')
    .then(response => response.json())
    .then(data => {
        console.log('What Python sent: ', data)
        let rec_user = '';
        let rec_name = '';
        let rec_email = '';
        let rec_password = '';

        rec_user = data.user;
        rec_name = data.name;
        rec_email = data.email;
        rec_password = data.password;

        console.log(data)

        // doing something with the data received from Python
        let uVal = document.querySelector('#u_val');
        let nVal = document.querySelector('#n_val');
        let eVal = document.querySelector('#e_val');
        let pVal = document.querySelector('#p_val');
        uVal.innerText = String(' ' + rec_user);
        nVal.innerText = String(' ' + rec_name);
        eVal.innerText = String(' ' + rec_email);
        pVal.innerText = String(' ' + rec_password);
    } )
    .catch(error => console.error(error));
}
