const mysql = require('mysql');
const express = require('express');
const session = require('express-session');
const path = require('path');
const input_url =  process.env.input_host


function return_True() {
    return true;
}


const app = express();
app.use(session({
    secret: 'secret',
    resave: true,
    saveUninitialized: true
}));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'static')));

// http://localhost:3000/
app.get('/', function (request, response) {
    // Render login template
    console.log('Input page is set to: ' + input_url)
    response.sendFile(path.join(__dirname + '/login.html'));
});

// http://localhost:3000/auth
app.post('/auth', function (request, response) {
    // Capture the input fields
    let username = request.body.username;
    let password = request.body.password;
    // Ensure the input fields exists and are not empty
    if (username == password) {
        // for now, just always redirect to /home
        request.session.loggedin = true;
        request.session.username = username;
        // Redirect to home page
        response.redirect('http://'+ input_url +':3001/input?username=' + username);
    } else {
        // response.send('Login Failed !!!!');
        // response.end();
        response.redirect('/');
    };
});

// http://localhost:3000/home
app.get('/home', function (request, response) {
    // If the user is loggedin
    if (request.session.loggedin) {
        // Output username
        response.send('Welcome back, ' + request.session.username + '!');
    } else {
        // Not logged in
        response.send('Please login to view this page!');
    }
    response.end();
});

app.listen(3000);
