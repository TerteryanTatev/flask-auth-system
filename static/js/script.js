document.addEventListener('DOMContentLoaded', function () {
    const toggleButtons = document.querySelectorAll('.toggle-password');
    toggleButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const targetId = button.getAttribute('data-target');
            const input = document.getElementById(targetId);
            if (input.type === 'password') {
                input.type = 'text';
                button.textContent = 'Hide';
            } else {
                input.type = 'password';
                button.textContent = 'Show';
            }
        });
    });

    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        setupRegisterForm(registerForm);
    }

    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        setupLoginForm(loginForm);
    }
});

function isValidEmail(email) {
    const pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return pattern.test(email);
}

function isValidUsername(username) {
    return username.length >= 3 && username.length <= 20;
}

function getPasswordStrength(password) {
    let score = 0;
    if (password.length >= 8) score++;
    if (/[A-Z]/.test(password)) score++;
    if (/[a-z]/.test(password)) score++;
    if (/[0-9]/.test(password)) score++;
    if (/[!@#$%^&*(),.?":{}|<>]/.test(password)) score++;
    return score;
}

function isValidPassword(password) {
    return getPasswordStrength(password) === 5;
}

function setInputState(input, feedbackElement, isValid, message) {
    if (isValid) {
        input.classList.remove('invalid');
        input.classList.add('valid');
        feedbackElement.textContent = '';
        feedbackElement.classList.remove('success');
    } else {
        input.classList.remove('valid');
        input.classList.add('invalid');
        feedbackElement.textContent = message;
    }
}

function setupRegisterForm(form) {
    const usernameInput = document.getElementById('username');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const confirmInput = document.getElementById('confirm_password');
    const submitButton = document.getElementById('submitButton');

    const usernameFeedback = document.getElementById('usernameFeedback');
    const emailFeedback = document.getElementById('emailFeedback');
    const strengthText = document.getElementById('strengthText');
    const strengthFill = document.getElementById('strengthFill');
    const confirmFeedback = document.getElementById('confirmFeedback');

    function validateForm() {
        const usernameValid = isValidUsername(usernameInput.value.trim());
        const emailValid = isValidEmail(emailInput.value.trim());
        const passwordValid = isValidPassword(passwordInput.value);
        const confirmValid = confirmInput.value === passwordInput.value && confirmInput.value.length > 0;

        if (usernameInput.value.length > 0) {
            setInputState(usernameInput, usernameFeedback, usernameValid, 'Username must be 3-20 characters.');
        }

        if (emailInput.value.length > 0) {
            setInputState(emailInput, emailFeedback, emailValid, 'Please enter a valid email address.');
        }

        const strength = getPasswordStrength(passwordInput.value);
        updateStrengthBar(strength, passwordInput.value.length);

        if (confirmInput.value.length > 0) {
            setInputState(confirmInput, confirmFeedback, confirmValid, 'Passwords do not match.');
        }

        submitButton.disabled = !(usernameValid && emailValid && passwordValid && confirmValid);
    }

    function updateStrengthBar(score, length) {
        if (length === 0) {
            strengthFill.style.width = '0%';
            strengthText.textContent = '';
            return;
        }

        const percentages = ['20%', '40%', '60%', '80%', '100%'];
        const colors = ['#f87171', '#fb923c', '#facc15', '#a3e635', '#4ade80'];
        const labels = ['Very weak', 'Weak', 'Fair', 'Good', 'Strong'];

        const index = Math.max(score - 1, 0);
        strengthFill.style.width = percentages[index];
        strengthFill.style.background = colors[index];
        strengthText.textContent = labels[index];
        strengthText.classList.toggle('success', score === 5);
    }

    usernameInput.addEventListener('input', validateForm);
    emailInput.addEventListener('input', validateForm);
    passwordInput.addEventListener('input', validateForm);
    confirmInput.addEventListener('input', validateForm);

    validateForm();
}

function setupLoginForm(form) {
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const submitButton = document.getElementById('submitButton');

    const emailFeedback = document.getElementById('emailFeedback');
    const passwordFeedback = document.getElementById('passwordFeedback');

    function validateForm() {
        const emailValid = isValidEmail(emailInput.value.trim());
        const passwordValid = passwordInput.value.length > 0;

        if (emailInput.value.length > 0) {
            setInputState(emailInput, emailFeedback, emailValid, 'Please enter a valid email address.');
        }

        if (passwordInput.value.length === 0) {
            passwordFeedback.textContent = '';
            passwordInput.classList.remove('valid', 'invalid');
        }

        submitButton.disabled = !(emailValid && passwordValid);
    }

    emailInput.addEventListener('input', validateForm);
    passwordInput.addEventListener('input', validateForm);

    validateForm();
}