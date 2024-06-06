const form = document.querySelector("form")
function sendEmail(){
    Email.send({
        Host : "smtp.elasticemail.com",
        Username : "ridesharehub2024@gmail.com",
        Password : "30F38E96E2020B75D419EDFDFA6286FEE2AA",
        To : 'ridesharehub2024@gmail.com',
        From : "ridesharehub2024@gmail.com",
        Subject : "This is the subject",
        Body : "And this is the body"
    }).then(
      message => alert(message)
    );
}
form.addEventListener("submit",(e)=>{
    e.preventDefault();
    sendEmail();
})