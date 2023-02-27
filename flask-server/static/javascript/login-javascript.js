function SubmitLogin() {
  console.log('clicked login')
  let usernameInput = document.getElementById('username').value
  let passwordInput = document.getElementById('password').value
  console.log(`username ${usernameInput}`)
  console.log(`password ${passwordInput}`)
  if (usernameInput == 'admin' && passwordInput == 'admin') {
    window.location.replace('http://localhost:5000/gui')
  }
}
